# swpp18-team4

[![Coverage Status](https://coveralls.io/repos/github/cki86201/swpp18-team4/badge.svg)](https://coveralls.io/github/cki86201/swpp18-team4)
[![Build Status](https://travis-ci.org/cki86201/swpp18-team4.svg?branch=master)](https://travis-ci.org/cki86201/swpp18-team4)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

# How to run
## Frontend
 - ng serve --proxy-config proxy.conf.json
## Backend
 - python manage.py runserver

# How to test
## Frontend
we use Jasmine & Karma for angular testing
- npm install
- ng test --code-coverage
- http-server -c-1 -o -p 9875 ./coverage
## Backend
- coverage run --source='./user' manage.py test
- coverage run --branch --source='./user' manage.py test
- coverage report


