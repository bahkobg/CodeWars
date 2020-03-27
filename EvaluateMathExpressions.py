import re


def calc(expression):
    """
    Given a mathematical expression as a string you must return the result as a number.

    :param expression:  string - in format of (2 / (2 + 3.33) * 4) - -6
    :return: int - return the result as a number
    """

    # remove all whitespaces
    expression = re.subn("\s", "", expression)[0]

    def _basic_math(expression):
        if re.search("\(|\)", expression):
            return False
        elif re.search('(\d)\/(\d)', expression) or re.search('(\d)\*(\d)', expression):
            return "RESULT -> {}".format(expression)
        else:
            return False

    return _basic_math(expression)


tests = [
    ["434221 + 43421", 2],
    ["8/16", 0.5],
    ["3 -(-1)", 4],
    ["12 + -3232132", 0],
    ["10- 2- -5", 13],
    ["(((10)))", 10],
    ["3 * 5", 15],
    ["-7 * -(6 / 3)", 14]
]

for test in tests:
    print(calc(test[0]))
