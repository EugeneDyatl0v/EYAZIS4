from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.api.article.views import article_router
app = FastAPI(
)

allow_origins = [
    'https://localhost:4200',
]

app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


app.include_router(article_router)
