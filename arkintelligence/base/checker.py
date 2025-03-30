import os


def _api_key_check():
    assert (
        os.getenv("ARK_API_KEY") is not None
    ), "ARK_API_KEY must be provided in environment variables."


def api_key_check(func):
    def wrapper(*args, **kwargs):
        _api_key_check()
        return func(*args, **kwargs)

    return wrapper


def _secret_key_check():
    assert (
        os.getenv("ARK_SECRET_KEY") is not None
    ), "ARK_SECRET_KEY must be provided in environment variables."


def secret_key_check(func):
    def wrapper(*args, **kwargs):
        _secret_key_check()
        return func(*args, **kwargs)

    return wrapper
