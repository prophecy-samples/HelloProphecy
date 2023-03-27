from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, source_table: str=None):
        self.spark = None
        self.update(source_table)

    def update(self, source_table: str="default_table"):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.source_table = source_table
        pass
