import inspect
from typing import Callable, Optional


def deprecated(
    details: Optional[str] = None
) -> Callable:
    """
    This is a decorator which can be used to mark functions
    and classes as deprecated. With `It will result in a warning
    being emitted when the function is used.

    :param details: details of the deprecation.
    """

    def decorator_wrapper(
        func: Optional[Callable]
    ) -> Callable:
        """
        The wrapper will either call into the decorator function returning the result,
        or return the decorator function ready to be called.

        if func is None then we are returning the decorator function
        Otherwise we are returning the result of the decorator function.

        The result of the decorator function is a wrapped function that was decorated,
        That when called will emit a warning.
        """

        def decorator(inner_func: Callable) -> Callable:
            def wrapped(*args, **kwargs):
                return inner_func(*args, **kwargs)

            return wrapped

        if func is None:
            return decorator

        return decorator(func)

    if isinstance(details, str):
        # @deprecated is used with a 'details' str.
        return decorator_wrapper(None)

    if inspect.isclass(details) or inspect.isfunction(details):
        # @deprecated is NOT used with a 'details' str.
        # so reason is a reference to the function or class being decorated.
        return decorator_wrapper(details)

    raise TypeError(repr(type(details)))
