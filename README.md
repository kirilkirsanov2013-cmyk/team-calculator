# team-calculator

Учебный проект по Git и GitHub (ПР12, «Современные технологии программирования»).
Автор: Кирсанов К.В., группа П-31БС.

Калькулятор на Python. Каждая операция добавлялась в отдельной ветке и попадала в `main` через pull request.

| Ветка | Что добавлено |
|---|---|
| feature-add | `add()` — сложение, тест `test_add.py` |
| feature-subtract | `subtract()` — вычитание, тест `test_subtract.py` |
| feature-multiply | `multiply()` — умножение, тест `test_multiply.py` |

Запуск тестов:

```
python -m pip install pytest
python -m pytest
```
