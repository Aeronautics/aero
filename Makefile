clean:
	find -iname '*.pyc' -o '*.pyo' -delete
bootstrap:
	@which virtualenv || echo 'Install virtualenv at least, so we can start.'
	test -d .venv || virtualenv .venv
	.venv/bin/pip install -r requirements.txt
	.venv/bin/pip install -r test_requirements.txt
	@echo 'To work with this virtualenv just execute source $PWD/.venv/bin/activate'
test:
	nosetests --all-modules tests/ ${ARGS}
coverage:
	$(MAKE) test ARGS="--with-coverage --cover-package=aero ${ARGS}"
coverage-html:
	$(MAKE) test ARGS="--cover-html ${ARGS}"
