def test_list_remove(get_list_fixture):
    l = get_list_fixture
    l.remove(3)
    result = True
    for num in l:
        if result:
            result = (num == 3)
    assert not result


def test_list_append(get_list_fixture):
    l = get_list_fixture
    l.append(11)
    result = False
    for num in l:
        if not result:
            result = (num == 11)
    assert result


def test_list_pop(get_list_fixture):
    l = get_list_fixture
    l.pop(4)
    result = True
    for num in l:
        if result:
            result = (num == 5)
    assert not result


def test_list_4_extend(get_list_fixture):
    l1 = get_list_fixture
    l2 = [11, 12, 13]
    l1.extend(l2)
    assert l1[7] == 13


def test_list_5_insert_params(get_list_fixture, list_params_fixture):
    l1 = get_list_fixture
    l2 = list_params_fixture
    l1.insert(0, l2)
    assert l1[0] == l2
