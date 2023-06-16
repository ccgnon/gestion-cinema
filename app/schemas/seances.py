rom pydantic import BaseModel, HttpUrl

from typing import Sequence


class SeancesBase(BaseModel):
    label: str
    source: str
    url: HttpUrl


class SeancesCreate(SeancesBase):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int


class SeancesUpdate(SeancesBase):
    label: str


# Properties shared by models stored in DB
class SeancesInDBBase(SeancesBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Seances(SeancesInDBBase):
    pass


# Properties properties stored in DB
class SeancesInDB(SeancesInDBBase):
    pass


class SeancesSearchResults(BaseModel):
    results: Sequence[Seances]
