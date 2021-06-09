import unittest
from CalcOps import SimpleOps as so


class MyTestCase(unittest.TestCase):

    def test_add(self):
        for i in range(-2, 2):
            for j in range(-2, 2):
                self.assertEqual(so.add(i, j), (i + j))

    def test_sub(self):
        for i in range(-2, 2):
            for j in range(-2, 2):
                # print(so.sub(i, j), "->", (1 - j))
                self.assertEqual(so.sub(i, j), (i - j))

    def test_mul(self):
        for i in range(-2, 2):
            for j in range(-2, 2):
                self.assertEqual(so.mul(i, j), (i * j))

    def test_div(self):
        for i in range(-2, 3):
            for j in range(-2, 3):
                if j == 0:
                    self.assertEqual(so.div(i, j), 0)
                else:
                    self.assertEqual(so.div(i, j), round((i / j), 2))

    def test_neg(self):
        for i in range(-2, 2):
            self.assertEqual(so.mul(i, -1), (i * -1))


if __name__ == '__main__':
    unittest.main()
