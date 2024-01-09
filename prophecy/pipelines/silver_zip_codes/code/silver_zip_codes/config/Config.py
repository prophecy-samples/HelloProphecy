from silver_zip_codes.graph.SG_IgnoreBadZip.config.Config import SubgraphConfig as SG_IgnoreBadZip_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, SG_IgnoreBadZip: dict=None, **kwargs):
        self.spark = None
        self.update(SG_IgnoreBadZip)

    def update(self, SG_IgnoreBadZip: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.SG_IgnoreBadZip = self.get_config_object(
            prophecy_spark, 
            SG_IgnoreBadZip_Config(prophecy_spark = prophecy_spark), 
            SG_IgnoreBadZip, 
            SG_IgnoreBadZip_Config
        )
        pass
