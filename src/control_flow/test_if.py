"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """Check conditional behavior for both students' input values."""

    for number in [21, 34]:
        conclusion = ''

        if number < 0:
            conclusion = 'Number is less than zero'
        elif number == 0:
            conclusion = 'Number equals to zero'
        elif number < 1:
            conclusion = 'Number is greater than zero but less than one'
        else:
            conclusion = 'Number bigger than or equal to one'

        assert conclusion == 'Number bigger than or equal to one'
    
def test_multiple_elif_branches():
    """Classify scores using multiple elif branches."""

    for score, expected in [
        (90, 'Excellent'),
        (89, 'Good'),
        (70, 'Good'),
        (69, 'Pass'),
        (50, 'Pass'),
        (49, 'Fail'),
    ]:
        if score >= 90:
            result = 'Excellent'
        elif score >= 70:
            result = 'Good'
        elif score >= 50:
            result = 'Pass'
        else:
            result = 'Fail'

        assert result == expected
def test_nested_conditions():
    """Check entry permission using nested conditions."""

    for age, has_ticket, expected in [
        (18, True, 'Entry allowed'),
        (18, False, 'Ticket required'),
        (17, True, 'Too young'),
        (17, False, 'Too young'),
    ]:
        if age >= 18:
            if has_ticket:
                result = 'Entry allowed'
            else:
                result = 'Ticket required'
        else:
            result = 'Too young'

        assert result == expected