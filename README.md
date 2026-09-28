# 城市燃气管道巡检平台

面向燃气管道巡线、调压站运行、泄漏检测处置、第三方施工监护与停气复气作业的一体化管网运维后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 燃气管道 | `pipeline` | 燃气管道 | 管段编号、管道材质、管径 |
| 调压站 | `regulator` | 调压站 | 站号、调压方式、进口压力 |
| 阀门井 | `valve` | 阀门井 | 井号、阀门类型、阀门口径 |
| 阴极保护 | `cathode` | 阴极保护点 | 保护编号、保护方式、保护电位 |
| 泄漏检测 | `leak` | 泄漏检测记录 | 检测编号、检测方式、检测点位 |
| 巡检路线 | `route` | 巡检路线 | 路线编号、所属片区、路线长度 |
| 抢修作业 | `rush` | 抢修作业单 | 抢修单号、发生位置、泄漏等级 |
| 燃气表 | `meter` | 燃气表 | 表号、表具类型、计量量程 |
| 入户安检 | `safetycheck` | 入户安检单 | 安检单号、用户编号、安检项目 |
| 管龄评估 | `pipeage` | 管龄评估记录 | 评估编号、管段编号、管龄 |
| 第三方施工监护 | `thirdparty` | 第三方施工监护单 | 监护编号、施工项目、交叉管段 |
| 停气复气 | `shutoff` | 停气复气作业 | 作业编号、影响管段、影响户数 |
| 隐患整改 | `hazard` | 隐患整改单 | 整改编号、隐患部位、隐患类别 |
| 抢修队伍 | `team` | 抢修队伍 | 队伍编号、驻地片区、队伍人数 |
| 燃气具 | `appliance` | 燃气具 | 器具编号、器具类型、品牌型号 |
| 压力监测 | `pressure` | 压力监测记录 | 监测编号、监测点位、监测压力 |
| 用户开户 | `account` | 用气户 | 户号、用户名称、用气地址 |
| 应急演练 | `emergency` | 应急演练 | 演练编号、演练科目、参演队伍 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
