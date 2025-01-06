test_data = {
        "text": "new_meme_28_12",
        "url": "https://i.imgflip.com/8zktbc.jpg",
        "tags": [ "fun", "olympic"],
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


def test_get_all_memes(token_validation, get_all_memes):
    token=token_validation()

    get_all_memes.get_the_selected_meme(token=token)
    get_all_memes.check_response_status_is_200()

def test_create_new_meme(token_validation, create_new_meme, delete_the_meme):
    token=token_validation()

    create_new_meme.create_new_meme(body=test_data, token=token)
    create_new_meme.check_response_status_is_200()

    delete_the_meme.delete_the_selected_meme(meme_id=create_new_meme.new_meme_id, token=token)
    delete_the_meme.check_response_status_is_200()

def test_get_the_meme(token_validation, create_new_meme, get_the_meme, delete_the_meme):
    token=token_validation()

    create_new_meme.create_new_meme(body=test_data, token=token)
    create_new_meme.check_response_status_is_200()

    get_the_meme.get_the_selected_meme(meme_id=create_new_meme.new_meme_id, token=token)
    get_the_meme.check_response_status_is_200()

    delete_the_meme.delete_the_selected_meme(meme_id=create_new_meme.new_meme_id, token=token)
    delete_the_meme.check_response_status_is_200()

def test_delete_the_meme(token_validation, create_new_meme, delete_the_meme):
    token=token_validation()

    create_new_meme.create_new_meme(body=test_data, token=token)
    create_new_meme.check_response_status_is_200()

    delete_the_meme.delete_the_selected_meme(meme_id=create_new_meme.new_meme_id, token=token)
    delete_the_meme.check_response_status_is_200()

def test_update_the_meme(token_validation, create_new_meme, put_the_meme, delete_the_meme):
    token=token_validation()

    create_new_meme.create_new_meme(body=test_data, token=token)
    create_new_meme.check_response_status_is_200()

    updated_data = {
        "id": create_new_meme.new_meme_id,
        "text": "UPD_new_meme_28_12",
        "url": "https://i.imgflip.com/8zktbc.jpg",
        "tags": [ "fun", "olympic"],
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

    put_the_meme.update_the_selected_meme(meme_id=create_new_meme.new_meme_id, body=updated_data, token=token)
    put_the_meme.check_response_status_is_200()

    delete_the_meme.delete_the_selected_meme(meme_id=create_new_meme.new_meme_id, token=token)
    delete_the_meme.check_response_status_is_200()
