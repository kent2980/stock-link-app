from app.models import IxHeadTitle, IxNonFraction, IxNonNumeric

from . import schema as sc


class SummaryItems:
    def __init__(
        self,
        head_item: IxHeadTitle | None = None,
        attr_value: str | None = None,
        tree_items: sc.TreeItemsList | None = None,
        from_names: list[str] = None,
        parent_items: list[str] | None = None,
        child_items: dict[str, str] | None = None,
        context_list: list[list[str]] | None = None,
        ix_non_fractions: list[IxNonFraction] | None = None,
        ix_non_numerics: list[IxNonNumeric] | None = None,
    ):
        self.head_item = head_item
        self.attr_value = attr_value
        self.tree_items = tree_items
        self.from_names = from_names
        self.parent_items = parent_items
        self.child_items = child_items
        self.context_list = context_list
        self.ix_non_fractions = ix_non_fractions
        self.ix_non_numerics = ix_non_numerics

    def set_head_item(self, head_item: IxHeadTitle):
        self.head_item = head_item

    def get_head_item(self) -> IxHeadTitle | None:
        return self.head_item

    def set_attr_value(self, attr_value: str):
        self.attr_value = attr_value

    def get_attr_value(self) -> str | None:
        return self.attr_value

    def set_tree_items(self, tree_items: sc.TreeItemsList):
        self.tree_items = tree_items

    def get_tree_items(self) -> sc.TreeItemsList | None:
        return self.tree_items

    def set_from_names(self, from_names: list[str]):
        self.from_names = from_names

    def get_from_names(self) -> list[str] | None:
        return self.from_names

    def set_parent_items(self, parent_items: list[str]):
        self.parent_items = parent_items

    def get_parent_items(self) -> list[str] | None:
        return self.parent_items

    def set_child_items(self, child_items: dict[str, str]):
        self.child_items = child_items

    def get_child_items(self) -> dict[str, str] | None:
        return self.child_items

    def set_context_list(self, context_list: list[list[str]]):
        self.context_list = context_list

    def get_context_list(self) -> list[list[str]] | None:
        return self.context_list

    def set_ix_non_fractions(self, ix_non_fractions: list[IxNonFraction]):
        self.ix_non_fractions = ix_non_fractions

    def get_ix_non_fractions(self) -> list[IxNonFraction] | None:
        return self.ix_non_fractions

    def set_ix_non_numerics(self, ix_non_numerics: list[IxNonNumeric]):
        self.ix_non_numerics = ix_non_numerics

    def get_ix_non_numerics(self) -> list[IxNonNumeric] | None:
        return self.ix_non_numerics
