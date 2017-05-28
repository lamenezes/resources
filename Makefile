clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

test: clean
	flake8 simple_model tests --max-line-length=96
	py.test

build: test clean
	python setup.py sdist

push:
	git push origin master --tags

upload:
	twine upload dist/*.gz

release-after-bump: build clean push upload
