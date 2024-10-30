import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import EmailStr
from sqlmodel import (
    DECIMAL,
    Column,
    Field,
    Index,
    Integer,
    Relationship,
    SQLModel,
    UniqueConstraint,
)


# region User
# Shared properties
class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserRegister(SQLModel):
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=40)
    full_name: str | None = Field(default=None, max_length=255)


# Properties to receive via API on update, all are optional
class UserUpdate(UserBase):
    email: EmailStr | None = Field(default=None, max_length=255)  # type: ignore
    password: str | None = Field(default=None, min_length=8, max_length=40)


class UserUpdateMe(SQLModel):
    full_name: str | None = Field(default=None, max_length=255)
    email: EmailStr | None = Field(default=None, max_length=255)


class UpdatePassword(SQLModel):
    current_password: str = Field(min_length=8, max_length=40)
    new_password: str = Field(min_length=8, max_length=40)


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    items: list["Item"] = Relationship(back_populates="owner", cascade_delete=True)


# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: uuid.UUID


class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int


# endregion


# region Item
# Shared properties
class ItemBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


# Properties to receive on item creation
class ItemCreate(ItemBase):
    pass


# Properties to receive on item update
class ItemUpdate(ItemBase):
    title: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


# Database model, database table inferred from class name
class Item(ItemBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(max_length=255)
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    owner: User | None = Relationship(back_populates="items")


# Properties to return via API, id is always required
class ItemPublic(ItemBase):
    id: uuid.UUID
    owner_id: uuid.UUID


class ItemsPublic(SQLModel):
    data: list[ItemPublic]
    count: int


# Generic message
class Message(SQLModel):
    message: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str = Field(min_length=8, max_length=40)


# endregion


# region Stock
class XbrlBase(SQLModel):
    """XBRLの基底クラスです。

    Properties:
        id int: インスタンスのIDです。
        insert_date (datetime.datetime): 挿入日時です。
        update_date (datetime.datetime): 更新日時です。
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    item_key: Optional[str] = Field(max_length=36, min_length=36, unique=True)
    insert_date: datetime = Field(default_factory=datetime.now)
    update_date: datetime = Field(default_factory=datetime.now)


class IxLocsBase(XbrlBase):
    """iXBRLのリンクベース情報を表すクラス

    Properties:
        id int: インスタンスのIDです。
        xlink_type (str): リンクタイプです。
        xlink_schema (str): スキーマです。
        xlink_href (str): リンク先です。
        xlink_label (str): ラベルです。
    """

    xlink_type: Optional[str] = Field(max_length=255)
    xlink_schema: Optional[str] = Field(max_length=255)
    xlink_href: Optional[str] = Field(default=None)
    xlink_label: Optional[str] = Field(default=None)


class IxArcsBase(XbrlBase):
    """iXBRLのリンクベース情報を表すクラス

    Properties:
        id int: インスタンスのIDです。
        xlink_type (str): リンクタイプです。
        xlink_arcrole (str): アークロールです。
        xlink_from (str): リンク元です。
        xlink_to (str): リンク先です。
    """

    xlink_type: Optional[str] = Field(max_length=255)
    xlink_arcrole: Optional[str] = Field(max_length=255)
    xlink_from: Optional[str] = Field(default=None)
    xlink_to: Optional[str] = Field(default=None)


class IxFilePath(XbrlBase, table=True):
    """ソースファイルのパス情報を表すクラス"""

    __tablename__ = "ix_file_path"

    xbrl_id: str = Field(default=None, max_length=36, unique=True)
    path: str = Field(default=None)


class IxHeadTitle(XbrlBase, table=True):
    """Class representing iXBRL header information"""

    __tablename__ = "ix_head_title"

    company_name: Optional[str] = Field(max_length=255, description="企業名")
    securities_code: str = Field(max_length=4, description="証券コード")
    document_name: Optional[str] = Field(max_length=255, description="書類名")
    reporting_date: date = Field(description="報告日")
    current_period: Optional[str] = Field(max_length=255, description="決算期")
    xbrl_id: str = Field(max_length=36, foreign_key="ix_file_path.xbrl_id", unique=True)
    report_type: Optional[str] = Field(max_length=4, description="報告書種別")
    listed_market: Optional[str] = Field(default=None, description="上場市場")
    market_section: Optional[str] = Field(default=None, description="市場区分")
    url: Optional[str] = Field(default=None, description="URL")
    is_bs: bool = Field(default=False, nullable=True, description="貸借対照表")
    is_pl: bool = Field(default=False, nullable=True, description="損益計算書")
    is_cf: bool = Field(
        default=False, nullable=True, description="キャッシュフロー計算書"
    )
    is_ci: bool = Field(default=False, nullable=True, description="包括利益計算書")
    is_sce: bool = Field(
        default=False, nullable=True, description="株主資本等変動計算書"
    )
    is_sfp: bool = Field(
        default=False, nullable=True, description="株主資本等変動計算書"
    )
    fiscal_year_end: Optional[str] = Field(default=None, description="決算期")
    tel: Optional[str] = Field(default=None, description="電話番号")
    is_dividend_revision: Optional[bool] = Field(
        default=None, nullable=True, description="配当修正"
    )
    dividend_increase_rate: Optional[str] = Field(default=None, description="増配率")
    is_earnings_forecast_revision: Optional[bool] = Field(
        default=None, nullable=True, description="業績予想の修正"
    )
    forecast_ordinary_income_growth_rate: Optional[str] = Field(
        default=None, description="予想経常利益増益率"
    )


class IxCalculationLoc(IxLocsBase, table=True):
    """Class representing iXBRL calculation location information"""

    __tablename__ = "ix_calculation_loc"

    xbrl_id: str = Field(default=None, max_length=36)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_href: Optional[str] = Field(default=None)
    source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )


class IxCalculationArc(IxArcsBase, table=True):
    """Class representing iXBRL calculation arc information"""

    __tablename__ = "ix_calculation_arc"

    xbrl_id: str = Field(default=None, max_length=36)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_order: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    xlink_weight: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )


class IxDefinitionLoc(IxLocsBase, table=True):
    """Class representing iXBRL definition location information"""

    __tablename__ = "ix_definition_loc"

    xbrl_id: str = Field(default=None, max_length=36)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_href: Optional[str] = Field(default=None)
    source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )

    __table_args__ = (
        Index("idx_ix_definition_loc_xbrl_id", "xbrl_id"),
        Index("idx_ix_definition_loc_source_file_id", "source_file_id"),
        Index("idx_ix_definition_loc_xlink_label", "xlink_label"),
        Index("idx_ix_definition_loc_attr_value", "attr_value"),
        Index("idx_ix_definition_loc_xlink_href", "xlink_href"),
        Index(
            "idx_ix_definition_loc_attr_value_xlink_label", "attr_value", "xlink_label"
        ),
        UniqueConstraint(
            "xbrl_id",
            "source_file_id",
            "xlink_label",
            "xlink_href",
            "attr_value",
            name="ix_definition_loc_uc",
        ),
    )


class IxDefinitionArc(IxArcsBase, table=True):
    """Class representing iXBRL definition arc information"""

    __tablename__ = "ix_definition_arc"

    xbrl_id: str = Field(default=None, max_length=36)
    xlink_to: str = Field(max_length=255)
    xlink_from: str = Field(max_length=255)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_order: Decimal = Field(sa_column=Column(DECIMAL(5, 2)))
    xlink_weight: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )

    __table_args__ = (
        Index("idx_ix_definition_arc_xbrl_id", "xbrl_id"),
        Index("idx_ix_definition_arc_xlink_to", "xlink_to"),
        Index("idx_ix_definition_arc_attr_value", "attr_value"),
        Index("idx_ix_definition_arc_xlink_from", "xlink_from"),
        Index("idx_ix_definition_arc_xlink_order", "xlink_order"),
        Index("idx_ix_definition_arc_source_file_id", "source_file_id"),
        Index("idx_ix_definition_arc_xlink_arcrole", "xlink_arcrole"),
        Index("idx_ix_definition_arc_attr_value_xlink_to", "attr_value", "xlink_to"),
        Index(
            "idx_ix_definition_arc_attr_value_xlink_from", "attr_value", "xlink_from"
        ),
        Index(
            "idx_ix_definition_arc_source_file_id_attr_value",
            "source_file_id",
            "attr_value",
        ),
        UniqueConstraint(
            "xbrl_id",
            "source_file_id",
            "xlink_from",
            "xlink_to",
            "xlink_arcrole",
            "attr_value",
            name="ix_definition_arc_uc",
        ),
    )


class IxLabelLoc(IxLocsBase, table=True):
    """Class representing iXBRL label location information"""

    __tablename__ = "ix_label_loc"

    xlink_href: Optional[str] = Field(default=None)
    xlink_label: Optional[str] = Field(default=None)
    source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )

    __table_args__ = (
        UniqueConstraint(
            "xlink_href", "xlink_label", "source_file_id", name="ix_label_loc_uc"
        ),
        Index("idx_ix_label_loc_xlink_href", "xlink_href"),
        Index("idx_ix_label_loc_xlink_label", "xlink_label"),
        Index(
            "idx_ix_label_loc_source_file_id_xlink_label",
            "source_file_id",
            "xlink_label",
        ),
    )


class IxLabelArc(IxArcsBase, table=True):
    """Class representing iXBRL label arc information"""

    __tablename__ = "ix_label_arc"

    source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )

    __table_args__ = (
        UniqueConstraint(
            "xlink_arcrole",
            "xlink_from",
            "xlink_to",
            "source_file_id",
            name="ix_label_arc_uc",
        ),
        Index("idx_ix_label_arc_source_file_id", "source_file_id"),
        Index(
            "idx_ix_label_arc_source_file_id_xlink_from", "source_file_id", "xlink_from"
        ),
        Index("idx_ix_label_arc_source_file_id_xlink_to", "source_file_id", "xlink_to"),
    )


class IxLabelValue(XbrlBase, table=True):
    """Class representing iXBRL label link information"""

    __tablename__ = "ix_label_value"

    xlink_type: Optional[str] = Field(max_length=255)
    xlink_label: Optional[str] = Field(default=None)
    xlink_role: Optional[str] = Field(max_length=255)
    xml_lang: Optional[str] = Field(max_length=255)
    label: str = Field(default=None)
    source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )

    __table_args__ = (
        UniqueConstraint("xlink_label", "source_file_id", name="ix_label_value_uc"),
        Index("idx_ix_label_value_source_file_id", "source_file_id"),
        Index("idx_ix_label_value_xlink_label", "xlink_label"),
        Index("idx_ix_label_value_xlink_role", "xlink_role"),
    )


class IxNonFraction(XbrlBase, table=True):
    """Class representing iXBRL non-fraction information"""

    __tablename__ = "ix_non_fraction"

    xbrl_id: str = Field(default=None, max_length=36)
    context: str = Field(default=None)
    decimals: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(5, 2)))
    format: Optional[str] = Field(max_length=255)
    name: str = Field(default=None)
    scale: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(5, 2)))
    sign: Optional[str] = Field(max_length=255, default=None)
    unit_ref: Optional[str] = Field(max_length=255)
    xsi_nil: Optional[bool] = Field(default=None)
    numeric: Optional[Decimal] = Field(default=None, sa_column=Column(DECIMAL(20, 2)))
    report_type: Optional[str] = Field(max_length=4)
    ixbrl_role: Optional[str] = Field(max_length=255)
    source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )
    xbrl_type: Optional[str] = Field(max_length=2)
    display_numeric: Optional[str] = Field(default=None)
    display_scale: Optional[str] = Field(default=None)

    __table_args__ = (
        Index("idx_ix_non_fraction_xbrl_id", "xbrl_id"),
        Index("idx_ix_non_fraction_name", "name"),
        Index("idx_ix_non_fraction_xbrl_type", "xbrl_type"),
        Index("idx_ix_non_fraction_context", "context"),
    )

    __str__ = "ix_non_fraction"


class IxNonNumeric(XbrlBase, table=True):
    """Class representing iXBRL non-numeric information"""

    __tablename__ = "ix_non_numeric"

    xbrl_id: str = Field(default=None, max_length=36)
    context: str = Field(default=None)
    name: str = Field(default=None)
    xsi_nil: Optional[bool] = Field(default=None)
    escape: Optional[bool] = Field(default=False)
    format: Optional[str] = Field(max_length=255)
    value: Optional[str] = Field(default=None)
    report_type: Optional[str] = Field(max_length=4)
    ixbrl_role: Optional[str] = Field(max_length=255)
    source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )
    xbrl_type: Optional[str] = Field(max_length=2)

    __table_args__ = (
        Index("idx_ix_non_numeric_xbrl_id", "xbrl_id"),
        Index("idx_ix_non_numeric_name", "name"),
        Index("idx_ix_non_numeric_xbrl_type", "xbrl_type"),
        Index("idx_ix_non_numeric_context", "context"),
    )

    __str__ = "ix_non_numeric"


class IxPresentationLoc(IxLocsBase, table=True):
    """Class representing iXBRL presentation label location information"""

    __tablename__ = "ix_presentation_loc"

    xbrl_id: str = Field(default=None, max_length=36)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_href: Optional[str] = Field(default=None)
    source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )


class IxPresentationArc(IxArcsBase, table=True):
    """Class representing iXBRL presentation label arc information"""

    __tablename__ = "ix_presentation_arc"

    xbrl_id: str = Field(default=None, max_length=36)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_order: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    xlink_weight: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )


class IxSourceFile(XbrlBase, table=True):
    """ソースファイル情報を表すクラス"""

    __tablename__ = "ix_source_file"

    id: Optional[str] = Field(max_length=36, primary_key=True)
    name: Optional[str] = Field(max_length=255)
    type: Optional[str] = Field(max_length=255)
    xbrl_id: Optional[str] = Field(max_length=36, foreign_key="ix_head_title.xbrl_id")
    url: Optional[str] = Field(max_length=255)

    __table_args__ = (Index("idx_ix_source_file_id", "id"),)


class ScLinkBaseRef(XbrlBase, table=True):
    """Class representing iXBRL linkbase reference information"""

    __tablename__ = "ix_schema_linkbase"

    xlink_arcrole: Optional[str] = Field(max_length=255)
    xlink_href: Optional[str] = Field(max_length=255)
    xlink_role: Optional[str] = Field(max_length=255)
    xlink_type: Optional[str] = Field(max_length=255)
    source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )
    xbrl_id: str = Field(max_length=36)
    xbrl_type: Optional[str] = Field(max_length=255)
    href_source_file_id: Optional[str] = Field(
        max_length=36, foreign_key="ix_source_file.id"
    )

    __table_args__ = (
        Index("idx_ix_schema_linkbase_xbrl_id", "xbrl_id"),
        Index("idx_ix_schema_linkbase_xbrl_type", "xbrl_type"),
        Index("idx_ix_schema_linkbase_xbrl_id_xlink_role", "xbrl_id", "xlink_role"),
        Index("idx_ix_schema_linkbase_href_source_file_id", "href_source_file_id"),
    )


class IxQualitative(XbrlBase, table=True):
    """Class representing iXBRL qualitative information"""

    __tablename__ = "ix_qualitative"

    currentId: str = Field(default=None, max_length=36, description="ID", unique=True)
    parentId: Optional[str] = Field(default=None, max_length=36, description="親ID")
    type: Optional[str] = Field(default=None, max_length=255, description="種類")
    content: Optional[str] = Field(default=None, description="タイトル、本文")
    order: Optional[int] = Field(default=None, description="順序")
    xbrl_id: str = Field(
        default=None,
        max_length=36,
        description="XBRL ID",
    )
    source_file_id: Optional[str] = Field(
        default=None,
        max_length=36,
        description="ソースファイルID",
        foreign_key="ix_source_file.id",
    )
    photo_url: Optional[str] = Field(default=None, description="画像URL")


class IxStockInfos(XbrlBase, table=True):
    """期末に公表される決算情報を表すクラス"""

    __tablename__ = "ix_stock_infos"

    code: str = Field(max_length=4, description="証券コード")
    name: str = Field(max_length=255, description="企業名")
    payout_ratio: Optional[str] = Field(max_length=255, description="配当性向")
    roe: Optional[str] = Field(max_length=255, description="自己資本当期純利益率")
    roa: Optional[str] = Field(max_length=255, description="総資産経常利益率")
    op_margin: Optional[str] = Field(max_length=255, description="売上高営業利益率")
    cf_operating: Optional[str] = Field(max_length=255, description="営業CF")
    cf_investing: Optional[str] = Field(max_length=255, description="投資CF")
    cf_financing: Optional[str] = Field(max_length=255, description="財務CF")
    cash_end: Optional[str] = Field(max_length=255, description="期末現金残高")


# endregion
