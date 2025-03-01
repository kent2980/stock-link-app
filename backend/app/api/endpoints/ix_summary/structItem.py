from . import schema as sc


class StructItem:
    period: sc.PeriodSchemaBase
    structs: sc.FinStructBase

    def __init__(self, period: sc.PeriodSchemaBase, structs: sc.FinStructBase):
        self._period = period
        self._structs = structs

    @property
    def period(self) -> sc.PeriodSchemaBase:
        return self._period

    @period.setter
    def period(self, value: sc.PeriodSchemaBase):
        self._period = value

    @property
    def structs(self) -> sc.FinStructBase:
        return self._structs

    @structs.setter
    def structs(self, value: sc.FinStructBase):
        self._structs = value
