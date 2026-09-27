class consicutive:
    def __init__(self,a):
        self.a = a
    def check(self):
        if self.a <= 1:
            return False
        else:
            for i in range(2, int(self.a ** 0.5) + 1):
                if self.a % i == 0:
                    return False
            return True
for i in range(1000):
        if (consicutive(i).check() and consicutive(i + 2).check()):
            print(f"({i}, {i+2})")
