from prophecy.cb.server.base.ComponentBuilderBase import *
from pyspark.sql import *
from pyspark.sql.functions import *

from prophecy.cb.server.base import WorkflowContext
from prophecy.cb.server.base.datatypes import SInt, SString
from prophecy.cb.ui.uispec import *


class DPSparkInit(ComponentSpec):
    name: str = "DPSparkInit"
    category: str = "Custom"


    def optimizeCode(self) -> bool:
        return True


    @dataclass(frozen=True)
    class DPSparkInitProperties(ComponentProperties):
        my_property: SString = SString("default value of my property")
        isCustomOutputSchema: Optional[str] = "True"

    def dialog(self) -> Dialog:
        return Dialog("DPSparkInit")


    def validate(self, context: WorkflowContext, component: Component[DPSparkInitProperties]) -> List[Diagnostic]:
        return []


    def onChange(self, context: WorkflowContext, oldState: Component[DPSparkInitProperties], newState: Component[DPSparkInitProperties]) -> Component[DPSparkInitProperties]:
        return newState


    class DPSparkInitCode(ComponentCode):
        def __init__(self, newProps):
            self.props: DPSparkInit.DPSparkInitProperties = newProps


        def apply(self, spark: SparkSession):
            from sap_sf_dp_utils import (
            DPSparkSession,
            DPDataLakeServiceClient,
            utils as u,
            enums as en,
            DPLogger
            )
            import re

            DPSparkSession(spark).data_lake_runtime_config_builder().build()
            dp = DPDataLakeServiceClient(spark)
            logger = DPLogger(spark, "dp-spark")
            Config.update(dp = DPDataLakeServiceClient(spark),
            logger = DPLogger(spark, "dp-spark"))
            print(Config.libraries)

            return