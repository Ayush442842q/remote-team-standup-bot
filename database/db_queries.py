import sqlite3
from sqlite3 import Error

# Database connection parameters
DB_NAME = 'remote_team_standup_bot.db'

# Create a connection to the database
def create_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except Error as e:
        print(e)
        return None

# Close the database connection
def close_connection(conn):
    if conn:
        conn.close()

# Users table queries
def create_user(conn, username, email, password, role='user'):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO Users (username, email, password, role)
                   VALUES (?, ?, ?, ?)"""
        cursor.execute(query, (username, email, password, role))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None

def get_user(conn, user_id):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Users
                   WHERE id = ?"""
        cursor.execute(query, (user_id,))
        return cursor.fetchone()
    except Error as e:
        print(e)
        return None

def update_user(conn, user_id, username, email, password, role):
    try:
        cursor = conn.cursor()
        query = """UPDATE Users
                   SET username = ?, email = ?, password = ?, role = ?
                   WHERE id = ?"""
        cursor.execute(query, (username, email, password, role, user_id))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def delete_user(conn, user_id):
    try:
        cursor = conn.cursor()
        query = """DELETE FROM Users
                   WHERE id = ?"""
        cursor.execute(query, (user_id,))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def get_users(conn):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Users"""
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

# Teams table queries
def create_team(conn, name, description, leader_id):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO Teams (name, description, leader_id)
                   VALUES (?, ?, ?)"""
        cursor.execute(query, (name, description, leader_id))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None

def get_team(conn, team_id):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Teams
                   WHERE id = ?"""
        cursor.execute(query, (team_id,))
        return cursor.fetchone()
    except Error as e:
        print(e)
        return None

def update_team(conn, team_id, name, description, leader_id):
    try:
        cursor = conn.cursor()
        query = """UPDATE Teams
                   SET name = ?, description = ?, leader_id = ?
                   WHERE id = ?"""
        cursor.execute(query, (name, description, leader_id, team_id))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def delete_team(conn, team_id):
    try:
        cursor = conn.cursor()
        query = """DELETE FROM Teams
                   WHERE id = ?"""
        cursor.execute(query, (team_id,))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def get_teams(conn):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Teams"""
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

# Tasks table queries
def create_task(conn, title, description, assignee_id, team_id):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO Tasks (title, description, assignee_id, team_id)
                   VALUES (?, ?, ?, ?)"""
        cursor.execute(query, (title, description, assignee_id, team_id))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None

def get_task(conn, task_id):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Tasks
                   WHERE id = ?"""
        cursor.execute(query, (task_id,))
        return cursor.fetchone()
    except Error as e:
        print(e)
        return None

def update_task(conn, task_id, title, description, assignee_id, team_id):
    try:
        cursor = conn.cursor()
        query = """UPDATE Tasks
                   SET title = ?, description = ?, assignee_id = ?, team_id = ?
                   WHERE id = ?"""
        cursor.execute(query, (title, description, assignee_id, team_id, task_id))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def delete_task(conn, task_id):
    try:
        cursor = conn.cursor()
        query = """DELETE FROM Tasks
                   WHERE id = ?"""
        cursor.execute(query, (task_id,))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def get_tasks(conn):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Tasks"""
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

# Standups table queries
def create_standup(conn, team_id, date, time):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO Standups (team_id, date, time)
                   VALUES (?, ?, ?)"""
        cursor.execute(query, (team_id, date, time))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None

def get_standup(conn, standup_id):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Standups
                   WHERE id = ?"""
        cursor.execute(query, (standup_id,))
        return cursor.fetchone()
    except Error as e:
        print(e)
        return None

def update_standup(conn, standup_id, team_id, date, time):
    try:
        cursor = conn.cursor()
        query = """UPDATE Standups
                   SET team_id = ?, date = ?, time = ?
                   WHERE id = ?"""
        cursor.execute(query, (team_id, date, time, standup_id))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def delete_standup(conn, standup_id):
    try:
        cursor = conn.cursor()
        query = """DELETE FROM Standups
                   WHERE id = ?"""
        cursor.execute(query, (standup_id,))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def get_standups(conn):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Standups"""
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

# Updates table queries
def create_update(conn, user_id, standup_id, text):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO Updates (user_id, standup_id, text)
                   VALUES (?, ?, ?)"""
        cursor.execute(query, (user_id, standup_id, text))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None

def get_update(conn, update_id):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Updates
                   WHERE id = ?"""
        cursor.execute(query, (update_id,))
        return cursor.fetchone()
    except Error as e:
        print(e)
        return None

def update_update(conn, update_id, user_id, standup_id, text):
    try:
        cursor = conn.cursor()
        query = """UPDATE Updates
                   SET user_id = ?, standup_id = ?, text = ?
                   WHERE id = ?"""
        cursor.execute(query, (user_id, standup_id, text, update_id))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def delete_update(conn, update_id):
    try:
        cursor = conn.cursor()
        query = """DELETE FROM Updates
                   WHERE id = ?"""
        cursor.execute(query, (update_id,))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def get_updates(conn):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Updates"""
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

# Comments table queries
def create_comment(conn, update_id, user_id, text):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO Comments (update_id, user_id, text)
                   VALUES (?, ?, ?)"""
        cursor.execute(query, (update_id, user_id, text))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None

def get_comment(conn, comment_id):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Comments
                   WHERE id = ?"""
        cursor.execute(query, (comment_id,))
        return cursor.fetchone()
    except Error as e:
        print(e)
        return None

def update_comment(conn, comment_id, update_id, user_id, text):
    try:
        cursor = conn.cursor()
        query = """UPDATE Comments
                   SET update_id = ?, user_id = ?, text = ?
                   WHERE id = ?"""
        cursor.execute(query, (update_id, user_id, text, comment_id))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def delete_comment(conn, comment_id):
    try:
        cursor = conn.cursor()
        query = """DELETE FROM Comments
                   WHERE id = ?"""
        cursor.execute(query, (comment_id,))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def get_comments(conn):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Comments"""
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

# Assignments table queries
def create_assignment(conn, task_id, user_id):
    try:
        cursor = conn.cursor()
        query = """INSERT INTO Assignments (task_id, user_id)
                   VALUES (?, ?)"""
        cursor.execute(query, (task_id, user_id))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None

def get_assignment(conn, assignment_id):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Assignments
                   WHERE id = ?"""
        cursor.execute(query, (assignment_id,))
        return cursor.fetchone()
    except Error as e:
        print(e)
        return None

def update_assignment(conn, assignment_id, task_id, user_id):
    try:
        cursor = conn.cursor()
        query = """UPDATE Assignments
                   SET task_id = ?, user_id = ?
                   WHERE id = ?"""
        cursor.execute(query, (task_id, user_id, assignment_id))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def delete_assignment(conn, assignment_id):
    try:
        cursor = conn.cursor()
        query = """DELETE FROM Assignments
                   WHERE id = ?"""
        cursor.execute(query, (assignment_id,))
        conn.commit()
        return cursor.rowcount
    except Error as e:
        print(e)
        return None

def get_assignments(conn):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Assignments"""
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

# Join queries
def get_team_tasks(conn, team_id):
    try:
        cursor = conn.cursor()
        query = """SELECT T.* FROM Tasks T
                   JOIN Teams TM ON T.team_id = TM.id
                   WHERE TM.id = ?"""
        cursor.execute(query, (team_id,))
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

def get_user_tasks(conn, user_id):
    try:
        cursor = conn.cursor()
        query = """SELECT T.* FROM Tasks T
                   JOIN Assignments A ON T.id = A.task_id
                   WHERE A.user_id = ?"""
        cursor.execute(query, (user_id,))
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

def get_standup_updates(conn, standup_id):
    try:
        cursor = conn.cursor()
        query = """SELECT U.* FROM Updates U
                   JOIN Standups S ON U.standup_id = S.id
                   WHERE S.id = ?"""
        cursor.execute(query, (standup_id,))
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

def get_update_comments(conn, update_id):
    try:
        cursor = conn.cursor()
        query = """SELECT C.* FROM Comments C
                   JOIN Updates U ON C.update_id = U.id
                   WHERE U.id = ?"""
        cursor.execute(query, (update_id,))
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

# Search/filter queries
def search_users(conn, query):
    try:
        cursor = conn.cursor()
        query_sql = """SELECT * FROM Users
                       WHERE username LIKE ? OR email LIKE ?"""
        cursor.execute(query_sql, ('%' + query + '%', '%' + query + '%'))
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

def search_tasks(conn, query):
    try:
        cursor = conn.cursor()
        query_sql = """SELECT * FROM Tasks
                       WHERE title LIKE ? OR description LIKE ?"""
        cursor.execute(query_sql, ('%' + query + '%', '%' + query + '%'))
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

def search_updates(conn, query):
    try:
        cursor = conn.cursor()
        query_sql = """SELECT * FROM Updates
                       WHERE text LIKE ?"""
        cursor.execute(query_sql, ('%' + query + '%',))
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

# Pagination queries
def get_users_paginated(conn, page, page_size):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Users
                   ORDER BY id
                   LIMIT ? OFFSET ?"""
        cursor.execute(query, (page_size, (page - 1) * page_size))
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

def get_tasks_paginated(conn, page, page_size):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Tasks
                   ORDER BY id
                   LIMIT ? OFFSET ?"""
        cursor.execute(query, (page_size, (page - 1) * page_size))
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None

def get_updates_paginated(conn, page, page_size):
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM Updates
                   ORDER BY id
                   LIMIT ? OFFSET ?"""
        cursor.execute(query, (page_size, (page - 1) * page_size))
        return cursor.fetchall()
    except Error as e:
        print(e)
        return None
import db_queries

# Create a connection to the database
conn = db_queries.create_connection()

# Create a new user
user_id = db_queries.create_user(conn, 'john_doe', 'johndoe@example.com', 'password123')

# Get the user's details
user = db_queries.get_user(conn, user_id)

# Update the user's details
db_queries.update_user(conn, user_id, 'jane_doe', 'janedoe@example.com', 'newpassword')

# Delete the user
db_queries.delete_user(conn, user_id)

# Close the database connection
db_queries.close_connection(conn)