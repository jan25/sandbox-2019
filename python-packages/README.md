
```
$ virtualenv -v .venv
$ source .venv/bin/activate

$ pip install .
```

```
$ cd docs
$ make html

$ cd _build
$ python3 -m http.server
```