from cleanup_data.graph.CleanupSubgraph.config.Config import SubgraphConfig as CleanupSubgraph_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, CleanupSubgraph: dict=None, **kwargs):
        self.spark = None
        self.update(CleanupSubgraph)

    def update(self, CleanupSubgraph: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.CleanupSubgraph = self.get_config_object(
            prophecy_spark, 
            CleanupSubgraph_Config(prophecy_spark = prophecy_spark), 
            CleanupSubgraph, 
            CleanupSubgraph_Config
        )
        pass
