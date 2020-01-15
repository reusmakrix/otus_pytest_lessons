def test_dictionary_1_keys(get_dictionary_fixture):
    d = get_dictionary_fixture
    sorted(d.keys())
    assert d['a'] == 1


def test_dictionary_2_pop(get_dictionary_fixture):
    d = get_dictionary_fixture
    result = d.pop('c')
    assert result == 3


def test_dictionary_3_update(get_dictionary_fixture):
    d1 = get_dictionary_fixture
    d2 = {'f': 6}
    d1.update(d2)
    result = d1['f']
    assert result == 6


def test_dictionary_4_get(get_dictionary_fixture):
    d = get_dictionary_fixture
    result = d.get('d')
    assert result == 4


def test_dictionary_5_del_params(get_dictionary_fixture, dictionary_params_fixture):
    data = [11, 12, 13, 14]
    d1 = get_dictionary_fixture
    d2 = dictionary_params_fixture
    d1.update(d2)
    result = d2.get('g')
    success = False
    for num in data:
        if num == result:
            success = True
    assert success
