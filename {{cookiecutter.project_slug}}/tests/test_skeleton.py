import pytest

from {{ cookiecutter.pkg_name }}.skeleton import fib, app


def test_fib():
    """API Tests"""
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(RuntimeError):
        fib(-10)


def test_app(capsys):
    """CLI Tests"""
    # capsys is a pytest fixture that allows asserts against stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    with pytest.raises(SystemExit):  # exit code is 0
        app("7")
    captured = capsys.readouterr()
    assert "The 7-th Fibonacci number is 13" in captured.out
