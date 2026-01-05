from fastapi import FastAPI, Request, HTTPException  # pyright: ignore[reportMissingImports]
from app.controllers.book_controller import router as book_router
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "data": None,
            "message": exc.detail
        }
    )

app.include_router(book_router)