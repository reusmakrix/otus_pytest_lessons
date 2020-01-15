import pytest


@pytest.fixture(params=[11, 12, 13, 14])
def list_params_fixture(request):
    return request.param


@pytest.fixture(params=[11, 12, 13, 14])
def set_params_fixture(request):
    return request.param


@pytest.fixture(params=[{'g': 11}, {'g': 12}, {'g': 13}, {'g': 14}])
def dictionary_params_fixture(request):
    return request.param


@pytest.fixture(params=[11, 12, 13, 14])
def string_params_fixture(request):
    return request.param

@pytest.fixture()
def get_string_fixture():
    return "test_string"


@pytest.fixture()
def get_list_fixture():
    return [1, 2, 3, 4, 5]


@pytest.fixture()
def get_dictionary_fixture():
    return {'e': 5, 'c': 3, 'b': 2, 'd': 4, 'a': 1}


@pytest.fixture()
def get_set_fixture():
    return {'a', 'b', 'c', 'd', 'e'}
