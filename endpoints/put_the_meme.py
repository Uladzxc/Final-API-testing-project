import requests
import allure


from endpoints.endpoint import Endpoint


class PutTheMeme(Endpoint):
    @allure.step('Update the selected meme using valid body')
    def update_the_selected_meme_positive(self, body, headers=None, token=None, meme_id=None):
        headers = headers or self.headers

        if token:
            headers['Authorization'] = f'{token}'

        self.response = requests.put(
            f'{self.url}/meme/{meme_id}',
            json=body,
            headers=headers
        )
        self.response_json = self.response.json()
        print(f'Selected meme is updated')
        return self.response_json

    @allure.step('Update the selected meme using invalid data body')
    def update_the_selected_meme_negative(self, body, headers=None, token=None, meme_id=None):
        headers = headers if headers else self.headers

        if token:
            headers['Authorization'] = f'{token}'

        self.response = requests.put(
            f'{self.url}/meme/{meme_id}',
            json=body,
            headers=headers
        )
        return self.response
