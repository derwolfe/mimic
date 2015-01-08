#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    DARWIN=true
else
    DARWIN=false
fi

if [[ "$DARWIN" = true ]]; then
    brew update

    if which pyenv > /dev/null; then
	eval "$(pyenv init -)"
    fi

    case "${TOXENV}" in
	py26)
	    curl -O https://bootstrap.pypa.io/get-pip.py
	    sudo python get-pip.py
	    pyenv install 2.6
	    pyenv global 2.6
	    ;;
	py27)
	    curl -O https://bootstrap.pypa.io/get-pip.py
	    sudo python get-pip.py
	    pyenv install 2.7.8
	    pyenv global 2.7
	    ;;
	pypy)
	    brew upgrade pyenv
	    pyenv install pypy-2.4.0
	    pyenv global pypy-2.4.0
	    ;;
	docs)
	    curl -O https://bootstrap.pypa.io/get-pip.py
	    sudo python get-pip.py
	    ;;
	bundle)
	    curl -O https://bootstrap.pypa.io/get-pip.py
	    sudo python get-pip.py
	    pyenv install 2.7.8
	    pyenv global 2.7.8
	    ;;
    esac
    pyenv rehash

else
    sudo apt-get -y update
    sudo add-apt-repository -y ppa:fkrull/deadsnakes

    case "${TOXENV}" in
	py26)
	    sudo apt-get install python2.6 python2.6-dev
	    ;;
	py27)
	    sudo apt-get install python2.7 python2.7-dev
	    ;;
	pypy)
	    sudo add-apt-repository -y ppa:pypy/ppa
	    sudo apt-get -y update
	    sudo apt-get install -y pypy pypy-dev

	    # This is required because we need to get rid of the Travis installed PyPy
	    # or it'll take precedence over the PPA installed one.
	    sudo rm -rf /usr/local/pypy/bin
	    ;;
	docs)
	    sudo apt-get install libenchant-dev
	    ;;
	docs-spellcheck)
	    sudo apt-get install libenchant-dev
	    ;;
    esac
fi

sudo pip install virtualenv
virtualenv ~/.venv
source ~/.venv/bin/activate
pip install tox coveralls
