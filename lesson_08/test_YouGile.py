from pages.PageObgect import PageObgect
import requests
api = PageObgect(
    "https://yougile.com/api-v2",
    "Bearer P8niqWZqPE2O0WuS35kPA-VdOQw28k9c6+NplD0RcyYRX-8IpU5NMw4b4OV5Tt9S"
    )


def test_create_projects():
    body = api.get_projects_list()
    len_befor = len(body["content"])
    title = "Создан новый проект"
    api.create_projects(title=title)
    body = api.get_projects_list()
    len_after = len(body["content"])
    assert len_after > len_befor


def test_negative_create_projects():
    title = ""
    result = api.create_projects(title=title)
    assert result['statusCode'] == 400


def test_get_projects_list():
    resp = api.get_projects_list()
    assert len(resp) > 0


def test_negative_get_projects_list():
    my_haders = {}
    my_haders[
        "Authorization"
        ] = ""
    result = requests.get(
        "https://yougile.com/api-v2"+'/projects',
            headers=my_haders
            )
    assert result.status_code == 401


def test_change_projects():
    title = "Обновлено название проекта"
    body = api.change_projects(title=title)
    result = body["id"]
    len = api.get_projects_list()
    len_after = len['content'][0]['id']
    assert result == len_after


def test_negative_change_projects():
    title = ""
    result = api.change_projects(title=title)
    assert result['statusCode'] == 400


def test_get_progect_id():
    result = api.get_project_id()
    body = api.get_projects_list()
    len_after = body["content"][0]
    assert result == len_after


def test_negative_get_progect_id():
    my_haders = {}
    my_haders[
        "Authorization"
        ] = "Bearer P8niqWZqPE2O0WuS35kPA-VdOQw28k9c6+NplD0RcyYRX-8IpU5NMw4b4OV5Tt9S"
    id_company = "5641351313513535531351"
    result = requests.get(
        "https://yougile.com/api-v2"+'/projects/'+id_company,
        headers=my_haders
        )
    assert result.status_code == 404