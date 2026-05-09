#!/usr/bin/env python3
"""Simple smoke test to check if the package is properly installed and can be imported without errors."""

from captainplanet import EnvironmentVariable

_TEST_DEFAULT = "This is a test variable."
_TEST_SET = "This is a test variable that has been set."

TEST_VAR = EnvironmentVariable("TEST_VARIABLE", str, default_value=_TEST_DEFAULT)
assert TEST_VAR.get() == _TEST_DEFAULT

TEST_VAR.set(_TEST_SET)
assert TEST_VAR.get() == _TEST_SET
