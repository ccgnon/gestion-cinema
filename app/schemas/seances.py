from pydantic import BaseModel, HttpUrl

from typing import Sequence


class SeancesBase(BaseModel):
    id: int


class SeancesCreate(SeancesBase):
    date: str
    submitter_id: int


class SeancesUpdate(SeancesBase):
    heure: int

class SeancesUpdate(SeancesBase):
    id_films: int

class SeancesUpdate(SeancesBase):
    id_salle: int

# Properties shared by models stored in DB
class SeancesInDBBase(SeancesBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Seances(SeancesInDBBase):
    pass
# Properties to return to client
class Seances(SeancesInDBBase):
    pass

# Properties to return to client
class Seances(SeancesInDBBase):
    pass

# Properties properties stored in DB
class SeancesInDB(SeancesInDBBase):
    pass


class SeancesSearchResults(BaseModel):
    results: Sequence[Seances]
