import unittest, random
from hw2 import get_dict as hwgd
from as2 import get_dict as asgd

class TestHomework(unittest.TestCase):
    def setUp(self):
        self.asd = hwgd()
        self.hwd = hwgd()
    
    def test_homework_2(self):
        for i in range(1, 101):
            self.assertEqual(self.asd[str(i)], self.hwd[str(i)])
        for i in range(20):
            x = random.randint(- 200, 0)
            self.assertNotIn(str(x), self.hwd)
        for i in range(20):
            x = random.randint(101, 300)
            self.assertNotIn(str(x), self.hwd)
        self.assertEqual(self.hwd, self.asd)

unittest.main()
