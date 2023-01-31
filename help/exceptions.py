from .messages import (
    TYPE_USERNAME_ERROR,
    WALLET_TYPE_ERROR,
    VALUE_PASSWORD_ERROR,
    VALUE_START_PHONE,
    VALUE_LENGTH_PHONE,
    VALUE_USERNAME_ERROR
)


class TypeUsernameError(TypeError):
    def __str__(self) -> str:
        return TYPE_USERNAME_ERROR


class ValueUsernameError(ValueError):
    def __str__(self) -> str:
        return VALUE_USERNAME_ERROR


class ValuePasswordError(ValueError):
    def __str__(self) -> str:
        return VALUE_PASSWORD_ERROR


class ValueStartPhone(ValueError):
    def __str__(self) -> str:
        return VALUE_START_PHONE


class ValueLengthPhone(ValueError):
    def __str__(self) -> str:
        return VALUE_LENGTH_PHONE


class WalletTypeError(TypeError):
    def __str__(self) -> str:
        return WALLET_TYPE_ERROR
