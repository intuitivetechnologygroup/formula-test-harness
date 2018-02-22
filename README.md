# Salt Formula Test Harness

Formulas to set up authconfig and sssd on Linux systems.

**Note:**
See the full Salt Formulas installation and usage instructions
<http://docs.saltstack.com/en/latest/topics/development/conventions/formulas.html>.

**Assumptions:**
`make` is on your system and available. If it is not or you are not sure what
`make` is, [this](https://www.gnu.org/software/make/) is a good place to start.


## Testing

The ***Makefile*** is located in the project base directory.

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


## Available states

### `authconfig`
Install SSSD and its dependencies on both RHEL|CentOS and Ubuntu|Debian. The
default state will detect your OS based on default grains and run the
corresponding state file

### `authconfig.redhat`

Handles the installation of SSSD and its dependencies on a RHEL|CentOS system.

### `authconfig.ubuntu`

Handles the installation of SSSD and its dependencies on a Ubuntu|Debian system.


## Pillar customizations

Any of these values can be overwritten in a pillar file. If you do find yourself needing
more overrides follow the example below.


## Pillar customizations

[pillar.example](authconfig/tests/pillar/authconfig/init.sls)
