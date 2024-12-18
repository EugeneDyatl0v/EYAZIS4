import uuid
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class ArticleSchema(BaseModel):
    title: str
    text: str
    source_language: str
    is_original: bool
    original_article_id: Optional[uuid.UUID]


class ArticleOutSchema(ArticleSchema):
    id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)


class ArticleListResponseSchema(BaseModel):
    success: bool
    message: str
    data: List[ArticleOutSchema]


class ArticleResponseSchema(BaseModel):
    success: bool
    message: str
    data: ArticleOutSchema


class WordFrequencySchema(BaseModel):
    normal_form: str
    frequency_count: int

    model_config = ConfigDict(from_attributes=True)

class WordFrequencyResponseSchema(BaseModel):
    success: bool
    message: str
    data: List[WordFrequencySchema]


class SpeechPartSchema(BaseModel):
    word: str
    part_of_speech: str


class SpeechPartResponseSchema(BaseModel):
    success: bool
    message: str
    data: List[SpeechPartSchema]


class SyntaxSchema(BaseModel):
    sentence: str
    image: str


class SyntaxResponseSchema(BaseModel):
    success: bool
    message: str
    data: List[SyntaxSchema]

