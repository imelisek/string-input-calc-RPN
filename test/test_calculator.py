from src.calculator import calculate, is_number, is_action, is_unary
import pytest
from pytest import approx

def test_easy():
    assert 4 == calculate('2 + 2')

def test_complex():
    assert 1.5 == calculate('2 * 2 + -2.5')

def test_wrong_value():
    with pytest.raises(ValueError):
        calculate('letter')

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        calculate('8 / 0')

def test_priorities():
    assert 10 == calculate('2 + 2 * 2 ** 2')

def test_aprox2():
    assert approx(0.00495) == calculate('495 / 1000 / 100')

def test_parenthesized_expr():
    assert 12 == calculate('( 2 + 8 / 2 ) * 2')

def test_unary_expr_easy():
    assert approx(0.5) == calculate('sin 30')

def test_unary_expr_complex():
    assert 4.5 == calculate('2 + sin ( 15 + 5 * 3 ) + 2')

def test_factorial():
    assert approx(64) == calculate('2 + 5 ! * sin ( 15 + 5 * 3 ) + 2')  

def test_hyperfunc():
    assert approx(0.2766) == calculate('-2.5 + sh 100')  

def test_isnum_true():
    assert True == is_number('8')

def test_num_negative():
    assert True == is_number('-8')

def test_float_point_num():
    assert True == is_number('2.5')

def test_float_negative():
    assert True == is_number('-2.1')

def test_isnum_notanum():
    assert False == is_number('letter')
   
def test_isnum_false():
    assert False == is_number('*')

def test_isact_true():
    assert True == is_action('-')

def test_isact_false():
    assert False == is_action('5')

def test_isact_notanaction():
   assert False == is_action('letter')

def test_isunary_true():
    assert True == is_unary('cos')

def test_isunary_false():
    assert False == is_unary('5')

def test_isunary_notanaction():
   assert False == is_unary('letter')





