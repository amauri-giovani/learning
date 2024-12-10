multiple_of = lambda base, num: num % base == 0


def robot(pos):
    say = str(pos)
    if multiple_of(3, pos) or multiple_of(5, pos):
        say = 'fizzbuzz'
    elif multiple_of(3, pos):
        say = 'fizz'
    elif multiple_of(5, pos):
        say = 'buzz'
    return say


def assert_equal(result, expected):
    from sys import _getframe

    msg = "Fail: Line {} got {} expecting {}"

    if not result == expected:
        current = _getframe()
        caller = current.f_back
        line_no = caller.f_lineno
        # print('caller', line_no)
        print(msg.format(line_no, result, expected))


assert_equal(robot(1), '1')
assert_equal(robot(2), '2')
assert_equal(robot(4), '4')
assert_equal(robot(3), 'fizz')
assert_equal(robot(6), 'fizz')
assert_equal(robot(9), 'fizz')
assert_equal(robot(5), 'buzz')
assert_equal(robot(10), 'buzz')
assert_equal(robot(20), 'buzz')
assert_equal(robot(15), 'fizzbuzz')
assert_equal(robot(30), 'fizzbuzz')
assert_equal(robot(45), 'fizzbuzz')
