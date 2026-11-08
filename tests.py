"""
Юнит-тесты для validators и operations.

Запуск: python -m unittest tests -v
Не менее 20 тестов.
"""

import unittest
from unittest.mock import patch

import logger
import operations
import validators


class TestValidateRange(unittest.TestCase):
    """Проверка границ через validate_range (5 тестов)."""

    def test_inside(self):
        """Значение внутри диапазона — True."""
        ok, msg = validators.validate_range(5.0, 1.0, 10.0)
        self.assertTrue(ok)
        self.assertEqual(msg, "")

    def test_on_lower_bound(self):
        """Значение на нижней границе — True."""
        ok, _ = validators.validate_range(1.0, 1.0, 10.0)
        self.assertTrue(ok)

    def test_on_upper_bound(self):
        """Значение на верхней границе — True."""
        ok, _ = validators.validate_range(10.0, 1.0, 10.0)
        self.assertTrue(ok)

    def test_below_lower(self):
        """Значение ниже нижней границы — False."""
        ok, msg = validators.validate_range(0.5, 1.0, 10.0)
        self.assertFalse(ok)
        self.assertIn("меньше нижней границы", msg)

    def test_above_upper(self):
        """Значение выше верхней границы — False."""
        ok, msg = validators.validate_range(11.0, 1.0, 10.0)
        self.assertFalse(ok)
        self.assertIn("больше верхней границы", msg)


class TestInputLength(unittest.TestCase):
    """Циклический ввод длины L (3 теста)."""

    def setUp(self):
        """Очистить журнал перед каждым тестом."""
        logger.clear()

    @patch("validators.input", side_effect=["abc", "10", "2.5"])
    def test_cycle_with_errors(self, _mock):
        """abc → 10 (выше границы) → 2.5 (ок)."""
        self.assertAlmostEqual(validators.input_length(), 2.5)

    @patch("validators.input", side_effect=["0.1"])
    def test_lower_bound(self, _mock):
        """Нижняя граница 0.1 принимается."""
        self.assertAlmostEqual(validators.input_length(), 0.1)

    @patch("validators.input", side_effect=["5.0"])
    def test_upper_bound(self, _mock):
        """Верхняя граница 5.0 принимается."""
        self.assertAlmostEqual(validators.input_length(), 5.0)


class TestInputThickness(unittest.TestCase):
    """Циклический ввод толщины t (3 теста)."""

    def setUp(self):
        """Очистить журнал перед каждым тестом."""
        logger.clear()

    @patch("validators.input", side_effect=["abc", "25", "0.5"])
    def test_cycle_with_errors(self, _mock):
        """abc → 25 (выше границы) → 0.5 (ок)."""
        self.assertAlmostEqual(validators.input_thickness(), 0.5)

    @patch("validators.input", side_effect=["0.1"])
    def test_lower_bound(self, _mock):
        """Нижняя граница 0.1 принимается."""
        self.assertAlmostEqual(validators.input_thickness(), 0.1)

    @patch("validators.input", side_effect=["20.0"])
    def test_upper_bound(self, _mock):
        """Верхняя граница 20.0 принимается."""
        self.assertAlmostEqual(validators.input_thickness(), 20.0)


class TestInputQuantity(unittest.TestCase):
    """Циклический ввод количества q (3 теста)."""

    def setUp(self):
        """Очистить журнал перед каждым тестом."""
        logger.clear()

    @patch("validators.input", side_effect=["abc", "0", "100"])
    def test_cycle_with_errors(self, _mock):
        """abc → 0 (ниже границы) → 100 (ок)."""
        self.assertEqual(validators.input_quantity(), 100)

    @patch("validators.input", side_effect=["1"])
    def test_lower_bound(self, _mock):
        """Нижняя граница 1 принимается."""
        self.assertEqual(validators.input_quantity(), 1)

    @patch("validators.input", side_effect=["1000"])
    def test_upper_bound(self, _mock):
        """Верхняя граница 1000 принимается."""
        self.assertEqual(validators.input_quantity(), 1000)


class TestOperations(unittest.TestCase):
    """Расчёты: масса партии и класс толщины (6 тестов)."""

    def test_mass_single_sheet(self):
        """Масса одного листа стали 1×1 м, t = 1 мм."""
        m = operations.sheet_mass(1.0, 1.0, 1.0, 7850.0, 1)
        self.assertAlmostEqual(m, 7.85, places=2)

    def test_mass_aluminum(self):
        """Масса 2×1.5 м, t = 2 мм, алюминий, q = 10."""
        m = operations.sheet_mass(2.0, 1.5, 2.0, 2700.0, 10)
        self.assertAlmostEqual(m, 162.0, places=2)

    def test_mass_copper(self):
        """Масса 0.5×0.5 м, t = 0.5 мм, медь, q = 100."""
        m = operations.sheet_mass(0.5, 0.5, 0.5, 8900.0, 100)
        self.assertAlmostEqual(m, 111.25, places=2)

    def test_thickness_thin(self):
        """t = 0.3 → тонкий лист."""
        self.assertEqual(operations.thickness_class(0.3), "тонкий лист")

    def test_thickness_normal_bounds(self):
        """t = 0.5 и t = 5.0 → нормальная толщина."""
        self.assertEqual(operations.thickness_class(0.5), "нормальная толщина")
        self.assertEqual(operations.thickness_class(5.0), "нормальная толщина")

    def test_thickness_thick(self):
        """t = 12 → толстый лист."""
        self.assertEqual(operations.thickness_class(12.0), "толстый лист")


if __name__ == "__main__":
    unittest.main()