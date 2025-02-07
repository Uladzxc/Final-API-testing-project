import requests
import allure


from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):
    @allure.step('Get the meme')
    def get_the_selected_meme(self, body=None, headers=None, token=None, meme_id=None):
        headers = headers or self.headers

        if token:
            headers['Authorization'] = f'{token}'

        self.response = requests.get(
            f'{self.url}/meme/{meme_id}',
            json=body,
            headers=headers
        )
        if self.response.text.strip():
            try:
                self.response_json = self.response.json()
            except requests.JSONDecodeError:
                self.response_json = None
        else:
            self.response_json = None
        return self.response
