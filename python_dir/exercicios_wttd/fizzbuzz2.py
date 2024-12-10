multiple_of = lambda base, num: num % base == 0


def robot(pos):
    say = str(pos)
    if multiple_of(3, pos) and multiple_of(5, pos):
        say = 'fizzbuzz'
    elif multiple_of(3, pos):
        say = 'fizz'
    elif multiple_of(5, pos):
        say = 'buzz'
    return say



def call_robot(list_numbers, expected):
    for number in list_numbers:
        assert robot(number) == expected


for number in [1, 4, 13]:
    assert robot(number) == str(number)

call_robot([3, 6, 27], 'fizz')
call_robot([5, 20, 40], 'buzz')
call_robot([15, 45, 150], 'fizzbuzz')
