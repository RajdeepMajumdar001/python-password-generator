import string
import pytest
from main import generate_password,main
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
def test_sim_pass_allowed():
    password = generate_password("1")
    allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits
    assert all(c in allowed for c in password)
def test_complex_password_contains_only_allowed_characters():
    password = generate_password("2")

    allowed = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + string.punctuation
    )

    assert all(c in allowed for c in password)

def test_main_generates_sim_password(monkeypatch, capsys) :
       monkeypatch.setattr("builtins.input", lambda _:"1")

       main()
       captured = capsys.readouterr()
       assert "generated password:" in captured.out
def test_main_com_pass(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _:"2")
    main()
    captured = capsys.readouterr()
    assert "generated password:" in captured.out




