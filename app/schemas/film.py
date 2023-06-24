from pydantic import BaseModel, HttpUrl

from typing import Sequence


class FilmBase(BaseModel):
    label: str
    summary: str
    url: HttpUrl


class FilmCreate(FilmBase):
    label: str
    summary: str
    url: HttpUrl
    submitter_id: int


class FilmUpdate(FilmBase):
    id: int
    label: str
    summary: str
    url: HttpUrl

class FilmUpdateRestricted(BaseModel):
    id: int
    label: str

# Properties shared by models stored in DB
class FilmInDBBase(FilmBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Film(FilmInDBBase):
    pass


# Properties properties stored in DB
class FilmInDB(FilmInDBBase):
    pass


class FilmSearchResults(BaseModel):
    results: Sequence[Film]

class FilmDelete(FilmBase):
    id: int