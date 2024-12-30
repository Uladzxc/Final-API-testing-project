import requests
import allure


from endpoints.endpoint import Endpoint

class PutTheMeme(Endpoint):
    @allure.step('Update the selected meme')
    def update_the_selected_meme(self, body, headers=None, token=None, meme_id=None):
        headers = headers if headers else self.headers

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
