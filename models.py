from db import connection, cursor
from config import queries
from datetime import datetime

def execute_query(query, data=None, fetch=False, fetchone=False):
    """Executa uma query no banco de dados e pode retornar resultados."""
    cursor.execute(query, data) if data else cursor.execute(query)
    if fetchone:
        return cursor.fetchone()
    if fetch:
        return cursor.fetchall()
    connection.commit()

def add_user(name, email, password):
    execute_query(queries['add_user'], (name, email, password))
    print('\nUSUÁRIO ADICIONADO COM SUCESSO!')

def add_complaint(name, description, user_id=None):
    if user_id and execute_query(queries['select_user'], (user_id,), fetchone=True):
        execute_query(queries['add_complaint'], (name, description, datetime.now(), user_id))
    else:
        execute_query(queries['add_anonimous_complaint'], (name, description, datetime.now()))
    print('\nRECLAMAÇÃO ADICIONADA COM SUCESSO!')

def remove_user(user_id):
    if execute_query(queries['select_user'], (user_id,), fetchone=True):
        execute_query(queries['delete_user'], (user_id,))
        print('\nUSUÁRIO REMOVIDO COM SUCESSO!')
    else:
        print('\nERRO: Usuário não encontrado!')

def remove_complaint(complaint_id):
    execute_query(queries['delete_complaint'], (complaint_id,))
    print('\nRECLAMAÇÃO REMOVIDA COM SUCESSO!')

def list_complaints():
    complaints = execute_query(queries['list_complaints'], fetch=True)
    print("\n--- LISTA DE RECLAMAÇÕES ---")
    print(f"{'ID':<5} | {'Título':<30} | {'Descrição':<50} | {'Data':<12} | {'Usuário':<15} | {'Status':<15}")
    print("-" * 140)
    
    for complaint in complaints:
        complaint_date = complaint[3].strftime('%d/%m/%Y') if complaint[3] else "N/A"
        user_info = execute_query(queries['select_user'], (complaint[4],), fetchone=True)
        user_name = user_info[1] if user_info else "Anônimo"
        status = 'Resolvida' if complaint[5] else 'Não Resolvida'
        print(f"{complaint[0]:<5} | {complaint[1]:<30} | {complaint[2]:<50} | {complaint_date:<12} | {user_name:<15} | {status:<15}")
    
    print("-" * 140)

def list_user_complaints(user_id):
    user_info = execute_query(queries['select_user'], (user_id,), fetchone=True)
    if not user_info:
        print('\nERRO: Usuário não encontrado!')
        return
    
    complaints = execute_query(queries['select_complaint_from_user'], (user_id,), fetch=True)
    print(f'\nReclamações de {user_info[1]}:')
    for complaint in complaints:
        print(f'{complaint[0]}. {complaint[1]}')

def mark_as_done(complaint_id):
    complaint_info = execute_query(queries['select_complaint'], (complaint_id,), fetchone=True)
    if not complaint_info:
        print('\nERRO: Reclamação não encontrada!')
        return
    
    if complaint_info[5]:
        print('Reclamação já foi resolvida!')
        return
    
    user_input = input(f'Você deseja marcar a reclamação "{complaint_info[1]}" como concluída? (s/n)\n')
    if user_input.lower() == 's':
        execute_query(queries['mark_complaint_as_done'], (complaint_id,))
        print('Status da reclamação atualizado!')
    else:
        print('Operação cancelada!')
