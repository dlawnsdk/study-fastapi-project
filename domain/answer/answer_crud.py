from datetime import datetime
from sqlalchemy.orm import Session
from domain.answer.answer_schema import AnswerCreate,AnswerUpdate
from models import Question, Answer, User


def create_answer(db: Session, question: Question, answer_create: AnswerCreate, user: User):
    db_answer = Answer(question=question, content=answer_create.content, create_date=datetime.now(), user=user)
    db.add(db_answer)
    db.commit()


def get_answer(db: Session, answer_id: int):
    answer = db.query(Answer).get(answer_id)
    return answer


def update_answer(db: Session, db_answer: Answer, answer_updaete: AnswerUpdate):
    db_answer.content = answer_updaete.content
    db_answer.modify_date = datetime.now()
    db.add(db_answer)
    db.commit()


def delete_answer(db: Session, db_answer: Answer):
    print("dddd", db_answer)
    db.delete(db_answer)
    db.commit()

def vote_answer(db: Session, db_answer: Answer, db_user: User):
    db_answer.voter.append(db_user)
    db.commit()