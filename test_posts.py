import pytest
import json

'''断言返回列表长度大于0'''
def test_get_all_posts(api_client):
    response = api_client.get('posts')
    assert isinstance(response.json(), list)
    assert len(response.json())>0


def test_create_post(api_client):
    '''测试创建新文章，返回201且包含id字段'''
    new_post = {
        "title": "test",
        'body': 'hhhhha',
        'userId': 1,
    }
    '''向 /posts 发送 POST 请求，请求体为 new_post 字典'''
    response = api_client.post('posts',json=new_post)
    assert response.status_code == 201
    data = response.json()
    assert 'id' in data


