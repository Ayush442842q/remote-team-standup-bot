-- Drop existing tables
DROP TABLE IF EXISTS Assignments;
DROP TABLE IF EXISTS Comments;
DROP TABLE IF EXISTS Updates;
DROP TABLE IF EXISTS Standups;
DROP TABLE IF EXISTS Tasks;
DROP TABLE IF EXISTS Teams;
DROP TABLE IF EXISTS Users;

-- Create Users table
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'user',
    CHECK (role IN ('user', 'admin'))
);

-- Create Teams table
CREATE TABLE Teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    leader_id INTEGER NOT NULL,
    FOREIGN KEY (leader_id) REFERENCES Users (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create Tasks table
CREATE TABLE Tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    assignee_id INTEGER,
    team_id INTEGER NOT NULL,
    status TEXT,
    FOREIGN KEY (assignee_id) REFERENCES Users (id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (team_id) REFERENCES Teams (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create Standups table
CREATE TABLE Standups (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    team_id INTEGER NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    FOREIGN KEY (team_id) REFERENCES Teams (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create Updates table
CREATE TABLE Updates (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    standup_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (standup_id) REFERENCES Standups (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create Comments table
CREATE TABLE Comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    update_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (update_id) REFERENCES Updates (id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create Assignments table
CREATE TABLE Assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    task_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    assigned_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES Tasks (id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create indexes
CREATE INDEX idx_Users_username ON Users (username);
CREATE INDEX idx_Users_email ON Users (email);
CREATE INDEX idx_Teams_name ON Teams (name);
CREATE INDEX idx_Tasks_title ON Tasks (title);
CREATE INDEX idx_Tasks_team_id ON Tasks (team_id);
CREATE INDEX idx_Standups_team_id ON Standups (team_id);
CREATE INDEX idx_Standups_date ON Standups (date);
CREATE INDEX idx_Updates_user_id ON Updates (user_id);
CREATE INDEX idx_Updates_standup_id ON Updates (standup_id);
CREATE INDEX idx_Comments_update_id ON Comments (update_id);
CREATE INDEX idx_Comments_user_id ON Comments (user_id);
CREATE INDEX idx_Assignments_task_id ON Assignments (task_id);
CREATE INDEX idx_Assignments_user_id ON Assignments (user_id);