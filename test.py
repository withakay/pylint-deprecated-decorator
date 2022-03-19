from deprecation import deprecated


@deprecated(details="deprecation details")
def test_with_details() -> None:
    # should generate a warning from pylint with details
    pass



test_with_details()
