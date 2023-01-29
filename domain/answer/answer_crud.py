from datetime import datetime
from sqlalchemy.orm import Session
from domain.answer.answer_schema import AnswerCreate
from models import Question, Answer


def create_answer(db: Session, question: Question, answer_create: AnswerCreate):
    print(1)
    db_answer = Answer(question=question, content=answer_create.content)
    print(2)
    db.add(db_answer)
    print(3)
    db.commit()

