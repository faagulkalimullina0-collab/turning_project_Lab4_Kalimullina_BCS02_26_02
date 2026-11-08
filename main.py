"""
Точка входа проекта «Расчёт расхода материала при раскрое листа».

Связывает модули: меню выбора материала, валидацию ввода,
расчёты и вывод результатов. Никакой логики валидации/расчёта
здесь нет — только связывание.
"""

from validators import (
    input_length,
    input_width,
    input_thickness,
    input_quantity,
)
from menu import show_menu, select_material, material_name
from operations import sheet_mass, thickness_class


def main() -> None:
    """Главный сценарий: меню → ввод → расчёт → вывод, до выхода."""
    print("=== Расчёт расхода материала при раскрое листа ===")

    while True:
        show_menu()
        rho = select_material()
        if rho is None:
            print("Работа завершена.")
            break

        length = input_length()
        width = input_width()
        thickness = input_thickness()
        quantity = input_quantity()

        mass = sheet_mass(length, width, thickness, rho, quantity)
        cls = thickness_class(thickness)

        print("\n Результаты ")
        print(f"Материал:        {material_name(rho)} (ρ = {rho:.0f} кг/м3)")
        print(f"Масса партии:    {mass:.2f} кг")
        print(f"Класс толщины:   {cls}")
        print("\n")


if __name__ == "__main__":
    main()