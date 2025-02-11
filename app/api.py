from datetime import datetime
from fastapi import FastAPI, Depends
from apscheduler.schedulers.background import BackgroundScheduler

from app.crawler import crawl_and_save
from app.database import get_db, init_db
from app.models import article

app = FastAPI(
    title = "PTT Stock Crawler",
    version = "1.0.0",
)

scheduler = BackgroundScheduler()
scheduler.add_job(
    crawl_and_save, 
    'interval', 
    minutes=10, 
    args=[next(get_db())],
    next_run_time=datetime.now()
)
scheduler.start()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def read_root():
    return {"message": "PTT Stock Crawler Service is running."}


@app.get("/articles")
def read_articles(
    db = Depends(get_db),
    page: int = 1,
    limit: int = 10
):
    articles = (
        db.query(article).
        offset((page - 1) * limit)
        .limit(limit)
        .all()
    )
    return articles


@app.get("/hot_articles")
def read_hot_articles(
    db = Depends(get_db),
    page: int = 1,
    limit: int = 10
):
    hot_articles = (
        db.query(article)
        .filter(article.push_count == 100)
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )
    return hot_articles