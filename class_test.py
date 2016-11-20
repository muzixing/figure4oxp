class A(object):
    def __init__(self):
        pass

if __name__ == '__main__':

    test = A()
    test.haha = 0
    print test.__dict__
    print A().__dict__
    # print diff(test, A)
