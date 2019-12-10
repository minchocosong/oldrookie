'''
제 1장 9번 문제
'''
import unittest


def answer():
    boy, girl = 20, 10
    boy, girl = boy+1, girl+1

    ary = [0] * (boy * girl)
    ary[0] = 1

    for g in range(0, girl):
        for b in range(0, boy):
            if (b != g) and (boy - b != girl - g):
                if b > 0:
                    ary[b + boy * g] += ary[b-1 + boy*g]

                if g > 0:
                    ary[b + boy * g] += ary[b+boy*(g-1)]
    return ary[-2] + ary[-boy-1]


class Test09(unittest.TestCase):
    '''
    A 20, B 10의 '조합'에서 , 2그룹으로 나누었을 때 그룹당 A와 B의 비율이 일치하지 않는 경우 카운트 
    '''

    def test_answer(self):
        self.assertEqual(2417416, answer())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test09)
    unittest.TextTestRunner(verbosity=2).run(suite)
