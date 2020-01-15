import pytest


@pytest.fixture()
def list_params_fixture():
    pass


@pytest.fixture()
def set_params_fixture():
    pass


@pytest.fixture()
def dictionary_params_fixture():
    pass


@pytest.fixture()
def string_params_fixture():
    pass


@pytest.fixture()
def get_string_fixture():
    return "test_string"


@pytest.fixture()
def get_list_fixture():
    return [1, 2, 3, 4, 5]


@pytest.fixture()
def get_dictionary_fixture():
    return {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


@pytest.fixture()
def get_set_fixture():
    return {'a', 'b', 'c', 'd', 'e'}
