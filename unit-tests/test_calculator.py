from calculator import square

# def test_square():
#     try :
#         assert square(2) == 4
#     except AssertionError:
#         print("Sqaure of 2 is not 4")

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

