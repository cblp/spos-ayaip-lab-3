#!/usr/bin/env python3

import random
import subprocess


CONVERT_PROG = 'build/convert'


def convert(choice, number):
    input = '\n'.join([str(choice), number, str(4)]).encode()
    [result] = [
        line.split()[1].decode()
        for line in
            subprocess.check_output(CONVERT_PROG, input=input, timeout=1)
            .splitlines()
        if line.startswith(b'Result:')
    ]
    return result


def test_convert(choice, process_got, process_expected):
    def case(x):
        expected = process_expected(x)
        got = convert(choice, process_got(x))
        assert got == expected, {'got': got, 'expected': expected}

    case(0)
    for _ in range(100):
        case(random.randint(0, 1000000))


def encode2(x): return bin(x)[2:]


def encode8(x): return oct(x)[2:]


def encode16(x): return hex(x)[2:]


encode10 = str


def main():
    test_convert(1, encode16, encode10)
    test_convert(2, encode8,  encode10)
    test_convert(3, encode10, encode2)


if __name__ == '__main__':
    main()
