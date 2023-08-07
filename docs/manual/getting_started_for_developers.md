# Getting Started for Developers

This project uses *tox* as a central build management tool.

Install tox and show all available commands (environments):

```bash
$ pip3 install -r requirements.txt
$ tox -a -v
```

The first call of tox usually takes some time, further calls are faster.

**Note:** Windows users can use `python -m tox` in case of problems.


## Generate HTML Documentation

Generate documentation which is placed at `build/docs/`:

```bash
$ tox -e docs
```


## Run Unit Tests

Run unit tests in *developer*/*editable* mode:

```bash
$ tox --develop -e unit_tests
```


## Build Wheel Package

Build the wheel package with tox and an isolated environment is not yet possible.
It can be built with:

```bash
$ pip3 install build
$ python3 -m build --wheel .
```

It is located in `dist/`.
