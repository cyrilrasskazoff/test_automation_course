# Проверка ожидаемого результата
# Assert: assert True не приводит к выводу дополнительных сообщений, assert False вызовет исключение AssertionError

assert abs(-1) == 1

# Простое сообщение AssertionError не очень информативно. Когда тестов становится много, бывает сложно вспомнить, что именно мы проверяем в данном тесте.
# Для добавления дополнительного сообщения можно при вызове assert через запятую написать нужное сообщение, которое будет выведено в случае ошибки проверки результата:

assert abs(-1) == -1, "Should be absolute value of a number"

# сообщения об ошибках должны быть информативными, иногда имеет смысл пользоваться форматированием строк, например f-строками
# def test_input_text(expected_result, actual_result):
#     assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

# Иногда при работе с текстами не нужны жёсткие проверки на полное совпадение, и требуется проверить,
# что некий текст является подстрокой другого текста. Это можно сделать с помощью ключевого слова in
# def test_substring(full_string, substring):
#     assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"