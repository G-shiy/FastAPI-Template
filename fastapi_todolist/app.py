from fastapi import FastAPI, status

from fastapi_todolist.schemas.user_schema import UserResponseSchema, UserSchema, UserDB

app = FastAPI()

test_data = []

@app.post(
    '/users/',
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        id = len(test_data) + 1,
        **user.model_dump()
    )
    return user_with_id


@app.get('/health', status_code=status.HTTP_200_OK)
async def health_check():
    return {'status': 'healthy'}
