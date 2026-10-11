import re

import pytest

from src.decorators import log, write_log


def test_log(capsys):
    @log()
    def my_func(x, y):
        return x + y

    my_func(2, 3)

    captured = capsys.readouterr()

    pattern = re.compile(
        r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} -> \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] my_func ok\n"
    )

    assert pattern.search(captured.out) is not None


def test_log_error():
    @log()
    def my_func():
        raise ValueError("Something went wrong!")

    with pytest.raises(Exception, match="Something went wrong!"):
        my_func()


def test_correct_log_to_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(str(log_file))
    def test_func(x, y):
        return x + y

    test_func(1, 2)

    content = log_file.read_text(encoding="utf-8")

    pattern = re.compile(
        r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} -> \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] test_func ok\n"
    )

    assert pattern.search(content) is not None


def test_error_log_to_file(tmp_path):
    log_file = tmp_path / "error.log"

    @log(str(log_file))
    def test_func(x, y):
        raise ValueError("Unforeseen error")

    try:
        test_func(1, 2)
    except Exception:
        pass

    content = log_file.read_text(encoding="utf-8")

    pattern = re.compile(
        r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} -> \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]"
        r" test_func ValueError: Unforeseen error\. Inputs: \(1, 2\), \{\}\n"
    )

    assert pattern.search(content) is not None


def test_write_log_to_console(capsys):
    write_log(func_name="Test", status="Passed")

    captured = capsys.readouterr()
    assert captured.out == f"[{None} -> {None}] Test Passed\n"


def test_write_log_to_file(tmp_path):
    log_file = tmp_path / "test.log"

    write_log(filename=str(log_file), func_name="test_func", status="Passed")

    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert content == f"[{None} -> {None}] test_func Passed\n"


def test_write_log_io_error(tmp_path, capsys):
    bad_path = tmp_path / "not_a_file"
    bad_path.mkdir()

    write_log(filename=str(bad_path), func_name="failing_func", status="crash")

    captured = capsys.readouterr()

    assert "Ошибка записи в файл" in captured.out
    assert "failing_func crash" in captured.out
