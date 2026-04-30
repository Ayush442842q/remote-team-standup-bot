# Entity Overview
The following entities/tables will be used in the database schema:
* **Users**: stores information about users
* **Teams**: stores information about teams
* **Tasks**: stores information about tasks
* **Standups**: stores information about standup meetings
* **Updates**: stores information about updates shared during standup meetings
* **Comments**: stores information about comments on updates
* **Assignments**: stores information about task assignments

# Schema Tables
## Users Table
| Column Name | Data Type | Constraints |
| --- | --- | --- |
| id | INTEGER | PRIMARY KEY, NOT NULL, UNIQUE |
| username | TEXT | NOT NULL, UNIQUE |
| email | TEXT | NOT NULL, UNIQUE |
| password | TEXT | NOT NULL |
| role | TEXT | NOT NULL |

## Teams Table
| Column Name | Data Type | Constraints |
| --- | --- | --- |
| id | INTEGER | PRIMARY KEY, NOT NULL, UNIQUE |
| name | TEXT | NOT NULL, UNIQUE |
| description | TEXT |  |
| leader_id | INTEGER | FOREIGN KEY REFERENCES Users(id) |

## Tasks Table
| Column Name | Data Type | Constraints |
| --- | --- | --- |
| id | INTEGER | PRIMARY KEY, NOT NULL, UNIQUE |
| title | TEXT | NOT NULL |
| description | TEXT |  |
| assignee_id | INTEGER | FOREIGN KEY REFERENCES Users(id) |
| team_id | INTEGER | FOREIGN KEY REFERENCES Teams(id) |
| status | TEXT |  |

## Standups Table
| Column Name | Data Type | Constraints |
| --- | --- | --- |
| id | INTEGER | PRIMARY KEY, NOT NULL, UNIQUE |
| team_id | INTEGER | FOREIGN KEY REFERENCES Teams(id) |
| date | DATE | NOT NULL |
| time | TIME | NOT NULL |

## Updates Table
| Column Name | Data Type | Constraints |
| --- | --- | --- |
| id | INTEGER | PRIMARY KEY, NOT NULL, UNIQUE |
| user_id | INTEGER | FOREIGN KEY REFERENCES Users(id) |
| standup_id | INTEGER | FOREIGN KEY REFERENCES Standups(id) |
| text | TEXT | NOT NULL |
| created_at | DATETIME | NOT NULL DEFAULT CURRENT_TIMESTAMP |

## Comments Table
| Column Name | Data Type | Constraints |
| --- | --- | --- |
| id | INTEGER | PRIMARY KEY, NOT NULL, UNIQUE |
| update_id | INTEGER | FOREIGN KEY REFERENCES Updates(id) |
| user_id | INTEGER | FOREIGN KEY REFERENCES Users(id) |
| text | TEXT | NOT NULL |
| created_at | DATETIME | NOT NULL DEFAULT CURRENT_TIMESTAMP |

## Assignments Table
| Column Name | Data Type | Constraints |
| --- | --- | --- |
| id | INTEGER | PRIMARY KEY, NOT NULL, UNIQUE |
| task_id | INTEGER | FOREIGN KEY REFERENCES Tasks(id) |
| user_id | INTEGER | FOREIGN KEY REFERENCES Users(id) |
| assigned_at | DATETIME | NOT NULL DEFAULT CURRENT_TIMESTAMP |

# Indexes
The following indexes will be created:
* **Users**: index on username and email
* **Teams**: index on name
* **Tasks**: index on title and team_id
* **Standups**: index on team_id and date
* **Updates**: index on user_id and standup_id
* **Comments**: index on update_id and user_id
* **Assignments**: index on task_id and user_id

# Relationships
The following relationships exist between the tables:
* A user can be a member of many teams (one-to-many).
* A team can have many users (one-to-many).
* A team can have many tasks (one-to-many).
* A task can have one assignee (one-to-one).
* A standup can have many updates (one-to-many).
* An update can have many comments (one-to-many).
* A task can have many assignments (one-to-many).

```
+---------------+
|  Users      |
+---------------+
           |
           |
           v
+---------------+
|  Teams      |
|  (leader_id) |
+---------------+
           |
           |
           v
+---------------+
|  Tasks      |
|  (team_id,  |
|   assignee_id)|
+---------------+
           |
           |
           v
+---------------+
|  Standups   |
|  (team_id)  |
+---------------+
           |
           |
           v
+---------------+
|  Updates    |
|  (user_id,  |
|   standup_id)|
+---------------+
           |
           |
           v
+---------------+
|  Comments   |
|  (update_id,|
|   user_id)  |
+---------------+
           |
           |
           v
+---------------+
|  Assignments|
|  (task_id,  |
|   user_id)  |
+---------------+
```

# Sample Queries
The following are some sample queries that can be used:
1. **Get all teams for a user**: `SELECT * FROM Teams WHERE leader_id = ?`
2. **Get all tasks for a team**: `SELECT * FROM Tasks WHERE team_id = ?`
3. **Get all updates for a standup**: `SELECT * FROM Updates WHERE standup_id = ?`
4. **Get all comments for an update**: `SELECT * FROM Comments WHERE update_id = ?`
5. **Get all assignments for a task**: `SELECT * FROM Assignments WHERE task_id = ?`

# Migration Notes
To create the tables, the following order should be followed:
1. **Users**: create the Users table first, as it is referenced by other tables.
2. **Teams**: create the Teams table next, as it references the Users table.
3. **Tasks**: create the Tasks table after the Teams table, as it references both the Teams and Users tables.
4. **Standups**: create the Standups table after the Teams table, as it references the Teams table.
5. **Updates**: create the Updates table after the Standups and Users tables, as it references both tables.
6. **Comments**: create the Comments table after the Updates and Users tables, as it references both tables.
7. **Assignments**: create the Assignments table after the Tasks and Users tables, as it references both tables.