from typing import List
from fastapi import FastAPI, HTTPException, status

from fastapi_todolist.schemas.user_schema import (
    UserDB,
    UserResponseSchema,
    UserSchema,
)

app = FastAPI()

test_data = []


@app.post(
    '/users/',
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        id=len(test_data) + 1,
        **user.model_dump()
    )
    test_data.append(user_with_id)
    return user_with_id

@app.get(
    '/users/',
    response_model=List[UserResponseSchema],
    status_code=status.HTTP_200_OK,
)
def get_users():
    if not test_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No users found'
        )
    
    return [user.model_dump() for user in test_data]



@app.get('/health', status_code=status.HTTP_200_OK)
async def health_check():
    return {'status': 'healthy'}
