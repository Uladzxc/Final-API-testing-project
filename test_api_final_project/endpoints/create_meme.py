import requests
import allure


from endpoints.endpoint import Endpoint

class CreateMeme(Endpoint):
    @allure.step('Create new meme')
    def create_new_meme(self, body, headers=None, token=None):
        headers = headers if headers else self.headers

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
        return self.response_json
