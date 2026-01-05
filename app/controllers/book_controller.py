from fastapi import APIRouter, HTTPException
from app.schemas.books import BookCreate, BookUpdate, StandardResponse
from app.core.db import db
from app.services import book_service

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=StandardResponse)
async def create_book(book: BookCreate):
    data = await book_service.create_book(db.books, book)
    return StandardResponse(
        success=True,
        data=data,
        message="Book created"
    )

@router.get("/", response_model=StandardResponse)
async def list_books():
    data = await book_service.get_all_book(db.books)
    return StandardResponse(
        success = True,
        data = data,
        message =  f"{len(data)} books fetched"
    )

@router.get("/{book_id}", response_model=StandardResponse)
async def get_book(book_id: str):
    data = await book_service.get_book(db.books, book_id)
    return StandardResponse(success=True, data=data, message="book returned")

@router.put("/{book_id}", response_model=StandardResponse)
async def update_book(book_id: str, book: BookUpdate):
    data = await book_service.update_book(db.books, book_id, book)
    return StandardResponse(success=True, data=data, message="book updated")

@router.delete("/{book_id}", response_model=StandardResponse)
async def delete_book(book_id: str):
    data = await book_service.delete_book(db.books, book_id)
    return StandardResponse(success=True, data=data, message="book deleted")
