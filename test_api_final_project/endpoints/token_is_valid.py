import requests
import allure

from endpoints.endpoint import Endpoint


class CheckIfTokenIsValid(Endpoint):
    @allure.step('Check if user token is still valid')
    def check_if_token_is_valid(self, user_token=None, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/authorize/{user_token}',
            headers=headers
        )
        print(f'Token is still valid {user_token}')
        return self.response

