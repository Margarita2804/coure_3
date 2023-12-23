# Описание проекта course work №3

## Структура проекта
  + main.py - запуск проекта
  + src/util.py - основные функции
  + data/operations.json - файл json проекта
  + tests/test_utils.py - файл с тестами функций
  + tests/data/ - папка с тестовыми json файлами
  + config.py - пути до файлов
  + .gitignore - файл игнор
  + requirements.txt - зависимости проекта
  + README.md - описание проекта

### Описание функций файла utils.py
+ load_data - загружает json файл проекта
+ sorted_data - сортирует загруженный json
+ date_conversion - конвертирует дату
+ transaction_convert_check - форматирует номер счета или карты
+ final_transaction - итоговая информация о транзакции
+ list_transaction - список итоговых транзакций
