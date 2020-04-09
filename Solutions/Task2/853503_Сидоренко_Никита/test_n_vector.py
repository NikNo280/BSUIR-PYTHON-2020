import math
import unittest

from n_vector import N_Vector

class Test_N_Vector(unittest.TestCase):
    def setUp(self):
        self.test_n_vector1 = N_Vector("1 2 3")
        self.test_n_vector2 = N_Vector("3 4 5")

    def test_multiplication_by_constant(self):
        self.assertTrue(self.test_n_vector1.multiplication_by_constant(3) == [3, 6, 9],
                         "Ошибка в умножении на константу")
        self.assertFalse(self.test_n_vector1.multiplication_by_constant(2) == [6, 13, 18],
                        "Ошибка в умножении на константу")

    def test_size(self):
        self.assertFalse(self.test_n_vector1.size() == 13,
                         "Ошибка, неверно найдена длинна")
        self.assertTrue(self.test_n_vector1.size() == math.sqrt(14),
                        "Ошибка, неверно найдена длинна")

    def test_get_item(self):
        self.assertFalse(self.test_n_vector1.get_item(0) == 2,
                         "Ошибка, неверно найден item по интедксу")
        self.assertTrue(self.test_n_vector1.get_item(2) == 3,
                        "Ошибка, неверно найден item по интедксу")

    def test_sum(self):
        self.assertFalse(self.test_n_vector1.sum(self.test_n_vector2) == [1, 13, 125],
                         "Ошибка в сложении")
        self.assertTrue(self.test_n_vector1.sum(self.test_n_vector2) == [4, 6, 8],
                        "Ошибка в сложении")

    def test_subtraction(self):
        self.assertFalse(self.test_n_vector1.subtraction(self.test_n_vector2) == [1, 213, 125],
                         "Ошибка в вычитании")
        self.assertTrue(self.test_n_vector1.subtraction(self.test_n_vector2) == [-2, -2, -2],
                        "Ошибка в вычитании")

    def test_multiplication(self):
        self.assertFalse(self.test_n_vector1.multiplication(self.test_n_vector2) == [1, 213, 125],
                         "Ошибка в умножении")
        self.assertTrue(self.test_n_vector1.multiplication(self.test_n_vector2) == [3, 8, 15],
                        "Ошибка в умножении")

    def test_division(self):
        self.assertFalse(self.test_n_vector2.division(self.test_n_vector1) == [1, 213, 125],
                         "Ошибка в делении")
        self.assertTrue(self.test_n_vector2.division(self.test_n_vector1) == [3.0, 2.0, 1.6666666666666667],
                        "Ошибка в делении")

    def test_scalar_product(self):
        self.assertFalse(self.test_n_vector1.scalar_product(self.test_n_vector2) == 12,
                         "Ошибка в скалярном произведении")
        self.assertTrue(self.test_n_vector1.scalar_product(self.test_n_vector2) == 26,
                        "Ошибка в скалярном произведении")

    def test_equals(self):
        self.assertFalse(self.test_n_vector1.equals(self.test_n_vector2),
                         "Ошибка в сравнении")
        self.assertTrue(self.test_n_vector1.equals(self.test_n_vector1),
                        "Ошибка в сравнении")

if __name__ == '__main__':
    unittest.main()
