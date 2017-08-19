ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))


develop:
	conda create --name flask-restful python=3.5  --path=$(ROOT_DIR)/.venv
	source activate flask-restful
	pip install -r requirements.txt

clean:
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '#*#' `
	@rm -f `find . -type f -name '*.orig' `
	@rm -f `find . -type f -name '*.rej' `