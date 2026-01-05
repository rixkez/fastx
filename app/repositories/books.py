from bson import ObjectId
from app.schemas.books import BookCreate, BookUpdate

async def create(collection, book: BookCreate):
    data = book.model_dump()
    result = await collection.insert_one(data)

    data["id"] = str(result.inserted_id)
    data.pop("_id", None)

    return data

async def get_all(collection):
    books = []
    async for book in collection.find({}):
        book["id"] = str(book["_id"])
        del book["_id"]
        books.append(book)
    return books

async def get_by_id(collection, book_id: str):
    book = await collection.find_one({"_id": ObjectId(book_id)})

    if not book:
        return None

    book["id"] = str(book["_id"])
    del book["_id"]

    return book

async def update_book(collection, book_id: str, book: BookUpdate):
    update_data = book.model_dump(exclude_unset=True)

    if not update_data:
        return await get_by_id(collection, book_id)

    await collection.update_one(
        {"_id": ObjectId(book_id)},
        {"$set": update_data}
    )

    return await get_by_id(collection, book_id)

async def delete_book(collection, book_id: str) -> bool:
    result = await collection.delete_one({"_id": ObjectId(book_id)})
    return result.deleted_count == 1