pipenv :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Pipenv это проект, цель которого привнести лучшее из мира packaging в мир 
# Python. Он объединяет такие утилиты как Pipfile, pip и virtualenv в единый 
# инструмент. Pipenv автоматически создаёт и управляет virtualenv в ваших проектах, 
# а также позволяет устанавливать/удалять пакеты Pipfile. А команда lock создаёт 
# lockfile (Pipfile.lock).

	# установк python нужной версии через pyenv
	# загрузка переиеннх среды из файла
	# проверка стиля кода
	# генерация requirements.txt из Pipfile
	# работа без virtualenv
	# обноружения неиспользуемых зависимостей

# документация на английском:
# https://docs.pipenv.org/

# почему следует использовать его, а не pip + virtualenv
# https://www.youtube.com/watch?v=pMNPP9VTI7U

# установка:
pip install pipenv

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# использование:

pipenv [OPTIONS] COMMAND [ARGS]...

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
OPTIONS:

--three / --two
# для инициализации виртуальной среды Python3 / Python2

--where
# 

--bare
#

--version
#

-h --help
#

--venv
#

--py
#

--envs
#

--rm
#

--completion
#

--man
#

--python TEXT
#

--site-packages
#




# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
COMMAND:

pipenv install
# если не передавать параметров команде install, будут установлены все требуемые 
# пакеты

pipenv install packag_name
# будет установлен требуемый пакет

pipenv uninstall
# если не передавать параметров команде uninstall, все пакеты будут удалены

pipenv uninstall packag_name
# будет удалён требуемый пакет

pipenv shell
# создаст обалочку в виртуальной среде

pipenv run 
# запустит переданную команду в virtualenv, со всеми переданными аргументами 
# (например, $ pipenv run python manage.py).

pipenv check
# проверит соответствие зависимостей текущей среды стандарту PEP 508

pipenv update
# обновит все пакеты

pipenv update packag_name
# обновит указаный пакет

pipenv lock
# обнавление лок-файла

pipenv clean
# 

pipenv graph
# визуализация дерева зависимостей

pipenv open packag_name
# откроет исходники указанного пакета

pipenv sync