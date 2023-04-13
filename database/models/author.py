from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

author = Table(
    "author",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("job", String, nullable=False),
    Column("photo", String, nullable=False)
)
