import math
import re
import uuid

from fastapi import APIRouter, Query, HTTPException

from googletrans import Translator

from sqlalchemy import select, func
from starlette.responses import JSONResponse

from server.api.article.schemas import ArticleListResponseSchema, ArticleOutSchema, ArticleResponseSchema, \
    ArticleSchema, WordFrequencyResponseSchema, WordFrequencySchema, SpeechPartResponseSchema, SpeechPartSchema, \
    SyntaxResponseSchema, SyntaxSchema
from server.database import get_session
from server.database.models import ArticleModel
from server.modules.checker import Checker
from server.modules.helpers import get_text
from server.modules.speech_parts import analyze_text

import spacy
from spacy import displacy

ru_nlp = spacy.load('ru_core_news_md')
en_nlp = spacy.load('en_core_web_sm')

article_router = APIRouter(
    prefix='/articles',
    tags=['Articles'],
)


@article_router.get('/')
async def get_articles():
    async with get_session() as session:
        query = select(ArticleModel)
        results = await session.execute(query)
        db_articles = results.scalars().all()

        return ArticleListResponseSchema(
            success=True,
            message='Successfully fetched articles',
            data=[ArticleOutSchema.model_validate(db_article) for db_article in db_articles],
        )


@article_router.get('/{id}/')
async def get_article(
        id: uuid.UUID
):
    async with get_session() as session:
        query = select(ArticleModel).filter_by(id=id)
        result = await session.execute(query)
        db_article = result.scalars().one_or_none()

        if not db_article:
            raise HTTPException(
                status_code=404,
                detail='Article not found',
            )

        return ArticleResponseSchema(
            success=True,
            message='Successfully fetched article',
            data=ArticleOutSchema.model_validate(db_article)
        )


@article_router.post('/')
async def create_article(
        article: ArticleSchema
):
    async with get_session() as session:
        new_article = ArticleModel(
            title=article.title,
            text=article.text,
            source_language=article.source_language,
            is_original=article.is_original,
            original_article_id=article.original_article_id
        )

        session.add(new_article)
        await session.commit()

        return JSONResponse(
            {'message': 'Successfully created article'},
            200
        )


@article_router.delete('/')
async def delete_article(
        article_id: uuid.UUID
):
    async with get_session() as session:
        query = select(ArticleModel).filter_by(id=article_id)
        result = await session.execute(query)
        db_article = result.scalars().one_or_none()

        if not db_article:
            raise HTTPException(
                status_code=404,
                detail='Article not found',
            )

        await session.delete(db_article)
        await session.commit()

        return JSONResponse(
            {'message': 'Successfully deleted article'},
            200
        )


@article_router.get('/translate/{id}/')
async def get_translated_article(
        id: uuid.UUID,
        target_language: str
):
    async with get_session() as session:
        query = select(ArticleModel).filter_by(id=id)
        result = await session.execute(query)
        db_article = result.scalars().one_or_none()

        if not db_article:
            raise HTTPException(
                status_code=404,
                detail='Article not found',
            )

        if not db_article.is_original:
            raise HTTPException(
                status_code=400,
                detail='Can\'t translate translation',
            )

        translator = Translator()
        translated_title = translator.translate(db_article.title, dest=target_language)
        translated_text = translator.translate(db_article.text, dest=target_language)

        new_article = ArticleModel(
            title=translated_title.text,
            text=translated_text.text,
            source_language=target_language,
            is_original=False,
            original_article_id=db_article.id
        )
        session.add(new_article)
        await session.commit()
        await session.refresh(new_article)
        return ArticleResponseSchema(
            success=True,
            message='Successfully translated article',
            data=ArticleOutSchema.model_validate(new_article)
        )


@article_router.get('/{id}/words/')
async def get_article_words(
        id: uuid.UUID
):
    async with get_session() as session:
        query = select(ArticleModel).filter_by(id=id)
        result = await session.execute(query)
        db_article = result.scalars().one_or_none()

        if not db_article:
            raise HTTPException(
                status_code=404,
                detail='Article not found',
            )

        checker = Checker()
        text = get_text(db_article.text)
        words = text.split(" ")
        all_words = checker.count_words(words)
        all_words = sorted(all_words, key=lambda word: word.normal_form)

        return WordFrequencyResponseSchema(
            success=True,
            message='Successfully fetched words frequency',
            data=[WordFrequencySchema.model_validate(word) for word in all_words]
        )


class SpeechPartSchemaResponseSchema:
    pass


class SpeechPartSchemaSchema:
    pass


@article_router.get('/{id}/words/speech-parts/')
async def get_article_words_speech_parts(
        id: str
):
    print('111')
    async with get_session() as session:
        query = select(ArticleModel).filter_by(id=id)
        result = await session.execute(query)
        db_article = result.scalars().one_or_none()

        if not db_article:
            raise HTTPException(
                status_code=404,
                detail='Article not found',
            )

        text = get_text(db_article.text)
        speech_parts = analyze_text(text)

        return SpeechPartResponseSchema(
            success=True,
            message='Successfully fetched words speech parts',
            data=[
                SpeechPartSchema(
                    word=word[0],
                    part_of_speech=word[1]
                ) for word in speech_parts
            ]
        )


@article_router.get('/{id}/syntax/')
async def get_article_syntax(
        id: uuid.UUID
):
    async with get_session() as session:
        query = select(ArticleModel).filter_by(id=id)
        result = await session.execute(query)
        db_article = result.scalars().one_or_none()

        if not db_article:
            raise HTTPException(
                status_code=404,
                detail='Article not found',
            )

        sentences = re.split(r'(?<=[.!?]) +', db_article.text)

        svg_list = []

        nlp = en_nlp if db_article.source_language == 'en' else ru_nlp
        spacy_sentences = []

        for sentence in sentences:
            doc = nlp(sentence.strip())
            spacy_sentences.append((doc, sentence))

        for sentence in spacy_sentences:
            svg = displacy.render(sentence[0], style='dep', options={'compact': True})
            pattern = r'width="(\d+)"'  # Регулярное выражение для поиска подстроки width="n"
            replacement = r'width="200%"'  # Заменить на новое значение
            svg_with_new_size = re.sub(pattern, replacement, svg, count=1)
            svg_list.append((svg_with_new_size, sentence[1]))

        return SyntaxResponseSchema(
            success=True,
            message='Successfully fetched syntax',
            data=[
                SyntaxSchema(
                    sentence=svg_item[1],
                    image=svg_item[0]
                ) for svg_item in svg_list
            ]
        )
