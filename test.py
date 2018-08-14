from Lict import Lict
from random import randint
from unittest import TestCase

class Lict_tests(TestCase):
    def __init__(self, initItem):
        self.test_package_init(initItem)
        self.fill()
        self.test_order()
        self.test_setitem()
        self.test_insert()
        self.test_put()


    def test_package_init(self, item):
        self.test = Lict(item)
        assert self.test[1] == item


    def fill(self):
        for n in range(1, 1000):
            position = randint(1, 100)
            self.test.put(n, pos=position)


    def test_order(self):
        try:
            count = 1
            for k in self.test.keys():
                assert count == k
                count += 1

        except AssertionError:
            print("Assertion Error: {} != {}\n"
            "try:\n"
            "    for n in range(len(self.test)):\n"
            "        for k in self.test.data:\n"
            "            assert n == k\n".format(count, k))


    def test_setitem(self):
        previous2 = self.test[2]
        self.test[1] = 1001
        assert self.test[1] == 1001
        assert self.test[2] == previous2


    def test_insert(self):
        self.test.__insert__(1002, 1)
        assert self.test[1] == 1002


    def test_put(self):
        previous5 = self.test[5]
        self.test.put(1003, 5)
        self.test.put(1004)
        assert self.test[5] == 1003
        assert self.test[6] == previous5
        assert self.test[len(self.test)] == 1004
        
        self.assertRaises(TypeError, 
            self.test.put(5, 'a')
        with self.assertRaises(TypeError):
            self.test.put(5, 0)
        with self.assertRaises(TypeError):
            self.test.put(5, 3.5)


testy = Lict_tests('a')