Простой инструмент для генерации отчетов по успеваемости студентов (и других метрик) из CSV-файлов.

Скачать проект на локальную машину.

Далее переходим в директорию workmate
c помощью команды ```cd workmate```
Устанавливаем зависимости с помощью команды ```poetry install```
Если poetry нету нужно установить.

После установки выполнить команду
```poetry run python main.py --files students1.csv students2.csv --report students-performance```

Тесты можно запустить с помощью команды
```poetry run python -m pytest -v```

Покрытие тестами
```poetry run python -m pytest --cov=reports --cov=main --cov-report=term-missing -v```
