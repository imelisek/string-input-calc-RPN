from src.calculator import calculate, is_number, is_action

def test_easy():
    assert 4 == calculate('2 + 2')

def test_priorities():
    assert 10 == calculate('2 + 2 * 2 ** 2')

def test_priorities2():
    assert 27 == calculate('6 / 2 * 3 ** 2')

def test_isnum_true():
    assert True == is_number('3')

def test_isnum_notanum():
    assert ValueError

def test_isnum_false():
    assert False == is_number('*')

def test_isact_true():
    assert True == is_action('-')

def test_isact_false():
    assert False == is_action('5')

def test_isact_notanaction():
    assert ValueError


