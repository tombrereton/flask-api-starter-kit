from api.schema import user


def add_create_user_job(user: user):
    return f"user {user.UserName} added"
