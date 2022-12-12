# unittest
# Тест-раннеры сами находят тестовые методы в указанных при запуске файлах, но для этого нужно следовать общепринятым правилам.
# Общее правило для всех фреймворков: название тестового метода должно начинаться со слова "test_".  Дальше может идти любой текст,
# который является уникальным названием для теста: e.g., def test_name_for_your_test():

# Для unittest существуют собственные дополнительные правила:
# 1. Тесты обязательно должны находиться в специальном тестовом классе.
# 2. Вместо assert должны использоваться специальные assertion методы

# Изменим наши предыдущие тесты, чтобы их можно было запустить с помощью unittest. Для этого нам понадобится выполнить следующие шаги:
#
# Импортировать unittest в файл: import unittest
# Создать класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
# Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции: def test_abs1(self):
# Изменить assert на self.assertEqual()
# Заменить строку запуска программы на unittest.main()

import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()