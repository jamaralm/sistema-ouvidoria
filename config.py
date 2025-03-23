DB_CONFIG = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "Ouvidoria"
}

queries = {
    'list_complaints': 'SELECT * FROM Complaints',
    'list_users': 'SELECT * FROM Users',
    'add_complaint': 'INSERT INTO Complaints (complaint_name,complaint_description, date_time, user_id) VALUES (%s,%s,%s,%s)',
    'add_anonimous_complaint': 'INSERT INTO Complaints (complaint_name, complaint_description, date_time)  VALUES (%s,%s,%s)',
    'add_user': 'INSERT INTO Users (username, email, password) VALUES (%s,%s,%s)',
    'delete_complaint': 'DELETE FROM Complaints WHERE complaint_id = %s',
    'delete_user': 'DELETE FROM Users WHERE user_id = %s',
    'select_user': 'SELECT * FROM Users WHERE user_id = %s',
    'select_complaint_from_user': 'SELECT * FROM Complaints WHERE user_id = %s',
    'select_complaint': 'SELECT * FROM Complaints WHERE complaint_id = %s',
    'mark_complaint_as_done': 'UPDATE Complaints SET is_done = TRUE WHERE complaint_id = %s'
}
