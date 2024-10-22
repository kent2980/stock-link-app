from app.models import Field, SQLModel


# Generic message
class Message(SQLModel):
    """メッセージを表すクラスです。

    Properties:
        message (str): メッセージです。

    Examples:
        Message(message="message")
    """

    message: str


# JSON payload containing access token
class Token(SQLModel):
    """アクセストークンを表すクラスです。

    Properties:
        access_token (str): アクセストークンです。
        token_type (str): トークンのタイプです。デフォルト値は"bearer"です。

    Examples:
        Token(access_token="string")
    """

    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    """JWTトークンのペイロードを表すクラスです。

    Properties:
        sub (int | None): ユーザーのIDです。デフォルト値はNoneです。

    Examples:
        TokenPayload(sub=1)
    """

    sub: int | None = None


class NewPassword(SQLModel):
    """新しいパスワードを表すクラスです。

    Properties:
        token (str): トークンです。
        new_password (str): 新しいパスワードです。

    Examples:
        NewPassword(token="string", new_password="string")
    """

    token: str
    new_password: str = Field(min_length=8, max_length=40)
