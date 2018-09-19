ex :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

pipenv --python 3.6
# установка python нужной версии

pipenv install package_name --dev
# установка пакета в список dev-зависимостей

pipenv lock --pre
#

pipenv graph
#

pipenv check
#

pipenv install -e .
#

pipenv run pip freeze
#

