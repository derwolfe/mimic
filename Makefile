all: clean build test

build:
	python setup-mac.py py2app

test:
	./dist/mimic.app/Contents/MacOS/run-tests

clean:
	find ./mimic/ -name '*.pyc' -delete
	find ./twisted/ -name '*.pyc' -delete
	find . -name 'dist' -print0 | xargs rm -rf
	find . -name 'build' -print0 | xargs rm -rf
	find . -name 'dropin.cache' -delete
run:
	open ./dist/mimic.app

.PHONY:
	build test clean run
