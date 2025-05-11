from typing import Dict, List, Optional

from app.models import IxHeadTitle, IxNonFraction, IxNonNumeric

from . import schema as sc


class SummaryItems:

    def __init__(
        self,
        head_item: Optional[IxHeadTitle] = None,
        attr_value: Optional[str] = None,
        tree_items: Optional[sc.TreeItemsList] = None,
        from_names: List[str] = None,
        parent_items: Optional[List[str]] = None,
        child_items: Optional[Dict[str, str]] = None,
        context_list: Optional[List[List[str]]] = None,
        ix_non_fractions: Optional[List[IxNonFraction]] = None,
        ix_non_numerics: Optional[List[IxNonNumeric]] = None,
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

    def get_head_item(self) -> Optional[IxHeadTitle]:
        return self.head_item

    def set_attr_value(self, attr_value: str):
        self.attr_value = attr_value

    def get_attr_value(self) -> Optional[str]:
        return self.attr_value

    def set_tree_items(self, tree_items: sc.TreeItemsList):
        self.tree_items = tree_items

    def get_tree_items(self) -> Optional[sc.TreeItemsList]:
        return self.tree_items

    def set_from_names(self, from_names: List[str]):
        self.from_names = from_names

    def get_from_names(self) -> Optional[List[str]]:
        return self.from_names

    def set_parent_items(self, parent_items: List[str]):
        self.parent_items = parent_items

    def get_parent_items(self) -> Optional[List[str]]:
        return self.parent_items

    def set_child_items(self, child_items: Dict[str, str]):
        self.child_items = child_items

    def get_child_items(self) -> Optional[Dict[str, str]]:
        return self.child_items

    def set_context_list(self, context_list: List[List[str]]):
        self.context_list = context_list

    def get_context_list(self) -> Optional[List[List[str]]]:
        return self.context_list

    def set_ix_non_fractions(self, ix_non_fractions: List[IxNonFraction]):
        self.ix_non_fractions = ix_non_fractions

    def get_ix_non_fractions(self) -> Optional[List[IxNonFraction]]:
        return self.ix_non_fractions

    def set_ix_non_numerics(self, ix_non_numerics: List[IxNonNumeric]):
        self.ix_non_numerics = ix_non_numerics

    def get_ix_non_numerics(self) -> Optional[List[IxNonNumeric]]:
        return self.ix_non_numerics
