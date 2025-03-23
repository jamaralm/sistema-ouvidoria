from db import connection, cursor
from config import queries
from datetime import datetime

'''
    ADD USER FUNCTION
'''

def add_user(name, email, password):
    data = (name, email, password)

    cursor.execute(queries['add_user'], data)
    connection.commit()

    print('\nUSUARIO ADICIONADO COM SUCESSO!')

'''
    ADD COMPLAINT FUNCTION
'''

def add_complaint(name, description, user_id):
    if not user_id == None:
        cursor.execute(queries['select_user'], (user_id,))
        user = cursor.fetchall()

        if user:
            data = (name, description, datetime.now(),user_id)

            cursor.execute(queries['add_complaint'], data)
            connection.commit()

            print('\nRECLAMACAO ADICIONADA COM SUCESSO!')
        else:
            print('\nERROR: USUARIO NAO ENCONTRADO!')
    else:
        data = (name, description, datetime.now())

        cursor.execute(queries['add_anonimous_complaint'], data)
        connection.commit()

        print('\nRECLAMACAO ADICIONADA COM SUCESSO!')

'''
    REMOVE USER FUNCTION
'''

def remove_user(user_id):
    cursor.execute(queries['select_user'], (user_id,))
    user = cursor.fetchone()

    if user:
        data = (user_id,)

        cursor.execute(queries['delete_user'], data)
        connection.commit()

        print('\nUSUARIO REMOVIDO COM SUCESSO!')
    else:
        print('\nERROR: usuario nao encontrado!')

'''
    REMOVE COMPLAINT FUNCTION
'''

def remove_complaint(complaint_id):
        data = (complaint_id,)

        cursor.execute(queries['delete_complaint'], data)
        connection.commit()

        print('\nRECLAMACAO REMOVIDA COM SUCESSO!')

'''
    LIST COMPLAINTS FUNCTION
'''

def list_complaints(): 
    cursor.execute(queries['list_complaints'])
    complaints = cursor.fetchall()

    print("\n--- LISTA DE RECLAMAÇÕES ---")
    print(f"{'ID':<5} | {'Título':<30} | {'Descrição':<50} | {'Data':<12} | {'Usuário':<15} | {'Status':<15}")
    print("-" * 140)

    for complaint in complaints:
        complaint_date = complaint[3].strftime('%d/%m/%Y') if complaint[3] else "N/A"
        cursor.execute(queries['select_user'], (complaint[4] ,))
        complaint_user = cursor.fetchall()

        if complaint[5] == True:
            is_complaint_done = 'Resolvida'
        elif complaint[5] == False:
            is_complaint_done = 'Nao Resolvida'

        for user_info in complaint_user:
            print(f"{complaint[0]:<5} | {complaint[1]:<30} | {complaint[2]:<50} | {complaint_date:<12} | {user_info[1]:<15} | {is_complaint_done:<15}")

    print("-" * 140)

'''
    LIST ALL COMPLAINTS FROM USER FUNCTION
'''

def list_user_complaints(user_id:int):
    cursor.execute(queries['select_complaint_from_user'], (user_id,))
    complaint_list = cursor.fetchall()
    cursor.execute(queries['select_user'], (user_id,))
    user_selected = cursor.fetchall()


    for user_info in user_selected:
        print(f'\nReclamacoes de {user_info[1]}:')
        for complaint in complaint_list:
            print(f'{complaint[0]}. {complaint[1]}')

'''
    MARK COMPLAINT AS DONE FUNCTION
'''

def mark_as_done(complaint_id):
    cursor.execute(queries['select_complaint'], (complaint_id,))
    complaint = cursor.fetchall()

    for complaint_info in complaint:
        if complaint_info[5] == 0:
            user_input = input(f'Voce deseja marcar a reclamacao "{complaint_info[1]}" como concluida? s/n\n')
            
            if user_input == 's':
                cursor.execute(queries['mark_complaint_as_done'], (complaint_id,))
                connection.commit()
                print('Status de reclamacao atualizado!')
            elif user_input == 'n':
                print('Tudo bem!')
        elif complaint_info[5] == 1:
            print('Complaint Done!')