from datetime import datetime
from sqlalchemy.orm import Session
from domain.answer.answer_schema import AnswerCreate
from models import Question, Answer


def create_answer(db: Session, question: Question, answer_create: AnswerCreate):
    print("db", db)
    print("question_id", question)
    print("question", answer_create.content)
    db_answer = Answer(question=question, content=answer_create.content)
    print("FINAL", db_answer)
    db.add(db_answer)
    db.commit()

