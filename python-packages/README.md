## Python packages and documentation with Sphinx

This project has a couple of minimal python packages and one using the other, along with unit tests backing them. This is an attempt to use python packages/imports and sphinx documentation generator.

### Initialize project
```
$ virtualenv -v .venv
$ source .venv/bin/activate

$ pip install .
```

### Generate HTML documentation from source using sphinx
```
$ cd docs
$ make html

$ python3 -m http.server --directory docs/_build/html
```

#### Run a few things
```
$ python3 -m shapes

$ python3 -m unittest tests.api_test
$ python3 -m unittest tests.shapes_test
$ python3 -m unittest tests.mymath_test
```

References:
* Sphinx tutorials at https://buildmedia.readthedocs.org/media/pdf/brandons-sphinx-tutorial/latest/brandons-sphinx-tutorial.pdf and https://pythonhosted.org/an_example_pypi_project/sphinx.html#full-code-example
* Newton Raphsons algorithm for square root: https://www.youtube.com/watch?v=j6ikEASjbWE
