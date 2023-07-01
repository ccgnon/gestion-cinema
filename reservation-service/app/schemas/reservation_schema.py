from typing import Optional

from pydantic import BaseModel, EmailStr


class reservationBase(BaseModel):
    amount: Optional[int]
    status: Optional[str]
    email: Optional[EmailStr] = None
    is_client: bool = False
    