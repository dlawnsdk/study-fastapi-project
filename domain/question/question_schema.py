import datetime

from pydantic import BaseModel, validator
from domain.answer.answer_schema import Answer
from domain.user.user_schema import User


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answer: list[Answer] = []
    user: User | None
    modify_date: datetime.datetime | None = None
    voter: list[User] = []

    class Config:
        orm_mode = True


class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []


class QuestionCreate(BaseModel):
    subject: str
    content: str
    # create_date: datetime.datetime

    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


# 상속
class QuestionUpdate(QuestionCreate):
    question_id: int


class QuestionDelete(BaseModel):
    question_id: int


class QuestionVote(BaseModel):
    question_id: int
