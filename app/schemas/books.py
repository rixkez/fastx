from typing import Optional, Any
from pydantic import BaseModel

class StandardResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None

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