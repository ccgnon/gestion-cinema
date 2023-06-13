from app.crud.base import CRUDBase
from app.models.film import Film
from app.schemas.film import FilmCreate, FilmUpdate


class CRUDFilm(CRUDBase[Film, FilmCreate, FilmUpdate]):
    ...
// premier commit

film = CRUDFilm(Film)
