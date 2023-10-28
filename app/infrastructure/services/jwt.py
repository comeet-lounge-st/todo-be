from config.settings import settings
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

access_token_transport = BearerTransport(tokenUrl="auth/sign-in")
refresh_token_transport = BearerTransport(tokenUrl="auth/jwt/refresh")


def get_access_token_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.access_token_secret,
        lifetime_seconds=settings.access_token_expiration,
    )


def get_refresh_token_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.refresh_token_secret,
        lifetime_seconds=settings.refresh_token_expiration,
    )


access_token_backend = AuthenticationBackend(
    name="jwt",
    transport=access_token_transport,
    get_strategy=get_access_token_strategy,
)

refresh_token_backend = AuthenticationBackend(
    name="jwt",
    transport=refresh_token_transport,
    get_strategy=get_refresh_token_strategy,
)
