import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import EmailStr
from sqlmodel import (
    DECIMAL,
    Column,
    Field,
    ForeignKeyConstraint,
    Index,
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
        item_key str: アイテムキーです。
        insert_date datetime: 挿入日時です。
        update_date datetime: 更新日時です。
    """

    id: Optional[int] = Field(
        default=None, primary_key=True, sa_column_kwargs={"comment": "ID"}
    )
    item_key: Optional[str] = Field(
        max_length=36,
        min_length=36,
        unique=True,
        sa_column_kwargs={"comment": "ItemKey"},
    )
    insert_date: datetime = Field(
        default_factory=datetime.now, sa_column_kwargs={"comment": "作成日時"}
    )
    update_date: datetime = Field(
        default_factory=datetime.now, sa_column_kwargs={"comment": "更新日時"}
    )


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

    head_item_key: str = Field(
        max_length=36, unique=True, sa_column_kwargs={"comment": "HeadItemKey"}
    )
    path: str = Field(default=None, sa_column_kwargs={"comment": "パス"})


class IxHeadTitle(XbrlBase, table=True):
    """Class representing iXBRL header information"""

    __tablename__ = "ix_head_title"

    item_key: str = Field(
        max_length=36,
        unique=True,
        foreign_key="ix_file_path.head_item_key",
        sa_column_kwargs={"comment": "ItemKey"},
    )
    company_name: Optional[str] = Field(
        default=None,
        max_length=255,
        description="企業名",
        sa_column_kwargs={"comment": "企業名"},
    )
    securities_code: Optional[str] = Field(
        default=None,
        max_length=4,
        description="証券コード",
        sa_column_kwargs={"comment": "証券コード"},
    )
    document_name: Optional[str] = Field(
        default=None,
        max_length=255,
        description="書類名",
        sa_column_kwargs={"comment": "書類名"},
    )
    reporting_date: Optional[date] = Field(
        default=None, description="報告日", sa_column_kwargs={"comment": "報告日"}
    )
    current_period: Optional[str] = Field(
        default=None,
        max_length=255,
        description="決算期",
        sa_column_kwargs={"comment": "決算期"},
    )
    report_type: Optional[str] = Field(
        default=None,
        max_length=4,
        description="報告書種別",
        sa_column_kwargs={"comment": "報告書種別"},
    )
    listed_market: Optional[str] = Field(
        default=None, description="上場市場", sa_column_kwargs={"comment": "上場市場"}
    )
    market_section: Optional[str] = Field(
        default=None, description="市場区分", sa_column_kwargs={"comment": "市場区分"}
    )
    url: Optional[str] = Field(
        default=None, description="URL", sa_column_kwargs={"comment": "URL"}
    )
    is_bs: Optional[bool] = Field(
        default=False,
        nullable=True,
        description="貸借対照表",
        sa_column_kwargs={"comment": "貸借対照表"},
    )
    is_pl: Optional[bool] = Field(
        default=False,
        nullable=True,
        description="損益計算書",
        sa_column_kwargs={"comment": "損益計算書"},
    )
    is_cf: Optional[bool] = Field(
        default=False,
        nullable=True,
        description="キャッシュフロー計算書",
        sa_column_kwargs={"comment": "キャッシュフロー計算書"},
    )
    is_ci: Optional[bool] = Field(
        default=False,
        nullable=True,
        description="包括利益計算書",
        sa_column_kwargs={"comment": "包括利益計算書"},
    )
    is_sce: Optional[bool] = Field(
        default=False,
        nullable=True,
        description="株主資本等変動計算書",
        sa_column_kwargs={"comment": "株主資本等変動計算書"},
    )
    is_sfp: Optional[bool] = Field(
        default=False,
        nullable=True,
        description="株主資本等変動計算書",
        sa_column_kwargs={"comment": "株主資本等変動計算書"},
    )
    fy_year_end: Optional[str] = Field(
        default=None, description="決算期", sa_column_kwargs={"comment": "決算期"}
    )
    tel: Optional[str] = Field(
        default=None, description="電話番号", sa_column_kwargs={"comment": "電話番号"}
    )
    is_div_rev: Optional[bool] = Field(
        default=None,
        nullable=True,
        description="配当修正",
        sa_column_kwargs={"comment": "配当修正"},
    )
    div_inc_rt: Optional[str] = Field(
        default=None, description="増配率", sa_column_kwargs={"comment": "増配率"}
    )
    is_fcst_rev: Optional[bool] = Field(
        default=None,
        nullable=True,
        description="業績予想の修正",
        sa_column_kwargs={"comment": "業績予想の修正"},
    )
    fcst_oi_gr_rt: Optional[str] = Field(
        default=None,
        description="予想経常利益増益率",
        sa_column_kwargs={"comment": "予想経常利益増益率"},
    )
    oi_prog_rt: Optional[float] = Field(
        default=None,
        description="経常利益進捗率",
        sa_column_kwargs={"comment": "経常利益進捗率"},
    )
    is_active: bool = Field(
        default=False,
        nullable=False,
        description="有効フラグ",
        sa_column_kwargs={"comment": "有効フラグ"},
    )
    is_generated: bool = Field(
        default=False,
        nullable=False,
        description="生成フラグ",
        sa_column_kwargs={"comment": "生成フラグ"},
    )
    specific_business: Optional[bool] = Field(
        default=None, description="特定事業", sa_column_kwargs={"comment": "特定事業"}
    )
    is_consolidated: Optional[bool] = Field(
        default=None, description="連結", sa_column_kwargs={"comment": "連結"}
    )
    change_in_net_sales: Optional[float] = Field(
        default=None,
        description="売上高増減率",
        sa_column_kwargs={"comment": "売上高増減率"},
    )
    change_in_ordinary_income: Optional[float] = Field(
        default=None,
        description="経常利益増減率",
        sa_column_kwargs={"comment": "経常利益増減率"},
    )
    change_in_net_income: Optional[float] = Field(
        default=None,
        description="当期純利益増減率",
        sa_column_kwargs={"comment": "当期純利益増減率"},
    )
    change_in_fore_net_sales: Optional[float] = Field(
        default=None,
        description="予想売上高増減率",
        sa_column_kwargs={"comment": "予想売上高増減率"},
    )
    change_in_fore_ordinary_income: Optional[float] = Field(
        default=None,
        description="予想経常利益増減率",
        sa_column_kwargs={"comment": "予想経常利益増減率"},
    )
    change_in_fore_net_income: Optional[float] = Field(
        default=None,
        description="予想純利益増減率",
        sa_column_kwargs={"comment": "予想純利益増減率"},
    )

    __table_args__ = (
        Index("idx_ix_head_title_item_key", "item_key"),
        Index("idx_ix_head_title_reporting_date", "reporting_date"),
        Index("idx_ix_head_title_report_type", "report_type"),
        Index("idx_ix_head_title_is_active", "is_active"),
        Index("idx_ix_head_title_is_generated", "is_generated"),
        Index("idx_ix_head_title_current_period", "current_period"),
        Index("idx_ix_head_specific_business", "specific_business"),
        Index("idx_ix_head_title_is_consolidated", "is_consolidated"),
    )


class IxSourceFile(XbrlBase, table=True):
    """ソースファイル情報を表すクラス"""

    __tablename__ = "ix_source_file"

    id: Optional[str] = Field(max_length=36, primary_key=True)
    name: Optional[str] = Field(max_length=255)
    type: Optional[str] = Field(max_length=255)
    head_item_key: Optional[str] = Field(max_length=36)
    url: Optional[str] = Field(max_length=255)

    __table_args__ = (
        Index("idx_ix_source_file_id", "id"),
        ForeignKeyConstraint(["head_item_key"], ["ix_head_title.item_key"]),
    )


class IxCalculationLoc(IxLocsBase, table=True):
    """Class representing iXBRL calculation location information"""

    __tablename__ = "ix_calculation_loc"

    head_item_key: str = Field(default=None, max_length=36)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_href: Optional[str] = Field(default=None)
    source_file_id: Optional[str] = Field(max_length=36)

    __table_args__ = (
        ForeignKeyConstraint(["head_item_key"], ["ix_head_title.item_key"]),
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
    )


class IxCalculationArc(IxArcsBase, table=True):
    """Class representing iXBRL calculation arc information"""

    __tablename__ = "ix_calculation_arc"

    head_item_key: str = Field(default=None, max_length=36)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_order: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    xlink_weight: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    source_file_id: Optional[str] = Field(max_length=36)

    __table_args__ = (
        ForeignKeyConstraint(["head_item_key"], ["ix_head_title.item_key"]),
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
    )


class IxDefinitionLoc(IxLocsBase, table=True):
    """Class representing iXBRL definition location information"""

    __tablename__ = "ix_definition_loc"

    head_item_key: str = Field(default=None, max_length=36)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_href: Optional[str] = Field(default=None)
    source_file_id: Optional[str] = Field(max_length=36)

    __table_args__ = (
        Index("idx_ix_definition_loc_head_item_key", "head_item_key"),
        Index("idx_ix_definition_loc_source_file_id", "source_file_id"),
        Index("idx_ix_definition_loc_xlink_label", "xlink_label"),
        Index("idx_ix_definition_loc_attr_value", "attr_value"),
        Index("idx_ix_definition_loc_xlink_href", "xlink_href"),
        Index(
            "idx_ix_definition_loc_attr_value_xlink_label", "attr_value", "xlink_label"
        ),
        # UniqueConstraint(
        #     "head_item_key",
        #     "source_file_id",
        #     "xlink_label",
        #     "attr_value",
        #     name="ix_definition_loc_uc",
        # ),
        ForeignKeyConstraint(["head_item_key"], ["ix_head_title.item_key"]),
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
    )


class IxDefinitionArc(IxArcsBase, table=True):
    """Class representing iXBRL definition arc information"""

    __tablename__ = "ix_definition_arc"

    head_item_key: str = Field(default=None, max_length=36)
    xlink_to: str = Field(max_length=255)
    xlink_from: str = Field(max_length=255)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_order: Decimal = Field(sa_column=Column(DECIMAL(5, 2)))
    xlink_weight: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    source_file_id: Optional[str] = Field(max_length=36)

    __table_args__ = (
        Index("idx_ix_definition_arc_head_item_key", "head_item_key"),
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
            "head_item_key",
            "source_file_id",
            "xlink_from",
            "xlink_to",
            "xlink_arcrole",
            "attr_value",
            name="ix_definition_arc_uc",
        ),
        ForeignKeyConstraint(["head_item_key"], ["ix_head_title.item_key"]),
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
        # ForeignKeyConstraint(
        #     ["head_item_key", "source_file_id", "attr_value", "xlink_to"],
        #     [
        #         "ix_definition_loc.head_item_key",
        #         "ix_definition_loc.source_file_id",
        #         "ix_definition_loc.attr_value",
        #         "ix_definition_loc.xlink_label",
        #     ],
        # ),
        # ForeignKeyConstraint(
        #     ["head_item_key", "source_file_id", "attr_value", "xlink_from"],
        #     [
        #         "ix_definition_loc.head_item_key",
        #         "ix_definition_loc.source_file_id",
        #         "ix_definition_loc.attr_value",
        #         "ix_definition_loc.xlink_label",
        #     ],
        # ),
    )


class IxLabelLoc(IxLocsBase, table=True):
    """Class representing iXBRL label location information"""

    __tablename__ = "ix_label_loc"

    xlink_href: Optional[str] = Field(default=None)
    xlink_label: Optional[str] = Field(default=None)
    source_file_id: Optional[str] = Field(max_length=36)

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
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
    )


class IxLabelArc(IxArcsBase, table=True):
    """Class representing iXBRL label arc information"""

    __tablename__ = "ix_label_arc"

    source_file_id: Optional[str] = Field(max_length=36)

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
        Index("idx_ix_label_arc_xlink_from", "xlink_from"),
        Index("idx_ix_label_arc_xlink_to", "xlink_to"),
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
    )


class IxLabelValue(XbrlBase, table=True):
    """Class representing iXBRL label link information"""

    __tablename__ = "ix_label_value"

    xlink_type: Optional[str] = Field(max_length=255)
    xlink_label: Optional[str] = Field(default=None)
    xlink_role: Optional[str] = Field(max_length=255)
    xml_lang: Optional[str] = Field(max_length=255)
    label: str = Field(default=None)
    source_file_id: Optional[str] = Field(max_length=36)

    __table_args__ = (
        UniqueConstraint("xlink_label", "source_file_id", name="ix_label_value_uc"),
        Index("idx_ix_label_value_source_file_id", "source_file_id"),
        Index("idx_ix_label_value_xlink_label", "xlink_label"),
        Index("idx_ix_label_value_xlink_role", "xlink_role"),
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
    )


class IxNonFraction(XbrlBase, table=True):
    """Class representing iXBRL non-fraction information"""

    __tablename__ = "ix_non_fraction"

    head_item_key: str = Field(default=None, max_length=36)
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
    source_file_id: Optional[str] = Field(max_length=36)
    xbrl_type: Optional[str] = Field(max_length=2)
    display_numeric: Optional[str] = Field(default=None)
    display_scale: Optional[str] = Field(default=None)

    __table_args__ = (
        Index("idx_ix_non_fraction_head_item_key", "head_item_key"),
        Index("idx_ix_non_fraction_name", "name"),
        Index("idx_ix_non_fraction_xbrl_type", "xbrl_type"),
        Index("idx_ix_non_fraction_context", "context"),
        Index("idx_ix_non_fraction_report_type", "report_type"),
        ForeignKeyConstraint(["head_item_key"], ["ix_head_title.item_key"]),
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
    )

    __str__ = "ix_non_fraction"


class IxNonNumeric(XbrlBase, table=True):
    """Class representing iXBRL non-numeric information"""

    __tablename__ = "ix_non_numeric"

    head_item_key: str = Field(default=None, max_length=36)
    context: str = Field(default=None)
    name: str = Field(default=None)
    xsi_nil: Optional[bool] = Field(default=None)
    escape: Optional[bool] = Field(default=False)
    format: Optional[str] = Field(max_length=255)
    value: Optional[str] = Field(default=None)
    report_type: Optional[str] = Field(max_length=4)
    ixbrl_role: Optional[str] = Field(max_length=255)
    source_file_id: Optional[str] = Field(max_length=36)
    xbrl_type: Optional[str] = Field(max_length=2)

    __table_args__ = (
        Index("idx_ix_non_numeric_head_item_key", "head_item_key"),
        Index("idx_ix_non_numeric_name", "name"),
        Index("idx_ix_non_numeric_xbrl_type", "xbrl_type"),
        Index("idx_ix_non_numeric_context", "context"),
        Index("idx_ix_non_numeric_report_type", "report_type"),
        ForeignKeyConstraint(["head_item_key"], ["ix_head_title.item_key"]),
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
    )

    __str__ = "ix_non_numeric"


class IxPresentationLoc(IxLocsBase, table=True):
    """Class representing iXBRL presentation label location information"""

    __tablename__ = "ix_presentation_loc"

    head_item_key: str = Field(default=None, max_length=36)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_href: Optional[str] = Field(default=None)
    source_file_id: Optional[str] = Field(max_length=36)

    __table_args__ = (
        ForeignKeyConstraint(["head_item_key"], ["ix_head_title.item_key"]),
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
    )


class IxPresentationArc(IxArcsBase, table=True):
    """Class representing iXBRL presentation label arc information"""

    __tablename__ = "ix_presentation_arc"

    head_item_key: str = Field(default=None, max_length=36)
    attr_value: Optional[str] = Field(max_length=255)
    xlink_order: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    xlink_weight: Optional[Decimal] = Field(
        default=None, sa_column=Column(DECIMAL(5, 2))
    )
    source_file_id: Optional[str] = Field(max_length=36)

    __table_args__ = (
        ForeignKeyConstraint(["head_item_key"], ["ix_head_title.item_key"]),
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
    )


class ScLinkBaseRef(XbrlBase, table=True):
    """Class representing iXBRL linkbase reference information"""

    __tablename__ = "ix_schema_linkbase"

    xlink_arcrole: Optional[str] = Field(max_length=255)
    xlink_href: Optional[str] = Field(max_length=255)
    xlink_role: Optional[str] = Field(max_length=255)
    xlink_type: Optional[str] = Field(max_length=255)
    source_file_id: Optional[str] = Field(max_length=36)
    head_item_key: str = Field(max_length=36, foreign_key="ix_head_title.item_key")
    xbrl_type: Optional[str] = Field(max_length=255)
    href_source_file_id: Optional[str] = Field(max_length=36)

    __table_args__ = (
        Index("idx_ix_schema_linkbase_head_item_key", "head_item_key"),
        Index("idx_ix_schema_linkbase_xbrl_type", "xbrl_type"),
        Index(
            "idx_ix_schema_linkbase_head_item_key_xlink_role",
            "head_item_key",
            "xlink_role",
        ),
        Index("idx_ix_schema_linkbase_href_source_file_id", "href_source_file_id"),
        ForeignKeyConstraint(["head_item_key"], ["ix_head_title.item_key"]),
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
    )


class IxQualitative(XbrlBase, table=True):
    """Class representing iXBRL qualitative information"""

    __tablename__ = "ix_qualitative"

    currentId: str = Field(default=None, max_length=36, description="ID", unique=True)
    parentId: Optional[str] = Field(default=None, max_length=36, description="親ID")
    type: Optional[str] = Field(default=None, max_length=255, description="種類")
    content: Optional[str] = Field(default=None, description="タイトル、本文")
    order: Optional[int] = Field(default=None, description="順序")
    head_item_key: str = Field(default=None, max_length=36, description="XBRL ID")
    source_file_id: Optional[str] = Field(
        default=None, max_length=36, description="ソースファイルID"
    )
    photo_url: Optional[str] = Field(default=None, description="画像URL")

    __table_args__ = (
        Index("idx_ix_qualitative_head_item_key", "head_item_key"),
        Index("idx_ix_qualitative_content", "content"),
        ForeignKeyConstraint(["head_item_key"], ["ix_head_title.item_key"]),
        ForeignKeyConstraint(["source_file_id"], ["ix_source_file.id"]),
    )


# endregion


# region StockInfo


class JpxStockInfoBase(SQLModel, table=False):
    """StockInfoの基底クラスです。

    Properties:
        id int: インスタンスのIDです。
        insert_date datetime: 挿入日時です。
        update_date datetime: 更新日時です。
    """

    id: Optional[int] = Field(
        default=None, primary_key=True, sa_column_kwargs={"comment": "ID"}
    )
    insert_date: datetime = Field(
        default_factory=datetime.now, sa_column_kwargs={"comment": "作成日時"}
    )
    update_date: datetime = Field(
        default_factory=datetime.now, sa_column_kwargs={"comment": "更新日時"}
    )


class JpxStockInfo(JpxStockInfoBase, table=True):
    """StockInfoの作成時のプロパティです。"""

    __tablename__ = "jpx_stock_info"

    input_date: str = Field(max_length=8, description="入力日")
    code: str = Field(max_length=5, description="証券コード", unique=True)
    name: str = Field(max_length=255, description="企業名")
    market_or_type: str = Field(max_length=255, description="市場・商品区分")
    industry_33_code: Optional[int] = Field(description="33業種コード")
    industry_33_name: Optional[str] = Field(max_length=255, description="33業種区分")
    industry_17_code: Optional[int] = Field(description="17業種コード")
    industry_17_name: Optional[str] = Field(max_length=255, description="17業種区分")
    scale_code: Optional[int] = Field(description="規模コード")
    scale_name: Optional[str] = Field(max_length=255, description="規模区分")

    __table_args__ = (
        Index("jpx_stock_info_market_or_type", "market_or_type"),
        Index("jpx_stock_info_industry_33_code", "industry_33_code"),
        Index("jpx_stock_info_industry_17_code", "industry_17_code"),
        Index("jpx_stock_info_scale_code", "scale_code"),
    )


# endregion
