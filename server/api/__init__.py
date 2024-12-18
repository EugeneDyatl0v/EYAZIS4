from fastapi import FastAPI

from server.api.article.views import article_router
app = FastAPI(
)

app.include_router(article_router)
