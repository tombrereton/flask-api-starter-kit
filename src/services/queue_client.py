from src.dtos.user import UserDto


def add_create_user_job(user: UserDto):
    return f"user {user.user_name} added"
