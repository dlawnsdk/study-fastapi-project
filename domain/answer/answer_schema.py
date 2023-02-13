import datetime

from pydantic import BaseModel, validator
from domain.user.user_schema import User

# Request Body인 경우 Pydantic의 BaseModel을 통해 데이터 체크를 수행한다.
# 이것이 의미하는 것 -> Request Body를 통해 받을 데이터를 만든다.


class AnswerCreate(BaseModel):
    content: str

    @validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
    user: User | None
    question_id: int
    modify_date: datetime.datetime | None = None
    voter: list[User] = []

    class Config:
        orm_mode = True


class AnswerUpdate(AnswerCreate):
    answer_id: int


class AnswerDelete(BaseModel):
    answer_id: int


class AnswerVote(BaseModel):
    answer_id: int
