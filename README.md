[![Build Status](https://travis-ci.org/intuitivetechnologygroup/formula-test-harness.svg?branch=master)](https://travis-ci.org/intuitivetechnologygroup/formula-test-harness)

# Salt Formula Test Harness

* [Install](#install)
  - [Project File Structure](#file-structure)
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

##### Clone this repository:

```bash
cd /path/to/project
mkdir -p tmp/formula-test-harness
git clone git@github.com:intuitivetechnologygroup/formula-test-harness.git tmp/formula-test-harness
```

##### Copy essentials:

Merge the files if they already exist in the project.

```bash
cd /path/to/project
cp -r tmp/formula-test-harness/tools tools
mkdir -p tests/srv/salt
cp -r tmp/formula-test-harness/tests/pytests tests/pytests

cp tmp/formula-test-harness/.travis.yml .travis.yml
sed -i '' 's/example/formula-name/' .travis.yml

cp tmp/formula-test-harness/Makefile Makefile
sed -i '' 's/example/formula-name/' Makefile

cp tmp/formula-test-harness/tests/srv/salt/top.sls tests/srv/salt/top.sls
sed -i '' 's/example/formula-name/' tests/srv/salt/top.sls
```

### <a name='file-structure'></a> Project File Structure

````
.
├── example
│   ├── init.sls
│   └── pkg.sls
├── tests
│   ├── pytests
│   │   └── apply-all-tests
│   │       ├── __init__.py
│   │       └── test_000_apply_state.py
│   └── srv
│       ├── pillar
│       │   ├── example
│       │   │   └── init.sls
│       │   └── top.sls
│       └── salt
│           └── top.sls
├── tools
│   ├── templates
│   │   └── Dockerfile.j2
│   ├── filltmpl.py
│   └── run-tests.sh
├── .travis.yml
└── Makefile
````


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
* `simplyadrian/allsalt:opensuse_master_2017.7.2`
* `simplyadrian/allsalt:ubuntu_master_2016.11.3`
* `simplyadrian/allsalt:ubuntu_master_2017.7.2`

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

##### Run tests

* `make test-centos_master_2017.7.2`
* `make test-debian_master_2017.7.2`
* `make test-opensuse_master_2017.7.2`
* `make test-ubuntu_master_2016.11.3`
* `make test-ubuntu_master_2017.7.2`

### <a name='run-containers'></a> Run Containers

* `make local-centos_master_2017.7.2`
* `make local-debian_master_2017.7.2`
* `make local-opensuse_master_2017.7.2`
* `make local-ubuntu_master_2016.11.3`
* `make local-ubuntu_master_2017.7.2`


## <a name='components'></a> Components

### Dockerfile Template

Rendering a dockerfile:

```bash
python tools/filltmpl.py {formula-name} {image-tag}
```
