import sqlite3
from datetime import datetime, timedelta

# Connect to the database
def connect_to_db(db_name):
    conn = sqlite3.connect(db_name)
    return conn

# Create seed data
def create_seed_data(conn):
    cursor = conn.cursor()

    # Users
    users = [
        ('john_doe', 'john.doe@example.com', 'password123', 'admin'),
        ('jane_doe', 'jane.doe@example.com', 'password123', 'user'),
        ('bob_smith', 'bob.smith@example.com', 'password123', 'user'),
        ('alice_johnson', 'alice.johnson@example.com', 'password123', 'user'),
        ('mike_williams', 'mike.williams@example.com', 'password123', 'user'),
    ]
    cursor.executemany('INSERT INTO Users (username, email, password, role) VALUES (?, ?, ?, ?)', users)

    # Get user ids
    cursor.execute('SELECT id FROM Users')
    user_ids = [row[0] for row in cursor.fetchall()]

    # Teams
    teams = [
        ('Development Team', 'This is the development team', user_ids[0]),
        ('Marketing Team', 'This is the marketing team', user_ids[1]),
        ('Sales Team', 'This is the sales team', user_ids[2]),
    ]
    cursor.executemany('INSERT INTO Teams (name, description, leader_id) VALUES (?, ?, ?)', teams)

    # Get team ids
    cursor.execute('SELECT id FROM Teams')
    team_ids = [row[0] for row in cursor.fetchall()]

    # Tasks
    tasks = [
        ('Task 1', 'This is task 1', None, team_ids[0], 'in_progress'),
        ('Task 2', 'This is task 2', None, team_ids[0], 'done'),
        ('Task 3', 'This is task 3', None, team_ids[1], 'in_progress'),
        ('Task 4', 'This is task 4', None, team_ids[1], 'done'),
        ('Task 5', 'This is task 5', None, team_ids[2], 'in_progress'),
    ]
    cursor.executemany('INSERT INTO Tasks (title, description, assignee_id, team_id, status) VALUES (?, ?, ?, ?, ?)', tasks)

    # Get task ids
    cursor.execute('SELECT id FROM Tasks')
    task_ids = [row[0] for row in cursor.fetchall()]

    # Assignments
    assignments = [
        (task_ids[0], user_ids[1]),
        (task_ids[1], user_ids[2]),
        (task_ids[2], user_ids[3]),
        (task_ids[3], user_ids[4]),
        (task_ids[4], user_ids[0]),
    ]
    cursor.executemany('INSERT INTO Assignments (task_id, user_id) VALUES (?, ?)', assignments)

    # Standups
    standups = [
        (team_ids[0], '2022-01-01', '10:00:00'),
        (team_ids[0], '2022-01-02', '10:00:00'),
        (team_ids[1], '2022-01-03', '10:00:00'),
        (team_ids[1], '2022-01-04', '10:00:00'),
        (team_ids[2], '2022-01-05', '10:00:00'),
    ]
    cursor.executemany('INSERT INTO Standups (team_id, date, time) VALUES (?, ?, ?)', standups)

    # Get standup ids
    cursor.execute('SELECT id FROM Standups')
    standup_ids = [row[0] for row in cursor.fetchall()]

    # Updates
    updates = [
        (user_ids[0], standup_ids[0], 'This is update 1'),
        (user_ids[1], standup_ids[0], 'This is update 2'),
        (user_ids[2], standup_ids[1], 'This is update 3'),
        (user_ids[3], standup_ids[2], 'This is update 4'),
        (user_ids[4], standup_ids[3], 'This is update 5'),
    ]
    cursor.executemany('INSERT INTO Updates (user_id, standup_id, text) VALUES (?, ?, ?)', updates)

    # Get update ids
    cursor.execute('SELECT id FROM Updates')
    update_ids = [row[0] for row in cursor.fetchall()]

    # Comments
    comments = [
        (update_ids[0], user_ids[1], 'This is comment 1'),
        (update_ids[1], user_ids[2], 'This is comment 2'),
        (update_ids[2], user_ids[3], 'This is comment 3'),
        (update_ids[3], user_ids[4], 'This is comment 4'),
        (update_ids[4], user_ids[0], 'This is comment 5'),
    ]
    cursor.executemany('INSERT INTO Comments (update_id, user_id, text) VALUES (?, ?, ?)', comments)

    conn.commit()

# Main function
def main():
    db_name = 'database.db'
    conn = connect_to_db(db_name)
    create_seed_data(conn)
    conn.close()

if __name__ == '__main__':
    main()