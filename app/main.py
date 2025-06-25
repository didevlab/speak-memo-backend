import os
from fastapi import FastAPI, Depends, Query, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, SessionLocal
from app.seed_data import run as run_seed  # ⬅️ importa o seed

# Cria tabelas
models.Base.metadata.create_all(bind=engine)

# Se variável de ambiente ativada, roda o seed
if os.getenv("SEED_DB", "false").lower() == "true":
    print("🚀 Rodando seed inicial do banco...")
    run_seed()

app = FastAPI()

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def normalize_cron(cron: str) -> str:
    """Remove espaços extras e padroniza cron."""
    return " ".join(cron.strip().split())

@app.post("/messages/", response_model=schemas.MessageResponse)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    result = crud.create_message(db, message)
    if result is None:
        raise HTTPException(status_code=400, detail="cron_expression já existe")
    return result


@app.delete("/messages/{message_id}", status_code=204)
def delete_message(message_id: int, db: Session = Depends(get_db)):
    success = crud.delete_message(db, message_id)
    if not success:
        raise HTTPException(status_code=404, detail="Message not found")

@app.get("/messages/", response_model=list[schemas.MessageResponse])
def read_messages(
    cron_expression: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    if cron_expression:
        normalized = normalize_cron(cron_expression)
        return db.query(models.Message).filter(models.Message.cron_expression == normalized).all()
    return crud.get_messages(db)
