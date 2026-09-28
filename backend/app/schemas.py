"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class PipelineEntry(BaseModel):
    """燃气管道明细结构。"""

    field_0: str | None = None  # 管段编号
    field_1: str | None = None  # 管道材质
    field_2: str | None = None  # 管径
    field_3: str | None = None  # 设计压力
    field_4: str | None = None  # 敷设方式
    field_5: str | None = None  # 投运日期
    field_6: str | None = None  # 所属片区
    field_7: str | None = None  # 管段状态

class RegulatorEntry(BaseModel):
    """调压站明细结构。"""

    field_0: str | None = None  # 站号
    field_1: str | None = None  # 调压方式
    field_2: str | None = None  # 进口压力
    field_3: str | None = None  # 出口压力
    field_4: str | None = None  # 调压器型号
    field_5: str | None = None  # 所属片区
    field_6: str | None = None  # 上次保养日
    field_7: str | None = None  # 调压站状态

class ValveEntry(BaseModel):
    """阀门井明细结构。"""

    field_0: str | None = None  # 井号
    field_1: str | None = None  # 阀门类型
    field_2: str | None = None  # 阀门口径
    field_3: str | None = None  # 井室深度
    field_4: str | None = None  # 所在管段
    field_5: str | None = None  # 上次启闭日
    field_6: str | None = None  # 启闭情况
    field_7: str | None = None  # 阀门井状态

class CathodeEntry(BaseModel):
    """阴极保护点明细结构。"""

    field_0: str | None = None  # 保护编号
    field_1: str | None = None  # 保护方式
    field_2: str | None = None  # 保护电位
    field_3: str | None = None  # 通电点位置
    field_4: str | None = None  # 恒电位仪编号
    field_5: str | None = None  # 测试日期
    field_6: str | None = None  # 测试员
    field_7: str | None = None  # 保护状态

class LeakEntry(BaseModel):
    """泄漏检测记录明细结构。"""

    field_0: str | None = None  # 检测编号
    field_1: str | None = None  # 检测方式
    field_2: str | None = None  # 检测点位
    field_3: str | None = None  # 甲烷浓度
    field_4: str | None = None  # 检测日期
    field_5: str | None = None  # 检测人
    field_6: str | None = None  # 复检日期
    field_7: str | None = None  # 检测状态

class RouteEntry(BaseModel):
    """巡检路线明细结构。"""

    field_0: str | None = None  # 路线编号
    field_1: str | None = None  # 所属片区
    field_2: str | None = None  # 路线长度
    field_3: str | None = None  # 点位数
    field_4: str | None = None  # 巡检班组
    field_5: str | None = None  # 巡线员
    field_6: str | None = None  # 上次巡检日
    field_7: str | None = None  # 路线状态

class RushEntry(BaseModel):
    """抢修作业单明细结构。"""

    field_0: str | None = None  # 抢修单号
    field_1: str | None = None  # 发生位置
    field_2: str | None = None  # 泄漏等级
    field_3: str | None = None  # 影响户数
    field_4: str | None = None  # 抢修班组
    field_5: str | None = None  # 到场时间
    field_6: str | None = None  # 完成时间
    field_7: str | None = None  # 抢修状态

class MeterEntry(BaseModel):
    """燃气表明细结构。"""

    field_0: str | None = None  # 表号
    field_1: str | None = None  # 表具类型
    field_2: str | None = None  # 计量量程
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 所属用户
    field_5: str | None = None  # 上次校验日
    field_6: str | None = None  # 累计读数
    field_7: str | None = None  # 表具状态

class SafetycheckEntry(BaseModel):
    """入户安检单明细结构。"""

    field_0: str | None = None  # 安检单号
    field_1: str | None = None  # 用户编号
    field_2: str | None = None  # 安检项目
    field_3: str | None = None  # 隐患数量
    field_4: str | None = None  # 安检员
    field_5: str | None = None  # 安检日期
    field_6: str | None = None  # 复检期限
    field_7: str | None = None  # 安检状态

class PipeageEntry(BaseModel):
    """管龄评估记录明细结构。"""

    field_0: str | None = None  # 评估编号
    field_1: str | None = None  # 管段编号
    field_2: str | None = None  # 管龄
    field_3: str | None = None  # 老化等级
    field_4: str | None = None  # 剩余寿命
    field_5: str | None = None  # 评估方法
    field_6: str | None = None  # 评估人
    field_7: str | None = None  # 评估状态

class ThirdpartyEntry(BaseModel):
    """第三方施工监护单明细结构。"""

    field_0: str | None = None  # 监护编号
    field_1: str | None = None  # 施工项目
    field_2: str | None = None  # 交叉管段
    field_3: str | None = None  # 施工方式
    field_4: str | None = None  # 监护要求
    field_5: str | None = None  # 监护人员
    field_6: str | None = None  # 监护起止日
    field_7: str | None = None  # 监护状态

class ShutoffEntry(BaseModel):
    """停气复气作业明细结构。"""

    field_0: str | None = None  # 作业编号
    field_1: str | None = None  # 影响管段
    field_2: str | None = None  # 影响户数
    field_3: str | None = None  # 停气原因
    field_4: str | None = None  # 计划停气时间
    field_5: str | None = None  # 计划复气时间
    field_6: str | None = None  # 通知情况
    field_7: str | None = None  # 作业状态

class HazardEntry(BaseModel):
    """隐患整改单明细结构。"""

    field_0: str | None = None  # 整改编号
    field_1: str | None = None  # 隐患部位
    field_2: str | None = None  # 隐患类别
    field_3: str | None = None  # 隐患等级
    field_4: str | None = None  # 责任班组
    field_5: str | None = None  # 整改期限
    field_6: str | None = None  # 验收人
    field_7: str | None = None  # 整改状态

class TeamEntry(BaseModel):
    """抢修队伍明细结构。"""

    field_0: str | None = None  # 队伍编号
    field_1: str | None = None  # 驻地片区
    field_2: str | None = None  # 队伍人数
    field_3: str | None = None  # 装备配置
    field_4: str | None = None  # 值班队长
    field_5: str | None = None  # 联系方式
    field_6: str | None = None  # 响应时限
    field_7: str | None = None  # 队伍状态

class ApplianceEntry(BaseModel):
    """燃气具明细结构。"""

    field_0: str | None = None  # 器具编号
    field_1: str | None = None  # 器具类型
    field_2: str | None = None  # 品牌型号
    field_3: str | None = None  # 使用年限
    field_4: str | None = None  # 所属用户
    field_5: str | None = None  # 上次检查日
    field_6: str | None = None  # 判废年限
    field_7: str | None = None  # 器具状态

class PressureEntry(BaseModel):
    """压力监测记录明细结构。"""

    field_0: str | None = None  # 监测编号
    field_1: str | None = None  # 监测点位
    field_2: str | None = None  # 监测压力
    field_3: str | None = None  # 报警上限
    field_4: str | None = None  # 报警下限
    field_5: str | None = None  # 采集时间
    field_6: str | None = None  # 监测员
    field_7: str | None = None  # 监测状态

class AccountEntry(BaseModel):
    """用气户明细结构。"""

    field_0: str | None = None  # 户号
    field_1: str | None = None  # 用户名称
    field_2: str | None = None  # 用气地址
    field_3: str | None = None  # 用气性质
    field_4: str | None = None  # 报装容量
    field_5: str | None = None  # 开户日期
    field_6: str | None = None  # 所属片区
    field_7: str | None = None  # 用户状态

class EmergencyEntry(BaseModel):
    """应急演练明细结构。"""

    field_0: str | None = None  # 演练编号
    field_1: str | None = None  # 演练科目
    field_2: str | None = None  # 参演队伍
    field_3: str | None = None  # 演练地点
    field_4: str | None = None  # 计划日期
    field_5: str | None = None  # 演练指挥
    field_6: str | None = None  # 评估结论
    field_7: str | None = None  # 演练状态
