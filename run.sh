#!/bin/sh

if [ ! -d venv ]
then
    virtualenv venv || (echo "Failed to create virtual environment. Try running 'pip install virtualenv'" ; exit 1)
fi

source venv/bin/activate

pip install --requirement requirements.txt --upgrade

exec ./imgupload-server.py
