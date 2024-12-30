TEST_DATA = {
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


def test_get_all_memes(generate_new_user_token, check_user_token, get_all_memes):
    new_user_token = (generate_new_user_token.generate_token(body = {"name": "TestUser"})).get('token')
    generate_new_user_token.check_response_status_is_200()

    get_all_memes.get_the_selected_meme(token=new_user_token)
    get_all_memes.check_response_status_is_200()

def test_create_new_meme(generate_new_user_token, check_user_token, create_new_meme, delete_the_meme):
    new_user_token = (generate_new_user_token.generate_token(body = {"name": "TestUser"})).get('token')
    generate_new_user_token.check_response_status_is_200()

    create_new_meme.create_new_meme(body=TEST_DATA, token=new_user_token)
    create_new_meme.check_response_status_is_200()

    delete_the_meme.delete_the_selected_meme(meme_id=create_new_meme.new_meme_id, token=new_user_token)
    delete_the_meme.check_response_status_is_200()

def test_get_the_meme(generate_new_user_token, check_user_token, create_new_meme, get_the_meme, delete_the_meme):
    new_user_token = (generate_new_user_token.generate_token(body = {"name": "TestUser"})).get('token')
    generate_new_user_token.check_response_status_is_200()

    create_new_meme.create_new_meme(body=TEST_DATA, token=new_user_token)
    create_new_meme.check_response_status_is_200()

    get_the_meme.get_the_selected_meme(meme_id=create_new_meme.new_meme_id, token=new_user_token)
    get_the_meme.check_response_status_is_200()

    delete_the_meme.delete_the_selected_meme(meme_id=create_new_meme.new_meme_id, token=new_user_token)
    delete_the_meme.check_response_status_is_200()

def test_delete_the_meme(generate_new_user_token, check_user_token, create_new_meme, delete_the_meme):
    new_user_token = (generate_new_user_token.generate_token(body = {"name": "TestUser"})).get('token')
    generate_new_user_token.check_response_status_is_200()

    create_new_meme.create_new_meme(body=TEST_DATA, token=new_user_token)
    create_new_meme.check_response_status_is_200()

    delete_the_meme.delete_the_selected_meme(meme_id=create_new_meme.new_meme_id, token=new_user_token)
    delete_the_meme.check_response_status_is_200()

def test_update_the_meme(generate_new_user_token, check_user_token, create_new_meme, put_the_meme, delete_the_meme):
    new_user_token = (generate_new_user_token.generate_token(body = {"name": "TestUser"})).get('token')
    generate_new_user_token.check_response_status_is_200()

    create_new_meme.create_new_meme(body=TEST_DATA, token=new_user_token)
    create_new_meme.check_response_status_is_200()

    UPDATED_DATA = {
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

    put_the_meme.update_the_selected_meme(meme_id=create_new_meme.new_meme_id, body=UPDATED_DATA, token=new_user_token)
    put_the_meme.check_response_status_is_200()

    delete_the_meme.delete_the_selected_meme(meme_id=create_new_meme.new_meme_id, token=new_user_token)
    delete_the_meme.check_response_status_is_200()

