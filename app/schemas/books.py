from typing import Optional
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    pages: int
    price: float

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    pages: Optional[int] = None
    price: Optional[float] = None

class BookResponse(BookBase):
    id: int