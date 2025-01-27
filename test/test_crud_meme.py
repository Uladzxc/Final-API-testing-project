positive_test_data = {
        "text": "new_meme_28_12",
        "url": "https://i.imgflip.com/8zktbc.jpg",
        "tags": ["fun", "olympic"],
        "info": {
            "colors": [
                "blue",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        }
    }

negative_test_data = {
        "url": "https://i.imgflip.com/8zktbc.jpg",
        "tags": ["fun", "olympic"],
        "info": {
            "colors": [
                "blue",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        }
    }


def test_user_authorization(generate_new_user_token):
    generate_new_user_token.generate_token(body={"name": "TestUser"})
    generate_new_user_token.check_response_status_is_200()

    assert 'token' in generate_new_user_token.response_json, "Field 'token' not found in the response"
    assert 'user' in generate_new_user_token.response_json, "Field 'token' not found in the response"


def test_if_token_is_valid(check_user_token, generate_new_user_token):
    token_data = generate_new_user_token.generate_token(body={"name": "TestUser"})
    response = check_user_token.check_if_token_is_valid(user_token=token_data['token'])
    check_user_token.check_response_status_is_200()

    check_user_token.check_if_validation_appears(
        response, message_text=f'Token is alive. Username is {token_data["user"]}'
    )


def test_get_all_memes(token_validation, get_all_memes):
    token = token_validation()

    get_all_memes.get_the_selected_meme(token=token)
    get_all_memes.check_response_status_is_200()

    assert 'data' in get_all_memes.response_json, "'data' is missing in response"


def test_create_new_meme_positive(token_validation, create_new_meme, delete_the_meme):
    token = token_validation()

    create_new_meme.create_new_meme_positive(body=positive_test_data, token=token)
    create_new_meme.check_response_status_is_200()

    response_json = create_new_meme.response_json
    create_new_meme.check_data_is_correct(response_json)
    create_new_meme.check_data_matches_the_test_data(positive_test_data, response_json)

    delete_the_meme.delete_the_selected_meme(meme_id=create_new_meme.new_meme_id, token=token)
    delete_the_meme.check_response_status_is_200()


def test_get_the_meme(token_validation, get_the_meme, create_and_delete_the_meme):
    token = token_validation()

    get_the_meme.get_the_selected_meme(meme_id=create_and_delete_the_meme, token=token)
    get_the_meme.check_response_status_is_200()

    response_json = get_the_meme.response_json
    get_the_meme.check_data_is_correct(response_json)


def test_delete_the_meme(token_validation, create_and_delete_the_meme, delete_the_meme):
    token = token_validation()

    response = delete_the_meme.delete_the_selected_meme(meme_id=create_and_delete_the_meme, token=token)
    delete_the_meme.check_response_status_is_200()

    assert f'Meme with id {create_and_delete_the_meme} successfully deleted' in response.text


def test_update_the_meme(token_validation, create_and_delete_the_meme, put_the_meme):
    token = token_validation()

    updated_data = {
        "id": create_and_delete_the_meme,
        "text": "UPD_new_meme_28_12",
        "url": "https://i.imgflip.com/8zktbc.jpg",
        "tags": ["fun", "olympic"],
        "info": {
            "colors": [
                "blue",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        }
    }

    put_the_meme.update_the_selected_meme_positive(meme_id=create_and_delete_the_meme, body=updated_data, token=token)
    put_the_meme.check_response_status_is_200()

    response_json = put_the_meme.response_json
    put_the_meme.check_data_is_correct(response_json)
    put_the_meme.check_data_matches_the_test_data(updated_data, response_json)

    assert updated_data['text'] in response_json['text']


def test_create_new_meme_negative(token_validation, create_new_meme):
    token = token_validation()

    response = create_new_meme.create_new_meme_negative(body=negative_test_data, token=token)
    create_new_meme.check_response_status_is_400()

    create_new_meme.check_if_validation_appears(response, message_text='Invalid parameters')


def test_delete_the_non_existent_meme(token_validation, delete_the_meme):
    token = token_validation()

    response = delete_the_meme.delete_the_selected_meme(meme_id=99999999, token=token)
    delete_the_meme.check_response_status_is_404()

    delete_the_meme.check_if_validation_appears(
        response, message_text='The requested URL was not found on the server. '
                               'If you entered the URL manually please check your spelling and try again.'
    )


def test_update_the_meme_negative(token_validation, create_and_delete_the_meme, put_the_meme):
    token = token_validation()

    updated_data = {
        "id": create_and_delete_the_meme,
        "text": "UPD_new_meme_28_12",
        "tags": ["fun", "olympic"],
        "info": {
            "colors": [
                "blue",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        }
    }

    response = put_the_meme.update_the_selected_meme_negative(
        meme_id=create_and_delete_the_meme, body=updated_data, token=token
    )
    put_the_meme.check_response_status_is_400()

    put_the_meme.check_if_validation_appears(response, message_text='Invalid parameters')
