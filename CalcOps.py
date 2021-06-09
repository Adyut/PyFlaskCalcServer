class SimpleOps:
    def __init__(self):
        pass

    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def sub(num1, num2):
        return num1 - num2

    @staticmethod
    def mul(num1, num2):
        return num1 * num2

    @staticmethod
    def div(num1, num2):
        if num2 == 0:
            return 0.0
        return round(num1 / num2, 2)
