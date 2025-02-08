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
    def check_data_is_correct(self, response_json):
        assert 'id' in response_json, "Field 'id' not found in the response"
        assert 'info' in response_json, "Field 'info' not found in the response"
        assert 'tags' in response_json, "Field 'tags' not found in the response"
        assert 'text' in response_json, "Field 'text' not found in the response"
        assert 'updated_by' in response_json, "Field 'updated_by' not found in the response"
        assert 'url' in response_json, "Field 'url' not found in the response"

    @allure.step('Check if the response data is equal to request data')
    def check_data_matches_the_test_data(self, test_data, response_json):
        assert test_data['info'] == response_json['info'], "Field 'info' not found in the response"
        assert test_data['tags'] == response_json['tags'], "Field 'tags' not found in the response"
        assert test_data['text'] == response_json['text'], "Field 'text' not found in the response"
        assert test_data['url'] == response_json['url'], "Field 'url' not found in the response"

    @allure.step('Check if validation message returns')
    def check_if_validation_appears(self, response, message_text):
        assert message_text in response.text

    @allure.step('Check if response has selected data')
    def check_if_response_has_selected_data(self, field_name, response_json, error_message):
        assert field_name in response_json, error_message

    @allure.step('Check if response has selected meme')
    def check_if_response_has_selected_meme(self, meme_id):
        assert 'id' in self.response_json, "Field 'id' not found in the response"
        response_id = self.response_json['id']
        assert meme_id == response_id, f"Expected meme_id={meme_id}, but got response_id={response_id}"
