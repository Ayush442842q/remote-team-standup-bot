# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from typing import Dict

# Create a base class for declarative class definitions
Base = declarative_base()

# Association table for many-to-many relationships
team_user = Table(
    'team_user', Base.metadata,
    Column('team_id', Integer, ForeignKey('teams.team_id')),
    Column('user_id', Integer, ForeignKey('users.user_id'))
)

class User(Base):
    """User model."""
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    teams = relationship("Team", secondary=team_user, back_populates="users")
    tasks = relationship("Task", back_populates="assignee")

    def to_dict(self) -> Dict:
        """Return a dictionary representation of the user."""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email
        }

class Team(Base):
    """Team model."""
    __tablename__ = 'teams'

    team_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    leader_id = Column(Integer, ForeignKey('users.user_id'))

    users = relationship("User", secondary=team_user, back_populates="teams")
    tasks = relationship("Task", back_populates="team")
    standup_meetings = relationship("StandupMeeting", back_populates="team")

    def to_dict(self) -> Dict:
        """Return a dictionary representation of the team."""
        return {
            "team_id": self.team_id,
            "name": self.name,
            "description": self.description,
            "leader_id": self.leader_id
        }

class Task(Base):
    """Task model."""
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    assignee_id = Column(Integer, ForeignKey('users.user_id'))
    team_id = Column(Integer, ForeignKey('teams.team_id'))

    assignee = relationship("User", back_populates="tasks")
    team = relationship("Team", back_populates="tasks")

    def to_dict(self) -> Dict:
        """Return a dictionary representation of the task."""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "assignee_id": self.assignee_id,
            "team_id": self.team_id
        }

class StandupMeeting(Base):
    """Standup meeting model."""
    __tablename__ = 'standup_meetings'

    standup_meeting_id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.team_id'))
    date = Column(DateTime)
    time = Column(DateTime)

    team = relationship("Team", back_populates="standup_meetings")

    def to_dict(self) -> Dict:
        """Return a dictionary representation of the standup meeting."""
        return {
            "standup_meeting_id": self.standup_meeting_id,
            "team_id": self.team_id,
            "date": self.date,
            "time": self.time
        }

class SentimentAnalysis(Base):
    """Sentiment analysis model."""
    __tablename__ = 'sentiment_analysis'

    sentiment_analysis_id = Column(Integer, primary_key=True)
    text = Column(String)
    sentiment = Column(String)

    def to_dict(self) -> Dict:
        """Return a dictionary representation of the sentiment analysis."""
        return {
            "sentiment_analysis_id": self.sentiment_analysis_id,
            "text": self.text,
            "sentiment": self.sentiment
        }

# Create an engine that stores data in a local directory's SQLite file
engine = create_engine('sqlite:///database/data.db')

# Create all tables in the engine
Base.metadata.create_all(engine)