from astroid.nodes import Call, ClassDef, FunctionDef, Name, node_classes
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


__version__ = '0.2.0'
__author__ = 'Jack Rutherford (@withakay)'


class DeprecatedChecker(BaseChecker):
    """
    A pylint checker to detect @deprecated decorators on classes and functions

    Basic usage:

    `pylint --load-plugins=deprecated_checker --disable=all --enable=deprecated-decorators test.py`

    (where deprecated_checker is a python module that is in the PYTHONPATH)
    """

    # BaseChecker overrides
    __implements__ = IAstroidChecker
    name = "no-deprecated-decorator"
    priority = -1
    msgs = {
        "W9001": (
            "%s %s is deprecated. %s",
            name,
            "Functions and Classes that have been marked as @deprecated should not be used",
        )
    }

    message_name = name

    # an array of decorators to match against
    decorator_names = ["deprecated"]

    # There are various packages that implement a @deprecated_check decorator
    # in similar but slightly different ways.
    # change the `reason_keyword` value to the name of the argument you
    # want to capture the value of when outputting a linter warning.
    # Given:
    #
    #   `@deprecated(details="some reason")`
    #
    # `reason_keyword` would be set to "reason"
    #
    reason_keyword = "details"

    def __init__(self, linter=None) -> None:
        super().__init__(linter)

    def visit_decorators(self, node: node_classes.Decorators) -> None:
        # Check if the node has decorators
        if not node.nodes:
            return

        parent_type = "unknown"
        # Figure out whether it's a class or function
        # that is deprecated, and get relevant info
        if isinstance(node.parent, ClassDef):
            parent_type = "class"
        elif isinstance(node.parent, FunctionDef):
            parent_type = "function"
        parent_name = node.parent.name

        # Check each decorator to see if it's @deprecated_check
        for decorator in node.get_children():
            if isinstance(decorator, Call):

                if decorator.func.name in self.decorator_names:
                    reason = "No reason specified"
                    if decorator.keywords is not None:
                        for keyword in decorator.keywords:
                            if keyword.arg == self.reason_keyword:
                                reason = f'"{keyword.value.value}"'
                    self.add_message(
                        msgid=self.message_name,
                        node=node.parent,
                        args=(parent_type, parent_name, reason),
                    )
            elif isinstance(decorator, Name):
                if decorator.name in self.decorator_names:
                    self.add_message(
                        msgid=self.message_name,
                        node=node.parent,
                        args=(
                            parent_type,
                            parent_name,
                            "No reason specified",
                        ),
                    )

def register(linter) -> None:
    linter.register_checker(DeprecatedChecker(linter))