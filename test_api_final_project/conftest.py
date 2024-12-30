import pytest

from endpoints.generate_token import GenerateUserToken
from endpoints.token_is_valid import CheckIfTokenIsValid
from endpoints.create_meme import CreateMeme
from endpoints.delete_the_meme import DeleteMeme
from endpoints.get_the_meme import GetMeme
from endpoints.get_all_memes import GetAllMemes
from endpoints.put_the_meme import PutTheMeme



@pytest.fixture()
def generate_new_user_token():
    return GenerateUserToken()

@pytest.fixture()
def check_user_token():
    return CheckIfTokenIsValid()

@pytest.fixture()
def create_new_meme():
    return CreateMeme()

@pytest.fixture()
def delete_the_meme():
    return DeleteMeme()

@pytest.fixture()
def get_the_meme():
    return GetMeme()

@pytest.fixture()
def get_all_memes():
    return GetAllMemes()

@pytest.fixture()
def put_the_meme():
    return PutTheMeme()