"""
Валидация пользовательского ввода.

- Проверка границ через if-elif-else.
- Циклический ввод до корректного значения.
- match-case здесь запрещён.
"""

from constants import (
    L_MIN, L_MAX,
    W_MIN, W_MAX,
    T_MIN, T_MAX,
    Q_MIN, Q_MAX,
)
from logger import log_error


def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    """
    Проверка попадания value в [low, high] через if-elif-else.

    Args:
        value: проверяемое значение.
        low: нижняя граница.
        high: верхняя граница.

    Returns:
        (True, "") если внутри диапазона,
        иначе (False, "сообщение").
    """
    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low})."
    elif value > high:
        return False, f"Ошибка: значение больше верхней границы ({high})."
    else:
        return True, ""


def input_number(prompt: str, low: float, high: float) -> float:
    """
    Циклически запрашивать число, пока не будет корректного.

    Проверяет тип через try/except ValueError и границы
    через validate_range. Все ошибки пишутся в logger.

    Args:
        prompt: приглашение к вводу.
        low: нижняя граница.
        high: верхняя граница.

    Returns:
        Корректное значение типа float.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введено не число ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)


def input_length() -> float:
    """Циклический ввод длины листа L (м), допустимо 0.1..5."""
    return input_number(
        "Введите длину листа L, м (0.1..5): ",
        L_MIN, L_MAX,
    )


def input_width() -> float:
    """Циклический ввод ширины листа W (м), допустимо 0.1..3."""
    return input_number(
        "Введите ширину листа W, м (0.1..3): ",
        W_MIN, W_MAX,
    )


def input_thickness() -> float:
    """Циклический ввод толщины листа t (мм), допустимо 0.1..20."""
    return input_number(
        "Введите толщину листа t, мм (0.1..20): ",
        T_MIN, T_MAX,
    )


def input_quantity() -> int:
    """
    Циклический ввод количества листов q (целое), допустимо 1..1000.
    """
    while True:
        raw = input("Введите количество листов q, шт. (1..1000): ").strip()
        try:
            value = int(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введено не целое число ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(float(value), float(Q_MIN), float(Q_MAX))
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)