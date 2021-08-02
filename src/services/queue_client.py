from src.dtos.user import User


def add_create_user_job(user: User):
    return f"user {user.user_name} added"
