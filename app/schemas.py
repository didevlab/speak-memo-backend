from pydantic import BaseModel
from enum import Enum

class MessageType(str, Enum):
    greeting = "greeting"
    question = "question"
    command = "command"

class MessageContext(str, Enum):
    morning = "morning"
    afternoon = "afternoon"
    evening = "evening"

class MessageRoutine(str, Enum):
    daily = "daily-routine"
    weekly = "weekly-routine"

class MessageCreate(BaseModel):
    text: str
    pronunciation: str
    meaning: str
    reply_text: str
    reply_pronunciation: str
    reply_meaning: str
    type: MessageType
    context: MessageContext
    routine: MessageRoutine
    cron_expression: str  # Ex: "30 9 * * 1,3,5"

class MessageResponse(MessageCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
