from app.crud.base import CRUDBase
from app.models.Seances import Seances
from app.schemas.Seances import SeancesCreate, SeancesUpdate


class CRUDSeances(CRUDBase[Seances, SeancesCreate, SeancesUpdate]):
    ...


film = CRUDSeances(Seances)