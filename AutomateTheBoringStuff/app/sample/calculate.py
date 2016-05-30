class Calculate(object):
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

if __name__ == '__main__':
    calc = Calculate()
    result = calc.add(2, 3)
    print(result)