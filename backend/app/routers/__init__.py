"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import pipeline as router_pipeline
from app.routers import regulator as router_regulator
from app.routers import valve as router_valve
from app.routers import cathode as router_cathode
from app.routers import leak as router_leak
from app.routers import route as router_route
from app.routers import rush as router_rush
from app.routers import meter as router_meter
from app.routers import safetycheck as router_safetycheck
from app.routers import pipeage as router_pipeage
from app.routers import thirdparty as router_thirdparty
from app.routers import shutoff as router_shutoff
from app.routers import hazard as router_hazard
from app.routers import team as router_team
from app.routers import appliance as router_appliance
from app.routers import pressure as router_pressure
from app.routers import account as router_account
from app.routers import emergency as router_emergency

ROUTERS = [router_pipeline, router_regulator, router_valve, router_cathode, router_leak, router_route, router_rush, router_meter, router_safetycheck, router_pipeage, router_thirdparty, router_shutoff, router_hazard, router_team, router_appliance, router_pressure, router_account, router_emergency]
