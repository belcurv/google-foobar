import pytest
import solution as module

class TestSolution:
    def testCanary(self):
        assert 1 == 1

    def testCaseOne(self):
        expected = []
        actual = module.solution1([1, 2, 3], 0)
        assert actual == expected

    def testCaseTwo(self):
        expected = [1,4]
        actual = module.solution1([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
        assert actual == expected

    def testCaseOne2(self):
        expected = []
        actual = module.solution2([1, 2, 3], 0)
        assert actual == expected

    def testCaseTwo2(self):
        expected = [1,4]
        actual = module.solution2([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
        assert actual == expected

    def testCaseOne3(self):
        expected = []
        actual = module.solution3([1, 2, 3], 0)
        assert actual == expected

    def testCaseTwo3(self):
        expected = [1,4]
        actual = module.solution3([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
        assert actual == expected
