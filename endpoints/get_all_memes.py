import requests
import allure

from endpoints.endpoint import Endpoint

class GetAllMemes(Endpoint):
    @allure.step('Get all memes')
    def get_the_selected_meme(self, body=None, headers=None, token=None):
        headers = headers if headers else self.headers

        if token:
            headers['Authorization'] = f'{token}'

        self.response = requests.get(
            f'{self.url}/meme',
            json=body,
            headers=headers
        )
        self.response_json = self.response.json()
        return self.response
