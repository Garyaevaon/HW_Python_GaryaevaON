import requests


class PageObgect:

    def __init__(self, url, key):
        self.url = url
        self.key = key

    def get_projects_list(self):
        my_haders = {}
        my_haders[
            "Authorization"
            ] = self.key
        resp = requests.get(
            self.url+'/projects',
            headers=my_haders
            )
        return resp.json()

    def create_projects(self, title=''):
        projects = {
            "title": title,
            "users": {"5577deb0-088a-4459-a907-c4b856040740": "admin"}
            }
        my_haders = {}
        my_haders[
            "Authorization"
            ] = self.key
        resp = requests.post(
            self.url+'/projects',
            json=projects,
            headers=my_haders
            )
        return resp.json()

    def change_projects(self, title=''):
        change = {
            "title": title
            }
        my_haders = {}
        my_haders[
            "Authorization"
            ] = self.key
        result = self.get_projects_list()
        id_company = result['content'][0]['id']
        resp = requests.put(
            self.url+'/projects/'+id_company,
            json=change,
            headers=my_haders
            )
        return resp.json()

    def get_project_id(self):
        my_haders = {}
        my_haders[
            "Authorization"
            ] = self.key
        body = self.get_projects_list()
        id_company = body['content'][0]['id']
        data = requests.get(
            self.url+'/projects/'+id_company,
            headers=my_haders
            )
        return data.json()
