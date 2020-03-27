import re


def calc(expression):
    """
    Given a mathematical expression as a string you must return the result as a number.

    :param expression:  string - in format of (2 / (2 + 3.33) * 4) - -6
    :return: int - return the result as a number
    """

    # remove all whitespaces
    expression = ''.join(expression.split()).replace('+-', '-').replace('--', '+')

    def _calc(expression):
        pass

    def _basic_math(expression):
        if re.search("\(|\)", expression):
            return None
        elif re.search('(-[0-9]+|[0-9]+)\*(-[0-9]+|[0-9]+)', expression):
            print(expression)
            try:
                result = re.search('(-[0-9]+|[0-9]+)\*(-[0-9]+|[0-9]+)', expression)
                result = int(result.group().split('+')[0]) + int(result.group().split('+')[1])
                return "COULD BE CALC WITH BASIC MATH", re.sub('(-[0-9]+|[0-9]+)\+(-[0-9]+|[0-9]+)', str(result), expression)
            except:
                return None
        elif re.search('(-[0-9]+|[0-9]+)\\(-[0-9]+|[0-9]+)', expression):
            print(expression)

    return _basic_math(expression)


tests = [
    ["1 + 1", 2],
    ["8/16", 0.5],
    ["3 -(-1)", 4],
    ["2 + -2", 0],
    ["10- 2- -5", 13],
    ["(((10)))", 10],
    ["3 * 5", 15],
    ["-7 * -(6 / 3)", 14]
]

for test in tests:
    print(calc(test[0]))
