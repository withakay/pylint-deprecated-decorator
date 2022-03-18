"""
To test `deprecated_checker` cd into the folder
this script is in and run pytest against this
file with the following command:

```
PYTHONPATH="$PYTHONPATH:$PWD" \
pylint --load-plugins=deprecated_checker --disable=all --enable=no-deprecated \
test_deprecated_checker.py
```

Note the plugin is named 'deprecated_checker'
(and this maps on to the deprecated_checker.py file)
and the check is called 'deprecated-decorator'
"""


from pylint_deprecated_decorator.deprecated_decorator import __version__
from mocked_deprecated_decorator import deprecated


def test_version():
    assert __version__ == '0.1.0'


@deprecated
def test_with_no_details() -> None:
    # should generate a warning from pylint with no extra details
    pass


@deprecated(details="this is test2's deprecation message")
def test_with_details() -> None:
    # should generate a warning from pylint with details
    pass


def test_with_no_decorator() -> None:
    # should be ignored
    pass


if __name__ == '__main__':
    test_with_no_details()
    test_with_details()
    test_with_no_decorator()