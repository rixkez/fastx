from fastapi import APIRouter
from app.schemas.books import BookCreate, BookUpdate
from app.core.db import db
from app.services import book_service

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/")
async def create_book(book: BookCreate):
    return await book_service.create_book(db.books, book)


@router.get("/")
async def list_books():
    return await book_service.get_all_book(db.books)


@router.get("/{book_id}")
async def get_book(book_id: str):
    return await book_service.get_book(db.books, book_id)


@router.put("/{book_id}")
async def update_book(book_id: str, book: BookUpdate):
    return await book_service.update_book(db.books, book_id, book)


@router.delete("/{book_id}")
async def delete_book(book_id: str):
    return await book_service.delete_book(db.books, book_id)
