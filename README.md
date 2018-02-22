# Salt Formula Test Harness

**Assumptions:**
`make` is on your system and available. If it is not or you are not sure what
`make` is, [this](https://www.gnu.org/software/make/) is a good place to start.


## Install

[placeholder]


## Testing

#### Start a virtualenv

```bash
pip install -U virtualenv
virtualenv .venv
source .venv/bin/activate
```

* install requirements: `make test-setup`
* run a test:
  - `make test_centos_master_2017.7.2`
  - `make test_debian_master_2017.7.2`
  - `make test_ubuntu_master_2017.7.2`
  - `make test_ubuntu_master_2016.11.3`
* test results will return to your screen.
