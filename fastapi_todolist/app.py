from fastapi import FastAPI, status

from fastapi_todolist.schemas.user_schema import UserSchema, UserResponseSchema

app = FastAPI()


@app.post("/users", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema):
    return user

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy"}