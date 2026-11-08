"""
Расчёты: масса партии листов и класс толщины.

Формула: m = L · W · (t / 1000) · ρ · q, кг.
Классификация толщины — через if-elif-else.
"""

from typing import Annotated

from constants import T_THIN_LIMIT, T_THICK_LIMIT


def sheet_mass(
    length: Annotated[float, "Длина листа, м"],
    width: Annotated[float, "Ширина листа, м"],
    thickness: Annotated[float, "Толщина листа, мм"],
    density: Annotated[float, "Плотность материала, кг/м3"],
    quantity: Annotated[int, "Количество листов, шт."],
) -> float:
    """
    Рассчитать массу партии листов.

    m = L · W · (t / 1000) · ρ · q

    Args:
        length: длина листа, м.
        width: ширина листа, м.
        thickness: толщина листа, мм.
        density: плотность материала, кг/м3.
        quantity: количество листов, шт.

    Returns:
        Масса партии, кг.
    """
    return length * width * (thickness / 1000.0) * density * quantity


def thickness_class(
    thickness: Annotated[float, "Толщина листа, мм"],
) -> str:
    """
    Классифицировать толщину листа через if-elif-else.

    t < 0.5           — тонкий лист;
    0.5 ≤ t ≤ 5       — нормальная толщина;
    t > 5             — толстый лист.

    Args:
        thickness: толщина листа, мм.

    Returns:
        Строка с названием класса толщины.
    """
    if thickness < T_THIN_LIMIT:
        return "тонкий лист"
    elif thickness <= T_THICK_LIMIT:
        return "нормальная толщина"
    else:
        return "толстый лист"