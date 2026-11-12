gendiff:
	uv run gendiff

sync:
	uv sync


tree:
	tree -I '__pycache__|.venv |tempCodeRunnerFile.py'



build:
	uv build


# Обновление пакета. Не нужна команда uv build. Берет код прям из  папки.
finstall:
	uv tool install --force .


# Установка пакета. Обязательна команда uv build.
install:
	uv tool install dist/*.whl


# Только проверяет код и стиль, ничего не меняет. Выводи красивое оформление на гитхаб.
lint:
	uv run ruff check --output-format=github gendiff tests
	uv run ruff format --check gendiff tests


# Автоматически исправляет ТОЛЬКО форматирование (пробелы, отступы), 
# но оставляет логические ошибки, чтобы ты исправил их сам
format:
	uv run ruff format gendiff tests


# Запуск тестов и процент покрытия кода тестами
test-coverage:
        uv run pytest --cov=gendiff tests/
