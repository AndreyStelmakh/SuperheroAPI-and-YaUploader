import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path: str, disk_file_path: str):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")

        with open(file_path, 'rb') as file:
            response = requests.put(href, data=file)
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    local_path_to_file = 'newsafr.xml'
    disk_file_path = 'test/netology.xml'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(local_path_to_file, disk_file_path)
