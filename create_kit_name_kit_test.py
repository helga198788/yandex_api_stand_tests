import sender_stand_request
import data

#Функция меняет значения в параметре name
def get_kit_body(name):
    # скопировать словарь с телом запроса из data, для того, чтобы не потерялись данные в исходном словаре
    current_body = data.kit_body.copy()
    # поменять значения в поле name
    current_body["name"] = name
    # возврат нового словаря с нужным значением name
    return current_body

# Функция для позитивной проверки
def positive_assert(name):
    # В переменную kit_body сохраняем тело запроса (обновлённое)
    kit_body = get_kit_body(name)
    #В переменную  auth_token сохраняем токен, который получили
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
# В переменную kit_response сохраняем  результат запроса на создание пользователя:

    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
# Проверяем, что код ответа равен 201
    print(kit_response.status_code)
    assert kit_response.status_code == 201
# Проверяем, что ответ с  полем name совпадает с полем name в запросе
    print(name , "<--- просто наме")
    print(kit_response.json()["name"])
    assert kit_response.json()["name"] == name

# Функция для негативной проверки
def negative_assert_code_400(name):
    # В переменную kit_body сохраняем тело запроса ( обновлённое)
    kit_body = get_kit_body(name)
    # В переменную  auth_token сохраняем токен,который получили
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
    # В переменную kit_response сохраняем результат запроса на создание пользователя:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
# Проверяем, что код ответа равен 400
    assert kit_response.status_code == 400

# Тест 1. Успешное создание набора
# Параметр name 1 символ
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("а")

# Тест 2. Успешное создание набора
# Параметр name 511 символов
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3. Набор не создался
# Параметр name 0 символов
def test_create_kit_0_letter_in_name_get_400_response():
    negative_assert_code_400("")

# Тест 4. Набор не создался
# Параметр name 512 символов
def test_create_kit_512_letters_in_name_get_400_response():
    negative_assert_code_400(" AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Успешное создание набора
# Параметр name английские буквы
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Успешное создание набора
# Параметр name русские буквы
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Успешное создание набора
    # Параметр name- спецсимволы
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

# Тест 8. Успешное создание набора
# Параметр name- допустимы пробелы
def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(" Человек и КО ")

# Тест 9. Успешное создание набора
# Параметр name- цифры
def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")

# Тест 10. Набор не создался
# В запросе нет параметра name
def test_create_kit_no_name_get_400_response():
# Копируем словарь с телом запроса из data в переменную kits_body
    kits_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kits_body.pop("name")
    # В переменную  auth_token сохраняется полученный токен
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
# В переменную kit_response сохраняется результат запроса на создание пользователя:
    kit_response = sender_stand_request.post_new_client_kit(kits_body, auth_token)
# Проверяем, что код ответа равен 400
    assert kit_response.status_code == 400

# Тест 11. Набор не создался
# В параметр name передан другой тип параметра(число)
def test_create_number_as_name_get_400_response():
    negative_assert_code_400(123)









