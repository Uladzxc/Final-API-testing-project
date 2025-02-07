import requests
import allure


from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    def __init__(self, url=None, headers=None):
        self.url = url or self.url
        self.headers = headers or self.headers
        self.new_meme_id = None

    @allure.step('Create new meme using valid body')
    def create_new_meme_positive(self, body, headers=None, token=None):
        headers = headers or self.headers

        if token:
            headers['Authorization'] = f'{token}'

        self.response = requests.post(
            f'{self.url}/meme',
            json=body,
            headers=headers
        )
        self.response_json = self.response.json()
        self.new_meme_id = self.response_json['id']
        print(f'New meme ID is {self.new_meme_id}')
        return self.response

    @allure.step('Create new meme using invalid data in body')
    def create_new_meme_negative(self, body, headers=None, token=None):
        headers = headers if headers else self.headers

        if token:
            headers['Authorization'] = f'{token}'

        self.response = requests.post(
            f'{self.url}/meme',
            json=body,
            headers=headers
        )
        return self.response
