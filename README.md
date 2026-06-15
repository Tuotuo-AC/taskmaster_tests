# TaskMaster API 自动化测试

基于 `pytest` + `requests` 的接口自动化测试项目，用于演示如何对 RESTful API 进行功能测试、数据驱动测试、报告生成及 CI 集成。

## 📋 项目简介

本项目以 JSONPlaceholder 提供的 `/todos` API 作为被测对象，覆盖了典型的 CRUD 操作（增、删、改、查），并包含：

- 正向/异常场景测试
- 参数化测试
- 数据驱动测试（JSON 外部数据）
- 测试报告生成（HTML / Allure）
- GitHub Actions 持续集成

## 🛠️ 技术栈

- Python 3.11+
- pytest – 测试框架
- requests – HTTP 客户端
- pytest-html – HTML 报告插件
- allure-pytest – Allure 报告插件
- GitHub Actions – CI/CD 自动执行

## 📁 项目结构

```markdown
taskmaster_tests/
├── .github/workflows/        # CI 配置文件
│   └── test.yml
├── utils/                    # 工具模块
│   └── api_client.py         # API 客户端封装
├── data/                     # 测试数据
│   └── test_data.json
├── conftest.py               # pytest  fixtures 定义
├── config.py                 # 配置（BASE_URL 等）
├── test_todos.py             # 测试用例
├── requirements.txt          # 依赖清单
├── .gitignore                # Git 忽略文件
└── README.md                 # 本文件
```

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/Tuotuo-AC/taskmaster_tests.git
cd taskmaster_tests
```

### 2. 创建虚拟环境并激活

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

如果还没有 `requirements.txt`，可以手动创建并写入：

```
pytest
requests
pytest-xdist
allure-pytest
pytest-html
```

### 4. 运行测试

```bash
pytest test_todos.py -v
```

所有测试都应该通过（8 passed）。

## 📊 生成测试报告

### HTML 报告

```bash
pip install pytest-html
pytest test_todos.py --html=report.html --self-contained-html
```

打开 `report.html` 即可。

### Allure 报告（更美观）

1. **安装 Allure 命令行工具（[下载地址](https://github.com/allure-framework/allure2/releases)）并加入 PATH。**
2. **运行测试生成原始数据：**

```bash
pytest test_todos.py --alluredir=./reports
```

3. **生成并查看报告**：

```bash
allure serve ./reports
```

浏览器会自动打开一个本地服务，展示交互式报告。

## 🔁 持续集成（GitHub Actions）

项目已配置 `.github/workflows/test.yml`，每当推送代码或发起 Pull Request 时，GitHub 会自动运行测试。

只需要：

- 将项目推送到 GitHub 仓库
- 进入仓库的 `Actions` 标签页查看运行结果

## 🧪 测试场景说明

| 测试函数                         | 覆盖场景                         |
| -------------------------------- | -------------------------------- |
| `test_get_all_todos`             | 获取所有任务，验证返回列表及长度 |
| `test_get_single_todo`           | 根据 ID 获取单个任务             |
| `test_get_todo_not_found`        | 获取不存在的任务（返回空对象）   |
| `test_create_todo`               | 创建新任务                       |
| `test_create_todo_missing_field` | 缺少必填字段时的处理（参数化）   |
| `test_update_todo`               | 全量更新任务                     |
| `test_delete_todo`               | 删除任务（模拟返回 200）         |

> 注：JSONPlaceholder 为 Mock API，删除和更新不会真正修改数据，但响应结构和状态码符合 REST 规范，适合教学。

