import re

from flask import flash


def check_name(name) -> bool:
    """
    Функция для проверки имени по регулярному выражению.
    :param name: str (имя пользователя)
    :return: bool
    """
    pattern_name = r"^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$"
    if re.match(pattern_name, name) is not None:
        return True
    return False


def check_email(email) -> bool:
    """
    Функция для проверки почты пользователя по регулярному выражению.
    :param email: str (почта пользователя)
    :return: bool
    """
    pattern_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$"
    if re.match(pattern_email, email) is not None:
        return True
    return False


def check_login(login) -> bool:
    """
    Функция для проверки логина пользователя по регулярному выражению.
    :param login: str (логин пользователя)
    :return: bool
    """
    pattern_login = r"^[a-z0-9]+$"
    if re.match(pattern_login, login) is not None:
        return True
    return False


def check_length_login(login) -> bool:
    """
    Функция для проверки длины логина пользователя.
    :param login: str (логин пользователя)
    :return: bool
    """
    if len(login) <= 4 or len(login) > 20:
        return True
    return False


def check_length_password(password) -> bool:
    """
    Функция для проверки длины пароля пользователя.
    :param password: str (пароль пользователя)
    :return: bool
    """
    if len(password) <= 6 or len(password) > 33:
        return True
    return False


def check_registration(login, password, email, name) -> bool:
    """
    Функция для полной проверки при регистрации. Всплывает сообщение о соответствующей ошибке.
    :param login: str (логин пользователя)
    :param password: str (пароль пользователя)
    :param email: str (почта пользователя)
    :param name: str (имя пользователя)
    :return: bool
    """
    if not check_login(login):
        flash({"title": "Ошибка", "message": "Неккоректный логин!"}, "error")
        return False
    elif check_length_login(login):
        flash(
            {"title": "Ошибка", "message": "Неверная длина логина, 5-20 символов!"},
            "error",
        )
        return False
    elif check_length_password(password):
        flash(
            {"title": "Ошибка", "message": "Неверная длина пароля, 7-33 символов!"},
            "error",
        )
        return False
    elif not check_email(email):
        flash({"title": "Ошибка", "message": "Некорректная почта!"}, "error")
        return False
    elif not check_name(name):
        flash({"title": "Ошибка", "message": "Некорректное имя!"}, "error")
        return False
    else:
        return True


def check_update(password, email, name) -> bool:
    """
    Функция для полной проверки при обновлении данных. Всплывает сообщение о соответствующей ошибке.
    :param password: str (пароль пользователя)
    :param email: str (почта пользователя)
    :param name: str (имя пользователя)
    :return: bool
    """
    if check_length_password(password):
        flash(
            {"title": "Ошибка", "message": "Неверная длина пароля, 7-33 символов!"},
            "error",
        )
        return False
    elif not check_email(email):
        flash({"title": "Ошибка", "message": "Некорректная почта!"}, "error")
        return False
    elif not check_name(name):
        flash({"title": "Ошибка", "message": "Некорректное имя!"}, "error")
        return False
    else:
        return True
