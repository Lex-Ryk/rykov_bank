from datetime import datetime


def log(filename=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            func_name = func.__name__
            start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            try:
                result = func(*args, **kwargs)
                status = 'ok'
                end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                write_log(start_time, end_time, filename=filename, func_name=func_name, status=status)
                return result
            except Exception as e:
                status = f'{type(e).__name__}: {str(e)}. Inputs: {args}, {kwargs}'
                end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                write_log(start_time, end_time, filename=filename, func_name=func_name, status=status)
                raise
        return inner
    return wrapper


def write_log(
        start_time=None,
        end_time=None,
        *,
        filename=None,
        func_name=None,
        status=None,):
    """Вспомогательная функция, которая отвечает за запись логов в файл или вывод их в консоль"""
    log_message = f'{func_name} {status}'
    if filename:
        try:
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(f'[{start_time} -> {end_time}] {log_message}\n')
        except IOError as e:
            print(f"Ошибка записи в файл {filename}: {e}")
            print(f'[{start_time} -> {end_time}] {log_message}')
    else:
        print(f'[{start_time} -> {end_time}] {log_message}')
