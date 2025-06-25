from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import models, schemas

def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(**message.dict())
    db.add(db_message)
    try:
        db.commit()
        db.refresh(db_message)
        return db_message
    except IntegrityError:
        db.rollback()
        return None  # Retorna None se duplicado

def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Message).offset(skip).limit(limit).all()

def delete_message(db: Session, message_id: int):
    message = db.query(models.Message).filter(models.Message.id == message_id).first()
    if message:
        db.delete(message)
        db.commit()
        return True
    return False