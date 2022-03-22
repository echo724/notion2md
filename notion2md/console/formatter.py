def error(msg):
    return f"\n<error>{'ERROR'+' ':>12}</error>{msg}\n"


def status(status, msg):
    return f"<status>{status+' ':>12}</status>{msg}"


def success(status, msg):
    return f"<success>{status+' ':>12}</success>{msg}"
