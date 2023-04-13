from fastapi import FastAPI

app = FastAPI()


@app.get("/authors")
def get_authors(count: int, offset: int):
    pass


@app.get("/publications/{author_id}")
def get_publications(author_id: int):
    pass


