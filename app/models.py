from sqlalchemy import Column, Integer, String, Enum, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class MessageType(str, enum.Enum):
    greeting = "greeting"
    question = "question"
    command = "command"

class MessageContext(str, enum.Enum):
    morning = "morning"
    afternoon = "afternoon"
    evening = "evening"

class MessageRoutine(str, enum.Enum):
    daily = "daily-routine"
    weekly = "weekly-routine"

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    pronunciation = Column(String, nullable=False)
    meaning = Column(String, nullable=False)
    reply_text = Column(String)
    reply_pronunciation = Column(String)
    reply_meaning = Column(String)
    type = Column(Enum(MessageType), nullable=False)
    context = Column(Enum(MessageContext), nullable=False)
    routine = Column(Enum(MessageRoutine), nullable=False)
    cron_expression = Column(String, nullable=False, unique=True) # <- novo campo!
