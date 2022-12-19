import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '40 \n 60'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('[\w,\W]*100[\w,\W]*', lines[0])
    assert res != None
    print(res.group())

    res = re.search('[\w,\W]*40[\w,\W]*60[\w,\W]*', lines[1])
    assert res != None
    print(res.group())

    res = re.search('[\w,\W]*40\.00[\w,\W]*60\.00[\w,\W]*', lines[2])
    assert res != None
    print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10 \n 20'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('[\w,\W]*30[\w,\W]*', lines[0])
    assert res != None
    print(res.group())

    res = re.search('[\w,\W]*10[\w,\W]*20[\w,\W]*', lines[1])
    assert res != None
    print(res.group())

    res = re.search('[\w,\W]*33\.33[\w,\W]*66\.67[\w,\W]*', lines[2])
    assert res != None
    print(res.group())
