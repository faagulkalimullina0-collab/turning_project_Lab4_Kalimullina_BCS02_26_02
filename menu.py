"""
Меню выбора материала и маршрутизация через match-case.

Пункты меню:
  1 — сталь    (ρ = 7850 кг/м3)
  2 — алюминий (ρ = 2700 кг/м3)
  3 — медь     (ρ = 8900 кг/м3)
  0 — выход
"""

from constants import RHO_STEEL, RHO_ALUMINUM, RHO_COPPER


def show_menu() -> None:
    """Вывести меню выбора материала."""
    print("\n Выберите материал листа:")
    print("  1 — сталь    (ρ = 7850 кг/м3)")
    print("  2 — алюминий (ρ = 2700 кг/м3)")
    print("  3 — медь     (ρ = 8900 кг/м3)")
    print("  0 — выход")


def select_material() -> float | None:
    """
    Циклически запрашивать материал и возвращать его плотность ρ.

    Маршрутизация — только match-case.
    Возвращает None, если выбран выход (0).
    """
    while True:
        choice = input("Введите номер материала (от 0 до 3): ").strip()
        match choice:
            case "1":
                return RHO_STEEL
            case "2":
                return RHO_ALUMINUM
            case "3":
                return RHO_COPPER
            case "0":
                return None
            case _:
                print("Ошибка: неверный пункт меню. Повторите ввод.")


def material_name(rho: float) -> str:
    """Вернуть название материала по его плотности (match-case)."""
    match rho:
        case 7850.0:
            return "сталь"
        case 2700.0:
            return "алюминий"
        case 8900.0:
            return "медь"
        case _:
            return "неизвестный материал"