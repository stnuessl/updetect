#
# Simple makefile to conveniently run the most important commands
#

PACKAGE_VERSION = $(shell PYTHONPATH=src python scripts/pyproject-version.py)

BUILD_DIR = build
PACKAGE_TARBALL = $(BUILD)/updetect-$(PACKAGE_VERSION).tar.gz
PACKAGE_WHEEL = $(BUILD)/updetect-$(PACKAGE_VERSION)-py3-none-any.whl
PACKAGE_FILES = $(PACKAGE_TARBALL) $(PACKAGE_WHEEL)

VENV_DIR = $(BUILD_DIR)/venv
VENV_PYTHON = $(VENV_DIR)/bin/python

all: package

clean:
	rm -rf $(BUILD_DIR) src/updetect.egg-info

package: $(PACKAGE_FILES)

release: $(PACKAGE_FILES) $(VENV_PYTHON)
	PACKAGE_VERSION=$(PACKAGE_VERSION) \
	VENV_PYTHON=$(VENV_PYTHON) \
		bash scripts/pypi-release.sh $^

test:
	PYTHONPATH=src python tests/test-updetect.py
	PYTHONPATH=src bash tests/test-updetect.sh

$(PACKAGE_FILES)&:
	python -m build --outdir $(BUILD_DIR)

$(VENV_PYTHON):
	python -m venv $(VENV_DIR)

# FIXME
# Move creation virtual environment here
# Read out project version here

.PHONY: all clean package test release
