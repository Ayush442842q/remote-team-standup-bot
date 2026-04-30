from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
import sqlite3
import jwt
import logging
from logging.handlers import RotatingFileHandler
import os

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Set up log file
log_file = 'app.log'
log_handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=1)
logger.addHandler(log_handler)

# Set up environment variables
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASE_URL = os.environ.get('DATABASE_URL')

# Set up database connection
conn = sqlite3.connect(DATABASE_URL)
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        team_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        leader_id INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        assignee_id INTEGER NOT NULL,
        team_id INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS standup_meetings (
        standup_meeting_id INTEGER PRIMARY KEY,
        team_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

# Set up FastAPI app
app = FastAPI()

# Set up OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# Define models
class Team(BaseModel):
    team_id: int
    name: str
    description: str
    leader_id: int

class Task(BaseModel):
    task_id: int
    title: str
    description: str
    assignee_id: int
    team_id: int

class StandupMeeting(BaseModel):
    standup_meeting_id: int
    team_id: int
    date: str
    time: str

class SentimentAnalysis(BaseModel):
    text: str

# Define routes
@app.post('/api/v1/teams', response_model=Team)
async def create_team(team: Team, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Create team
    cursor.execute('''
        INSERT INTO teams (name, description, leader_id)
        VALUES (?, ?, ?)
    ''', (team.name, team.description, team.leader_id))
    conn.commit()
    team_id = cursor.lastrowid
    return Team(team_id=team_id, name=team.name, description=team.description, leader_id=team.leader_id)

@app.get('/api/v1/teams/{team_id}', response_model=Team)
async def get_team(team_id: int, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Get team
    cursor.execute('''
        SELECT * FROM teams WHERE team_id = ?
    ''', (team_id,))
    team = cursor.fetchone()
    if team is None:
        raise HTTPException(status_code=404, detail='Team not found')
    return Team(team_id=team[0], name=team[1], description=team[2], leader_id=team[3])

@app.put('/api/v1/teams/{team_id}', response_model=Team)
async def update_team(team_id: int, team: Team, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Update team
    cursor.execute('''
        UPDATE teams SET name = ?, description = ?, leader_id = ?
        WHERE team_id = ?
    ''', (team.name, team.description, team.leader_id, team_id))
    conn.commit()
    return Team(team_id=team_id, name=team.name, description=team.description, leader_id=team.leader_id)

@app.delete('/api/v1/teams/{team_id}')
async def delete_team(team_id: int, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Delete team
    cursor.execute('''
        DELETE FROM teams WHERE team_id = ?
    ''', (team_id,))
    conn.commit()
    return {'message': 'Team deleted'}

@app.post('/api/v1/tasks', response_model=Task)
async def create_task(task: Task, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Create task
    cursor.execute('''
        INSERT INTO tasks (title, description, assignee_id, team_id)
        VALUES (?, ?, ?, ?)
    ''', (task.title, task.description, task.assignee_id, task.team_id))
    conn.commit()
    task_id = cursor.lastrowid
    return Task(task_id=task_id, title=task.title, description=task.description, assignee_id=task.assignee_id, team_id=task.team_id)

@app.get('/api/v1/tasks/{task_id}', response_model=Task)
async def get_task(task_id: int, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Get task
    cursor.execute('''
        SELECT * FROM tasks WHERE task_id = ?
    ''', (task_id,))
    task = cursor.fetchone()
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    return Task(task_id=task[0], title=task[1], description=task[2], assignee_id=task[3], team_id=task[4])

@app.put('/api/v1/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, task: Task, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Update task
    cursor.execute('''
        UPDATE tasks SET title = ?, description = ?, assignee_id = ?, team_id = ?
        WHERE task_id = ?
    ''', (task.title, task.description, task.assignee_id, task.team_id, task_id))
    conn.commit()
    return Task(task_id=task_id, title=task.title, description=task.description, assignee_id=task.assignee_id, team_id=task.team_id)

@app.delete('/api/v1/tasks/{task_id}')
async def delete_task(task_id: int, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Delete task
    cursor.execute('''
        DELETE FROM tasks WHERE task_id = ?
    ''', (task_id,))
    conn.commit()
    return {'message': 'Task deleted'}

@app.post('/api/v1/standup-meetings', response_model=StandupMeeting)
async def create_standup_meeting(standup_meeting: StandupMeeting, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Create standup meeting
    cursor.execute('''
        INSERT INTO standup_meetings (team_id, date, time)
        VALUES (?, ?, ?)
    ''', (standup_meeting.team_id, standup_meeting.date, standup_meeting.time))
    conn.commit()
    standup_meeting_id = cursor.lastrowid
    return StandupMeeting(standup_meeting_id=standup_meeting_id, team_id=standup_meeting.team_id, date=standup_meeting.date, time=standup_meeting.time)

@app.get('/api/v1/standup-meetings/{standup_meeting_id}', response_model=StandupMeeting)
async def get_standup_meeting(standup_meeting_id: int, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Get standup meeting
    cursor.execute('''
        SELECT * FROM standup_meetings WHERE standup_meeting_id = ?
    ''', (standup_meeting_id,))
    standup_meeting = cursor.fetchone()
    if standup_meeting is None:
        raise HTTPException(status_code=404, detail='Standup meeting not found')
    return StandupMeeting(standup_meeting_id=standup_meeting[0], team_id=standup_meeting[1], date=standup_meeting[2], time=standup_meeting[3])

@app.put('/api/v1/standup-meetings/{standup_meeting_id}', response_model=StandupMeeting)
async def update_standup_meeting(standup_meeting_id: int, standup_meeting: StandupMeeting, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Update standup meeting
    cursor.execute('''
        UPDATE standup_meetings SET team_id = ?, date = ?, time = ?
        WHERE standup_meeting_id = ?
    ''', (standup_meeting.team_id, standup_meeting.date, standup_meeting.time, standup_meeting_id))
    conn.commit()
    return StandupMeeting(standup_meeting_id=standup_meeting_id, team_id=standup_meeting.team_id, date=standup_meeting.date, time=standup_meeting.time)

@app.delete('/api/v1/standup-meetings/{standup_meeting_id}')
async def delete_standup_meeting(standup_meeting_id: int, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Delete standup meeting
    cursor.execute('''
        DELETE FROM standup_meetings WHERE standup_meeting_id = ?
    ''', (standup_meeting_id,))
    conn.commit()
    return {'message': 'Standup meeting deleted'}

@app.post('/api/v1/sentiment-analysis', response_model=SentimentAnalysis)
async def analyze_sentiment(sentiment_analysis: SentimentAnalysis, token: str = Depends(oauth2_scheme)):
    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

    # Analyze sentiment
    # NOTE: This is a placeholder for a real sentiment analysis API
    sentiment = 'positive'
    return SentimentAnalysis(text=sentiment_analysis.text, sentiment=sentiment)

# Set up CORS
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# Set up error handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {'error': {'code': exc.status_code, 'message': exc.detail}}

# Set up login route
@app.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Validate credentials
    if form_data.username != 'admin' or form_data.password != 'password':
        raise HTTPException(status_code=401, detail='Invalid credentials')

    # Generate token
    payload = {'username': form_data.username}
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return {'access_token': token, 'token_type': 'bearer'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
uvicorn app:app --host 0.0.0.0 --port 8000