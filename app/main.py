"""The root file of the application"""
from fastapi import FastAPI
from database.db import init_db


app = FastAPI(
    title="Acme Customer Manager",
    description="The backend of a customer management app",
    version="0.1.0"
)


@app.on_event("startup")
async def app_startup():
    """Function is called on app startup"""
    print("Connecting to the database...")
    await init_db()


@app.get("/")
async def root() -> dict[str, str]:
    """The root endpoint

    Returns:
        dict[str, str]: Returns a simple dictionary
    """
    return {"message": "Hello World"}
