[![Build Status](https://travis-ci.org/intuitivetechnologygroup/formula-test-harness.svg?branch=master)](https://travis-ci.org/intuitivetechnologygroup/formula-test-harness)

# <a name='documentation'></a> Salt Formula Test Harness

* [Project Setup](#project-setup)
  - [Project File Structure](#file-structure)
* [Configuration](#configuration)
* [Testing](#testing)
  - [Run Tests](#run-tests)
  - [Run Interactive Containers](#run-containers)
  - [Continuous Integration](#ci)
* [Components](#components)

---

Run as many pytest suites that you need to run in a clean, isolated environment.

#### Assumptions:

`make` is on your system and available. If it is not or you are not sure what
`make` is, [this](https://www.gnu.org/software/make/) is a good place to start.


## <a name='project-setup'></a> Project Setup

##### Clone this repository:

```bash
cd /path/to/project
mkdir tmp
git clone https://github.com/intuitivetechnologygroup/formula-test-harness.git tmp/formula-test-harness
```

##### Copy essentials:

Merge the files if they already exist in the project.
Replace `FORMULA-NAME` with the name of your formula.

```bash
cd /path/to/project
mkdir -p tests/srv/salt

cp -r tmp/formula-test-harness/tools tools
cp -r tmp/formula-test-harness/tests/pytests tests/pytests
cp tmp/formula-test-harness/.gitignore .gitignore

cp tmp/formula-test-harness/.travis.yml .travis.yml
sed -i '' 's/example/FORMULA-NAME/' .travis.yml

cp tmp/formula-test-harness/Makefile Makefile
sed -i '' 's/example/FORMULA-NAME/' Makefile

cp tmp/formula-test-harness/tests/srv/salt/top.sls tests/srv/salt/top.sls
sed -i '' 's/example/FORMULA-NAME/' tests/srv/salt/top.sls
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
├── .gitignore
├── .travis.yml
└── Makefile
````

### pytests

* Create your test sequences in `tests/pytests/`.
* The file structures should be setup the same way as any other python unit tests.
* Each test suite is essentially it's own python package so it must contain an `__init__.py` file.
* All test files must be in prefixed with `test_`.


## <a name='development'></a> Development

### <a name='dev-setup'></a> Setup

**Start a virtualenv**

```bash
pip install -U virtualenv
virtualenv .venv
source .venv/bin/activate
```

**Install local requirements**

```bash
make setup
```

### <a name='dev-utility-implementations'></a> Utility Implementations

#### Tool Configuration

##### `./tools/templates/Dockerfile.j2`

Add any package installation requirements here.

##### `./tools/run-tests.sh`

Add the shell commands to run the tests here.

#### Execution Files

The tooling config/execution files should be placed under `./tests/<util-name>/*`


## <a name='testing'></a> Testing

First, follow the [Development Setup](#dev-setup) instructions.

### <a name='run-tests'></a> Run Tests

Tests will be run on the following base images:

* `simplyadrian/allsalt:centos_master_2017.7.2`
* `simplyadrian/allsalt:debian_master_2017.7.2`
* `simplyadrian/allsalt:opensuse_master_2017.7.2`
* `simplyadrian/allsalt:ubuntu_master_2016.11.3`
* `simplyadrian/allsalt:ubuntu_master_2017.7.2`

##### Run the tests

* `make test-centos_master_2017.7.2`
* `make test-debian_master_2017.7.2`
* `make test-opensuse_master_2017.7.2`
* `make test-ubuntu_master_2016.11.3`
* `make test-ubuntu_master_2017.7.2`

### <a name='run-containers'></a> Run Interactive Containers

* `make local-centos_master_2017.7.2`
* `make local-debian_master_2017.7.2`
* `make local-opensuse_master_2017.7.2`
* `make local-ubuntu_master_2016.11.3`
* `make local-ubuntu_master_2017.7.2`

### <a name='ci'></a> Continuous Integration

[![Build Status](https://travis-ci.org/intuitivetechnologygroup/formula-test-harness.svg?branch=master)](https://travis-ci.org/intuitivetechnologygroup/formula-test-harness)

Continuous integration details are available on [Travis CI](https://travis-ci.org/intuitivetechnologygroup/formula-test-harness).


## <a name='components'></a> Components

### Dockerfile Template

Rendering a dockerfile:

```bash
python tools/filltmpl.py {formula-name} {image-tag}
```
