from api.schema import user_schema


def add_create_user_job(user: user_schema):
    return f"user {user.UserName} added"
