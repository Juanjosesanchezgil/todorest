from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    description: str | None = Field(default=None, index=True)
    complete: bool = Field(index=True)
