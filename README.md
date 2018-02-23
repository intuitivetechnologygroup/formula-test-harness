# Salt Formula Test Harness

* [Install](#install)
* [Configuration](#configuration)
* [Testing](#testing)
  - [Run Tests](#run-tests)
  - [Run Containers](#run-containers)
* [Components](#components)

---

**Assumptions:**

`make` is on your system and available. If it is not or you are not sure what
`make` is, [this](https://www.gnu.org/software/make/) is a good place to start.


## <a name='install'></a> Install

[placeholder]


## <a name='configuration'></a> Configuration

Update the `FORMULA_NAME` variable in the `Makefile`:

````
FORMULA_NAME = "my-formula"
````


## <a name='testing'></a> Testing

### <a name='run-tests'></a> Run Tests

Tests will be run on the following base images:

* `simplyadrian/allsalt:centos_master_2017.7.2`
* `simplyadrian/allsalt:debian_master_2017.7.2`
* `simplyadrian/allsalt:ubuntu_master_2017.7.2`
* `simplyadrian/allsalt:ubuntu_master_2016.11.3`

##### Start a virtualenv

```bash
pip install -U virtualenv
virtualenv .venv
source .venv/bin/activate
```

##### Install local requirements

```bash
make setup
```

#### Run tests

* `make test-centos_master_2017.7.2`
* `make test-debian_master_2017.7.2`
* `make test-ubuntu_master_2017.7.2`
* `make test-ubuntu_master_2016.11.3`

### <a name='run-containers'></a> Run Containers

* `make local-centos_master_2017.7.2`
* `make local-debian_master_2017.7.2`
* `make local-ubuntu_master_2017.7.2`
* `make local-ubuntu_master_2016.11.3`


## <a name='components'></a> Components

### Dockerfile Template

Rendering a dockerfile:

```bash
python tools/filltmpl.py {formula-name} {image-tag}
```
