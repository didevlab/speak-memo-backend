from app.database import SessionLocal
from app.models import Message

seed_data = [
    {
        "text": "Did you have lunch?",
        "pronunciation": "Díd iú rév lântch?",
        "meaning": "Você almoçou?",
        "reply_text": "Yes, I had lunch.",
        "reply_pronunciation": "Iés, ai réd lântch.",
        "reply_meaning": "Sim, eu almocei.",
        "type": "question",
        "context": "afternoon",
        "routine": "daily-routine",
        "cron_expression": "0 14 * * *"
    },
    {
        "text": "Do you like coffee?",
        "pronunciation": "Dú iú láik cófi?",
        "meaning": "Você gosta de café?",
        "reply_text": "Yes, I love coffee.",
        "reply_pronunciation": "Iés, ai lâv cófi.",
        "reply_meaning": "Sim, eu amo café.",
        "type": "question",
        "context": "afternoon",
        "routine": "daily-routine",
        "cron_expression": "30 14 * * *"
    },
    {
        "text": "Do you speak English?",
        "pronunciation": "Dú iú spík ínglish?",
        "meaning": "Você fala inglês?",
        "reply_text": "I'm learning English now.",
        "reply_pronunciation": "Aim lârnin ínglish náu.",
        "reply_meaning": "Estou aprendendo inglês agora.",
        "type": "question",
        "context": "afternoon",
        "routine": "daily-routine",
        "cron_expression": "0 15 * * *"
    },
    {
        "text": "What's your native language?",
        "pronunciation": "Uóts iór nêitiv lénguêtch?",
        "meaning": "Qual é sua língua nativa?",
        "reply_text": "My native language is Portuguese.",
        "reply_pronunciation": "Mai nêitiv lénguêtch is Pórtchuguiz",
        "reply_meaning": "Minha língua nativa é o português.",
        "type": "question",
        "context": "afternoon",
        "routine": "daily-routine",
        "cron_expression": "30 15 * * *"
    },
    {
        "text": "What's your name?",
        "pronunciation": "Uóts iór nêim?",
        "meaning": "Qual é o seu nome?",
        "reply_text": "My name is Diego.",
        "reply_pronunciation": "Mai nêim is Diêigo",
        "reply_meaning": "Meu nome é Diego.",
        "type": "question",
        "context": "afternoon",
        "routine": "daily-routine",
        "cron_expression": "0 16 * * *"
    },
    {
        "text": "How old are you?",
        "pronunciation": "Ráu ould ar iú?",
        "meaning": "Quantos anos você tem?",
        "reply_text": "I'm 34 years old.",
        "reply_pronunciation": "Aim thârtí-fór íers ould",
        "reply_meaning": "Eu tenho 34 anos.",
        "type": "question",
        "context": "afternoon",
        "routine": "daily-routine",
        "cron_expression": "30 16 * * *"
    },
    {
        "text": "What do you like to do?",
        "pronunciation": "Uót dú iú láik tchu dú?",
        "meaning": "O que você gosta de fazer?",
        "reply_text": "I like to snowboard.",
        "reply_pronunciation": "Ai láik tchu snôubórd",
        "reply_meaning": "Eu gosto de praticar snowboard.",
        "type": "question",
        "context": "afternoon",
        "routine": "daily-routine",
        "cron_expression": "0 17 * * *"
    },
    {
        "text": "Where are you from?",
        "pronunciation": "Uér ar iú fróm?",
        "meaning": "De onde você é?",
        "reply_text": "I'm from Brazil.",
        "reply_pronunciation": "Aim fróm Brazil",
        "reply_meaning": "Eu sou do Brasil.",
        "type": "question",
        "context": "afternoon",
        "routine": "daily-routine",
        "cron_expression": "30 17 * * *"
    },
    {
        "text": "Are you done for today?",
        "pronunciation": "Ar iú dãn fór tchudêi?",
        "meaning": "Você terminou por hoje?",
        "reply_text": "Yes, I finished work.",
        "reply_pronunciation": "Iés, ai fínisht uârk",
        "reply_meaning": "Sim, terminei o trabalho.",
        "type": "question",
        "context": "afternoon",
        "routine": "daily-routine",
        "cron_expression": "0 18 * * *"
    },
    {
        "text": "See you tomorrow!",
        "pronunciation": "Sii iú tumórrou!",
        "meaning": "Até amanhã!",
        "reply_text": "See you!",
        "reply_pronunciation": "Sii iú!",
        "reply_meaning": "Até mais!",
        "type": "greeting",
        "context": "afternoon",
        "routine": "daily-routine",
        "cron_expression": "20 18 * * *"
    }
]

def run():
    db = SessionLocal()
    try:
        for item in seed_data:
            exists = db.query(Message).filter(Message.cron_expression == item["cron_expression"]).first()
            if not exists:
                speak_memo = Message(**item)
                db.add(speak_memo)
        db.commit()
        print("✅ Seed executado com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao rodar seed: {e}")
        db.rollback()
    finally:
        db.close()
