import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    """整个测试会话只创建一次APIClient"""
    return APIClient()

@pytest.fixture
def sample_todo_data():
    """示例任务数据，每个测试用例独立"""
    return {
        "userId": 1,
        "title": "learn pytest",
        "completed": False
    }

