from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models import author, publication
from schemas import Author, Publication


app = FastAPI()


@app.get("/authors", response_model=list[Author])
async def get_authors(offset: int = 0, limit: int = 10, session: AsyncSession = Depends(get_async_session)):
    query = select(author).order_by(author.c.name).limit(limit).offset(offset)
    result = (await session.execute(query)).all()
    return [Author(id=a[0], name=a[1], username=a[2], job=a[3], photo=a[4]) for a in result]


@app.get("/publications/{authorid}", response_model=list[Publication])
async def get_publications(author_id: int, offset: int = 0, limit: int = 10,  session: AsyncSession = Depends(get_async_session)):
    query = select(publication).where(publication.c.author_id == author_id).order_by(publication.c.date).limit(limit).offset(offset)
    result = (await session.execute(query)).all()
    return [Publication(id=p[0], title=p[1], date=p[2], author_id=p[3], description=p[4]) for p in result]
