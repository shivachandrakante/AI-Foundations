
from pydantic import BaseModel, EmailStr, ValidationError

class GeminiResponse(BaseModel):
    text: str
    tokens: int 
    success: str
    email: EmailStr


try:
    response1 = GeminiResponse(
        text = "Python is a aprogramming Language",
        tokens = "T100",
        success="true",
        email="dummyemailemail.com"
    )
    print(response1)
except ValidationError as e:
    print(f"Exception message {e.errors()}")
except Exception as e:
    print(f"Error message {e}")

