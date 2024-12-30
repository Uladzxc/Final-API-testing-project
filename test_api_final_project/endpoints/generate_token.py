import requests
import allure

from endpoints.endpoint import Endpoint


class GenerateUserToken(Endpoint):

    @allure.step('Generate new token')
    def generate_token(self, body=None, headers=None):
        headers = headers if headers else self.headers

        self.response = requests.post(
            f'{self.url}/authorize',
            json=body,
            headers=headers
        )
        self.response_json = self.response.json()
        self.user_token = self.response_json['token']
        return self.response_json
