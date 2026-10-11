from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """Декоратор, который логирует результат выполнения функций"""

    def wrapper(func: F) -> F:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                status = "ok"
                end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                write_log(start_time, end_time, filename=filename, func_name=func_name, status=status)
                return result
            except Exception as e:
                status = f"{type(e).__name__}: {str(e)}. Inputs: {args}, {kwargs}"
                end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                write_log(start_time, end_time, filename=filename, func_name=func_name, status=status)
                raise

        return cast(F, inner)

    return wrapper


def write_log(
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    *,
    filename: Optional[str] = None,
    func_name: Optional[str] = None,
    status: Optional[str] = None,
) -> None:
    """Вспомогательная функция, которая отвечает за запись логов в файл или вывод их в консоль"""
    log_message = f"{func_name} {status}"
    if filename:
        try:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"[{start_time} -> {end_time}] {log_message}\n")
        except IOError as e:
            print(f"Ошибка записи в файл {filename}: {e}")
            print(f"[{start_time} -> {end_time}] {log_message}")
    else:
        print(f"[{start_time} -> {end_time}] {log_message}")
