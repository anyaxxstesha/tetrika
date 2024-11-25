import unittest

from task_1.solution import sum_two, sum_str, no_return_annotation, no_params_annotation, bad_return_annotation


class DecoratorStrictTestCase(unittest.TestCase):
    """Тесты для декоратора strict """

    def test_sum_two_same_type(self):
        """
        Тестируется декорированная функция
        sum_two с аргументами одинаковых типов
        """
        result = sum_two(1, 2)
        self.assertEqual(result, 3)

    def test_sum_two_diff_type(self):
        """
        Тестируется декорированная функция
        sum_two с аргументами разных типов
        """
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)

    def test_sum_str_same_type(self):
        """
        Тестируется декорированная функция
        sum_str с аргументами одинаковых типов
        """
        result = sum_str('a', 'b', 'c')
        self.assertEqual(result, 'abc')

    def test_sum_str_diff_type(self):
        """
        Тестируется декорированная функция
        sum_str с аргументами разных типов
        """
        with self.assertRaises(TypeError):
            sum_str('a', 2.4)

    def test_no_return_annotations(self):
        """
        Тестируется декорированная функция no_return_annotation
        с отсутствующей аннотацией возвращаемого значения
        """
        with self.assertRaises(TypeError):
            no_return_annotation('a')

    def test_no_params_annotations(self):
        """
        Тестируется декорированная функция no_params_annotation
        с отсутствующей аннотацией параметров
        """
        with self.assertRaises(TypeError):
            no_params_annotation('ra', 'fa')

    def test_sum_str_wrong_return(self):
        """
        Тестируется декорированная функция
        sum_str с аргументами разных типов
        """
        with self.assertRaises(TypeError):
            sum_str('a', 'b')

    def test_bad_return_annotation(self):
        """
        Тестируется декорированная функция bad_return_annotation
        с несовпадающими типами аннотации возвращаемого значения
        и фактического возвращаемого значения
        """
        with self.assertRaises(TypeError):
            bad_return_annotation(1, 2)

if __name__ == '__main__':
    unittest.main()
