import pytest

# def test_check_if_token_is_still_valid(generate_new_user_token, check_user_token):
#     generate_new_user_token.generate_token(body = {"name": "TestUser"})
#     generate_new_user_token.check_response_status_is_200()
#     check_user_token.check_if_token_is_valid(user_token=generate_new_user_token.user_token)
#     check_user_token.check_response_status_is_200()

TEST_DATA = [
    {
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
]

def test_create_new_meme(generate_new_user_token, check_user_token, create_new_meme):
    new_user_token = (generate_new_user_token.generate_token(body = {"name": "TestUser"})).get('token')
    print(new_user_token)
    generate_new_user_token.check_response_status_is_200()
    create_new_meme.create_new_meme(body=TEST_DATA, token=new_user_token)
    create_new_meme.check_response_status_is_200()


