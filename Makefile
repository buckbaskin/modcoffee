# Based on the Makefile from the requests package
init:
	pip install -r requirements.txt

test:
	# This runs all of the tests. To run an individual test, run py.test with
	# the -k flag, like "py.test -k test_path_is_not_double_encoded"
	py.test --verbose --doctest-modules tests modcoffee

coverage:
	py.test --verbose --doctest-modules --cov-report term --cov-report html:cover --cov=modcoffee tests modcoffee

lint:
	pylint modcoffee/
	pylint --disable=R,C,I tests/

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel --universal upload
	rm -fr build dist .egg requests.egg-info
