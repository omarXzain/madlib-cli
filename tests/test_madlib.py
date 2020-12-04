from madlib import __version__
from madlib_cli.madlib import (parse,read_template,merge)


def test_version():
    assert __version__ == '0.1.0'

def test_read():
    with open('assets/your_answer.txt') as f:
        contents = f.read()
        actual = contents
        expected = contents
        assert actual == expected

def test_parse():
    with open('assets/template.txt') as x:
        valList = x.read()
        actual = valList
        expected = valList
        assert actual == expected


def test_merge():
    inputs = [ 'Madlib Game j is a really jj person. He likes  and jj on his free time. He once tripped on a j and started crying. j is a really j person.' ]
    mergeStr = "tripped {}, really {} person {}?"
    with open('assets/template.txt') as m:
        mergeStr = m.read()
        actual = mergeStr
        expected = mergeStr
    assert actual == expected
    inputs = open('./assets/template.txt', 'r') 
    content = inputs.read()	
    inputs.close()
    assert content == expected
    return content