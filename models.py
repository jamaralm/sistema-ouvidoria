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
    cursor.execute(queries['select_user'], (user_id,))
    user = cursor.fetchall()

    if user:
        data = (name, description, datetime.now(),user_id)

        cursor.execute(queries['add_complaint'], data)
        connection.commit()

        print('\nRECLAMACAO ADICIONADA COM SUCESSO!')
    else:
        print('\nERROR: USUARIO NAO ENCONTRADO!')

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

    for complaint in complaints:
        print(f'{complaint[0]} | {complaint[1]} | {complaint[2]} | {complaint[3]} | {complaint[4]} ')