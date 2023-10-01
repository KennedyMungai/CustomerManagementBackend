"""The root file of the application"""
from fastapi import FastAPI


app = FastAPI(
    title="Acme Customer Manager",
    description="The backend of a customer management app",
    version="0.1.0"
)


@app.get("/")
async def root() -> dict[str, str]:
    """The root endpoint

    Returns:
        dict[str, str]: Returns a simple dictionary
    """
    return {"message": "Hello World"}
