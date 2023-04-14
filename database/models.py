from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey

metadata = MetaData()


author = Table(
    "author",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("job", String, nullable=False),
    Column("photo", String, nullable=False)
)


publication = Table(
    "publication",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("date", TIMESTAMP, default=datetime.utcnow),
    Column("author_id", Integer, ForeignKey("author.id")),
    Column("description", String, nullable=False)
)
