import requests


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {self.token}'}
        params = {'path': file_path, 'overwrite': 'true'}
        res = requests.get(url=url, headers=headers, params=params)
        href = res.json().get('href', ' ')
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return 'Файл успешно загружен'
        return 'Ошибка загрузки'


if __name__ == '__main__':

    path_to_file = 'files/file.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
