import allure

class Endpoint:
    url = 'http://167.172.172.115:52355/'
    response = None
    response_json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that response is 200')
    def check_response_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that response is 404')
    def check_response_status_is_404(self):
        assert self.response.status_code == 404

    @allure.step('Check that response is 400')
    def check_response_status_is_400(self):
        assert self.response.status_code == 400
