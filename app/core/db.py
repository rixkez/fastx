from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]
load_dotenv()

from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.book 