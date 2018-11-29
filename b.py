import a

def g():
    a.f()
    print "name = " + __name__

if __name__ == "__main__":
    g()
