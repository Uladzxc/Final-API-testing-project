import requests
import allure


from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    @allure.step('Delete the meme')
    def delete_the_selected_meme(self, body=None, headers=None, token=None, meme_id=None):
        headers = headers or self.headers

        if token:
            headers['Authorization'] = f'{token}'

        self.response = requests.delete(
            f'{self.url}/meme/{meme_id}',
            json=body,
            headers=headers
        )
        return self.response
