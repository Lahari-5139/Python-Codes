class wholeNum(Exception):
    def __init__(self, exp,kuchBhi):
        self.exp = exp
        self.kuchBhi = kuchBhi

    def message(self,msg):
        return msg

x = input()
def r(x):
    if int(x) != x:
        raise wholeNum("The number you entered is not a whole number",'Koi toh')
r(x)
try:
    y = input()
    r(y)
except wholeNum as e:
    print "Kuch toh gadbad", e.message('koi message')
