build:	clean
	python cx_setup.py bdist_dmg

clean:
	find . -name 'build' -print0 | xargs rm -rf
