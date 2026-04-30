# README-database.md
## Database Overview
This database is designed to support a team management system, where users can be assigned to teams, tasks, and standups. The database consists of seven tables: Users, Teams, Tasks, Standups, Updates, Comments, and Assignments. Each table has a specific purpose and is related to others through foreign keys.

## Schema Description
The database schema is as follows:

* **Users**: stores information about users, including their username, email, password, and role.
* **Teams**: stores information about teams, including their name, description, and leader.
* **Tasks**: stores information about tasks, including their title, description, assignee, and status.
* **Standups**: stores information about standups, including their team, date, and time.
* **Updates**: stores information about updates made by users during standups, including the text and created_at timestamp.
* **Comments**: stores information about comments made on updates, including the text and created_at timestamp.
* **Assignments**: stores information about task assignments, including the task, user, and assigned_at timestamp.

The relationships between tables are as follows:

* A user can be a member of multiple teams (one-to-many).
* A team can have multiple users (one-to-many).
* A task can be assigned to one user (one-to-one).
* A standup is associated with one team (one-to-one).
* An update is associated with one standup and one user (one-to-one).
* A comment is associated with one update and one user (one-to-one).
* An assignment is associated with one task and one user (one-to-one).

## Setup Instructions
To set up the database, follow these steps:

1. Install a SQLite database management system on your local machine.
2. Create a new database and execute the provided SQL script to create the tables and indexes.
3. Update the database connection settings in your application to point to the new database.

## How to Run Migrations
To run migrations, follow these steps:

1. Make changes to the database schema by modifying the SQL script.
2. Run the updated SQL script on the database to apply the changes.
3. Update the database connection settings in your application to reflect the changes.

## How to Seed Data
To seed data, follow these steps:

1. Create a new SQL script that inserts sample data into the tables.
2. Run the script on the database to populate the tables with data.
3. Update the database connection settings in your application to reflect the changes.

## Query Examples
Here are some example queries:

* Get all users: `SELECT * FROM Users;`
* Get all tasks assigned to a user: `SELECT * FROM Tasks WHERE assignee_id = ?;`
* Get all updates made by a user: `SELECT * FROM Updates WHERE user_id = ?;`
* Get all comments on an update: `SELECT * FROM Comments WHERE update_id = ?;`

## Index Optimization Notes
The database has several indexes created to improve query performance:

* `idx_Users_username` on the `username` column of the `Users` table.
* `idx_Users_email` on the `email` column of the `Users` table.
* `idx_Teams_name` on the `name` column of the `Teams` table.
* `idx_Tasks_title` on the `title` column of the `Tasks` table.
* `idx_Tasks_team_id` on the `team_id` column of the `Tasks` table.
* `idx_Standups_team_id` on the `team_id` column of the `Standups` table.

These indexes can be adjusted or added to as needed to optimize query performance.

## Backup Strategy
To ensure data integrity and availability, a backup strategy should be implemented:

* Schedule regular backups of the database using a tool like `sqlite3` or a third-party backup solution.
* Store backups in a secure location, such as an external hard drive or cloud storage service.
* Test backups regularly to ensure they can be restored successfully in case of a failure.