def _parse_num_string(num_string):
    """
    Validates and splits a number string into sign, integer digits, and fractional digits.
    """
    if not isinstance(num_string, str):
        return (False, 1, "0", "")

    s = num_string.strip()
    if s == "":
        return (False, 1, "0", "")

    # Handle sign
    sign = 1
    if s[0] in "+-":
        if s[0] == "-":
            sign = -1
        s = s[1:]

    if s == "":
        return (False, 1, "0", "")

    # Only digits and at most one dot
    if s.count(".") > 1:
        return (False, 1, "0", "")

    for ch in s:
        if not (ch.isdigit() or ch == "."):
            return (False, 1, "0", "")

    # Must contain at least one digit
    if not any(ch.isdigit() for ch in s):
        return (False, 1, "0", "")

    if "." in s:
        left, right = s.split(".", 1)
    else:
        left, right = s, ""

    int_digits = left if left != "" else "0"
    frac_digits = right  # can be ""

    if not int_digits.isdigit():
        return (False, 1, "0", "")
    if frac_digits != "" and not frac_digits.isdigit():
        return (False, 1, "0", "")

    return (True, sign, int_digits, frac_digits)


# Conversion functions for characteristic and mantissa
def characteristic(num_string):
    """
    Extracts the characteristic (integer part) from a number string.
    """
    ok, sign, int_digits, frac_digits = _parse_num_string(num_string)
    if not ok:
        return (False, 0)

    return (True, sign * int(int_digits))


def mantissa(num_string):
    """
    Extracts the mantissa (fractional part) from a number string.
    """
    ok, sign, int_digits, frac_digits = _parse_num_string(num_string)
    if not ok:
        return (False, 0, 0)

    # No decimal point => no fractional digits
    if frac_digits == "":
        return (True, 0, 1)

    numerator = int(frac_digits)
    denominator = 10 ** len(frac_digits)
    return (True, numerator, denominator)


