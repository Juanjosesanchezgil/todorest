from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    surname: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
