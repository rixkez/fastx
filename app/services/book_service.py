from fastapi import HTTPException, status
from app.schemas.books import BookCreate, BookUpdate
from app.repositories import books as repo


async def create_book(collection, book: BookCreate):
    return await repo.create(collection, book)

async def get_all_book(collection):
    return await repo.get_all(collection)

async def get_book(collection, book_id):
    book = await repo.get_by_id(collection, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    return book

async def update_book(collection, book_id, book: BookUpdate):
    existing = await repo.get_by_id(collection, book_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    return await repo.update_book(collection, book_id, book)

async def delete_book(collection, book_id: str):
    deleted = await repo.delete_book(collection, book_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    return {"deleted": True}