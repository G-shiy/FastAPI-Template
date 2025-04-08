from fastapi import FastAPI, status

from fastapi_todolist.schemas.user_schema import UserResponseSchema, UserSchema

app = FastAPI()

test_data = []

@app.post(
    '/users/',
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: UserSchema):
    test_data.append(user)
    return user


@app.get('/health', status_code=status.HTTP_200_OK)
async def health_check():
    return {'status': 'healthy'}
