from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, source_table: str=None, **kwargs):
        self.spark = None
        self.update(source_table)

    def update(self, source_table: str="default_table", **kwargs):
        prophecy_spark = self.spark
        self.source_table = source_table
        pass
