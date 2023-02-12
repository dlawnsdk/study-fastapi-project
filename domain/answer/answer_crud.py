from datetime import datetime
from sqlalchemy.orm import Session
from domain.answer.answer_schema import AnswerCreate
from models import Question, Answer, User


def create_answer(db: Session, question: Question, answer_create: AnswerCreate, user: User):
    db_answer = Answer(question=question, content=answer_create.content, create_date=datetime.now(), user=user)
    db.add(db_answer)
    db.commit()


def get_answer(db: Session, answer_id: int):
    answer = db.query(Answer).get(answer_id)
    return answer


def vote_answer(db: Session, db_answer: Answer, db_user: User):
    db_answer.voter.append(db_user)
    db.commit()