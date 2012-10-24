# PYSHELL:=$(shell which ipython || which python|| which sh)
# SHELL=$(PYSHELL)
#.SHELLFLAGS=-c
SHELL:=$(shell which ipython)
#SHELL=/usr/local/share/python/ipython
.SILENT: ;      # no need for @
.ONESHELL: ;    # recipes execute in same shell
.NOTPARALLEL: ; # wait for this target to finish
.EXPORT_ALL_VARIABLES: ; # send all vars to shell
Makefile: ;     # skip prerequisite discovery

# shrink: awk 'START{x=""};{gsub(" {4}","ø")};{gsub(" ","∆")};{x = x"≈"$0};END{print x}'  tt.t | gzip -9 -f > ts.gz
MAKE_MODULE=≈def∆prompt(kx):≈øif∆len(kx['value'].strip())∆==∆0:≈øøprint∆kx['message']≈øøif∆'usage'∆in∆kx:≈øøøprint∆'{:>9}\n{:10}{}'.format('Usage:',∆'',∆kx['usage'])≈øøreturn∆True≈øreturn∆False≈≈def∆prompt_in(msg):≈øfrom∆sys∆import∆stdout≈øprint∆msg≈østdout.flush()≈øinp∆=∆raw_input('')≈østdout.flush()≈øreturn∆inp≈
.module-exists:
	!test -f Makefile.py || echo $$MAKE_MODULE | awk '{gsub("∆"," ")};{gsub("ø","    ")};{gsub("≈","\n")};{if(x){x=x"\\n"$$0}else{x=$$0}};END{print x};' > Makefile.py

# checkshellconf: SHELL=/bin/sh
# 	ifeq (,$(findstring python, $(PYSHELL)))
# 	    echo "You will require a python installation for aero"
# 	    exit
# 	else ifeq (,$(findstring ipython, $(PYSHELL)))
# 	    echo "You should have ipython installed for general goodness but its also required for this Makefile."
# 	    echo "You can simply install ipython with aero install pip:ipython"
# 	    exit
# 	endif


# Do the funky python
.cmd:
	$c

.DEFAULT_GOAL := cmd
cmd: .module-exists
	c = !echo $$py
	kx = dict(
	    value=c.s,
	    message='cmd one liners target requires the py paramater variable set',
	    usage="make py='alias'"
	)
	from Makefile import prompt
	if prompt(kx) is False:
	    !$(MAKE) .cmd c="$$py"

python: .module-exists
	c = !echo $$filename
	kx = dict(
	    value=c.s,
	    message='python source file target requires the filename paramater variable set',
	    usage="make python filename='source.py'"
	)
	from Makefile import prompt
	if prompt(kx) is False:
	    !$(MAKE) .cmd c="$$( < $$filename)"

run-python: .module-exists
	c = !echo $$filename
	kx = dict(
	    value=c.s,
	    message='python source file run target, allows no magic, requires the filename paramater variable set',
	    usage="make run-python filename='source.py'"
	)
	from Makefile import prompt
	if prompt(kx) is False:
		!$(MAKE) .cmd c="run $$filename"


lsmagic:
	lsmagic

php:
	%%script /usr/bin/env php
	<?php
	echo "I am php\n";

bash:
	%%bash
	echo I am bash

clean:
	!find . -iname '*.pyc' -o -iname '*.pyo' -delete

pypack: .module-exists
	c = !test -f setup.py || echo 'all clear'
	kx = dict(
	    value=c.s,
	    message='A setup.py file already exists in this location, pypack requires an empty folder.'
	)
	from Makefile import prompt_in
	if prompt(kx) is False:
	   package = prompt_in('Name of the new package')
	   descript = prompt_in('Give a brief description')
	   author = prompt_in('Author name')
	   email = prompt_in('Author email')
	   url = prompt_in('Project url')
	   version = prompt_in('Initial release version')
	   !pypack --author=author --email=email --url=url --initial-version=version --desc=descript package

bootstrap:
	!which virtualenv || echo 'Install virtualenv at least, so we can start.'
	!test -d .venv || virtualenv .venv
	!.venv/bin/pip install -r requirements.txt
	!.venv/bin/pip install -r test_requirements.txt
	!echo 'To work with this virtualenv just execute source $PWD/.venv/bin/activate'

test:
	!nosetests --all-modules tests/ ${ARGS}

coverage:
	!$(MAKE) test ARGS="--with-coverage --cover-package=aero ${ARGS}"

coverage-html:
	!$(MAKE) test ARGS="--cover-html ${ARGS}"

# -include=checkshellconf
