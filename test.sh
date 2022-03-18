#!/usr/bin/env bash
echo "Expect 2 errors"
PYTHONPATH="$PYTHONPATH:$PWD/pylint_deprecated_decorator" \
pylint --load-plugins=deprecated_decorator --disable=all --enable=no-deprecated-decorator \
tests/test_pylint_deprecated_decorator.py