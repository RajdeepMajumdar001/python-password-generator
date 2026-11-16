import string
import pytest
from main import generate_password
def test_simple_password_length():
    password = generate_password("1")
    assert len(password) == 8
def test_complex_password_length():
    password = generate_password("2")
    assert len(password) == 12
def test_sim_pass_all_char():
    password = generate_password("1")
    assert any(c in string .ascii_uppercase for c in password)
    assert any(c in string.ascii_lowercase for c in password)
    assert any(c in string.digits for c in password)
def test_com_pass_pass():
    password= generate_password("2")
    assert any(c in string.ascii_uppercase for c in password)
    assert any(c in string.ascii_lowercase for c in password)
    assert any(c in string.digits for c in password)
    assert any(c in string.punctuation for c in password)
def test_in_ch():
    with pytest.raises(ValueError):
        generate_password("3")