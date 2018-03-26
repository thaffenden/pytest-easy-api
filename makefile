
test:
	pytest -vv -s --cov-report term-missing --cov pytest_easy_api tests

release:
	python setup.py sdist upload -r pypi
