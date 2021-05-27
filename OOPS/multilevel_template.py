class A:
    def a_method(self):
        print("This is method from from A")

class B(A):
    def b_method(self):
        print("This is method from from B")

class C(B):
    def c_method(self):
        print("This is method from from C")

c = C()
c.a_method()
c.b_method()
c.c_method()