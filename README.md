# pylint-deprecated-decorator
A pylint checker to detect and @deprecated decorators on classes and functions.
Warns when classes and functions are being called that are decorated with @deprecated. 
Intended to be used in conjunction with a library like https://pypi.org/project/deprecation/.

Given some python code like
```
from deprecation import deprecated


@deprecated(details="Replaced by new_function")
def old_function() -> None:
    pass
    
old_function()
```

We can get a pylint warning like
```
example.py:4:0: W9001: function old_function is deprecated. Replaced by new_function (no-deprecated-decorator)
```

# Instalation

Install via pip e.g. `python -m pip install pylint-deprecated-decorator`

# Usage

To run the check we need to tell pylint to load the plugin and if you have --disable=all set, optionally enable the check

`pylint --load-plugins=deprecated_decorator --disable=all --enable=no-deprecated-decorator some_module.py`

This can also be configured in the `.pylintrc`. Consult the pylint documentation for more information.
