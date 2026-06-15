# 覆盖正向、异常、边界场景
import pytest
import json
from test_todos import *

def test_get_all_todos(api_client):
    """测试获取所有任务：状态码200，返回列表"""
    response = api_client.get("todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    # 默认返回200条记录
    assert len(response.json()) == 200

def test_get_single_todo(api_client):
    """测试获取单个任务：存在情况"""
    todo_id = 1
    response = api_client.get(f"todos/{todo_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == todo_id
    assert "title" in data

def test_get_todo_not_found(api_client):
    """测试获取不存在的任务：404"""
    response = api_client.get("todos/99999")
    assert response.status_code == 404

def test_create_todo(api_client, sample_todo_data):
    """测试创建任务：返回201及数据匹配"""
    response = api_client.post("todos", json=sample_todo_data)
    assert response.status_code == 201
    created = response.json()
    # Mock API会返回id=201（新ID），且内容一致
    assert created["title"] == sample_todo_data["title"]
    assert created["userId"] == sample_todo_data["userId"]
    assert "id" in created

@pytest.mark.parametrize("missing_field", ["title", "userId"])
def test_create_todo_missing_field(api_client, missing_field):
    """参数化测试：缺少必填字段时的行为"""
    incomplete_data = {"completed": False}
    response = api_client.post("todos", json=incomplete_data)
    # Mock API 对缺失字段依然会返回201（因为是模拟），但实际项目中应返回400
    # 这里主要演示参数化写法，你可以根据真实项目调整预期
    assert response.status_code in [201, 400]

def test_update_todo(api_client):
    """测试全量更新"""
    todo_id = 1
    updated_data = {
        "userId": 1,
        "title": "updated title",
        "completed": True
    }
    response = api_client.put(f"todos/{todo_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "updated title"

def test_delete_todo(api_client):
    """测试删除"""
    todo_id = 1
    response = api_client.delete(f"todos/{todo_id}")
    assert response.status_code == 200
    # 注意：JSONPlaceholder实际不会删除数据，但返回200代表请求有效


@pytest.mark.parametrize("test_case", json.load(open("data/test_data.json")))
def test_todo_by_user_id(api_client, test_case):
    response = api_client.get("todos", params={"userId": test_case["user_id"]})
    assert response.status_code == 200
    todos = response.json()
    assert any(todo["title"] == test_case["expected_title"] for todo in todos)