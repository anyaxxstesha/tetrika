import csv
import os
import sys
import unittest

from bs4 import BeautifulSoup

from task_2.solution import main


class DecoratorStrictTestCase(unittest.TestCase):
    """Тесты для декоратора strict """

    def test_main(self):
        """Testing main function."""
        main()
        self.assertTrue(os.path.exists('./beasts.csv'))
        with open('beasts.csv', 'r') as file:
            reader = csv.reader(file)
            summ = 0
            for _, amount in reader:
                summ += int(amount)
        self.assertEqual(summ, 46307)


if __name__ == '__main__':
    unittest.main()
