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

    @allure.step('Check if data is correct')
    def check_deta_is_correct(self, response_json):
        assert 'id' in response_json, "Field 'id' not found in the response"
        assert 'info' in response_json, "Field 'info' not found in the response"
        assert 'tags' in response_json, "Field 'tags' not found in the response"
        assert 'text' in response_json, "Field 'text' not found in the response"
        assert 'updated_by' in response_json, "Field 'updated_by' not found in the response"
        assert 'url' in response_json, "Field 'url' not found in the response"
