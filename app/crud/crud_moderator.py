from app.crud.base import CRUDBase
from app.models.moderator import Moderator
from app.schemas.moderator import ModeratorCreate, ModeratorUpdate


class CRUDModerator(CRUDBase[Moderator, ModeratorCreate, ModeratorUpdate]):
    pass


moderator = CRUDModerator(Moderator)
