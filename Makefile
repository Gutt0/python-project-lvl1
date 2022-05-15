install: #устанавливаем poetry
	poetry install

brain-games: #вызываем приветственное сообщение
	poetry run brain-games

build: #сборка проекта
	poetry build

publish: #публикация вне PyPi
	poetry publish --dry-run

package-install: #установка проекта
	python3 -m pip install --user dist/*.whl