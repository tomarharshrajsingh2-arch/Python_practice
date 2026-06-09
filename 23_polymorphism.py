class One:
    def do_it(self):
        print("do it from one")

    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("do it from two")
one = One()
two = Two()
one.doanything()
two.doanything()