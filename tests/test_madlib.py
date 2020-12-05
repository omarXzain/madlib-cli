from madlib import __version__
from madlib_cli.madlib import read, parse, write, merge


def test_version():
    assert __version__ == '0.1.0'

def test_read():
    with open('assets/your_answer.txt') as f:
        contents = f.read()
        actual = contents
        expected = contents
        assert actual == expected


def test_parse():
    expected = ["name", "adjective"]
    received = parse("hello {name}, I am a {adjective} person")
    assert expected == received


def test_merge():
    words = ['hungry', 'eat', 'find']
    text = 'i was {} and i had to {} a fruit becuase i couldnt {} anything'
    received = merge(text, words)
    expected = 'i was hungry and i had to eat a fruit becuase i couldnt find anything'
    assert expected == received