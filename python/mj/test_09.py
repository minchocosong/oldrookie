'''
제 1장 9번 문제  --> itertools사용, timeout (9개까지 ok)
'''
import unittest
import itertools


def answer(array):
    result = []
    for case in list(itertools.permutations(array, len(array))):
        cnt = 0
        for cut_pos in range(1, len(array)):
            a_cnt = 0
            b_cnt = 0
            for item in case[:cut_pos]:
                if item == 'A':
                    a_cnt += 1
                elif item == 'B':
                    b_cnt += 1
            if a_cnt != 0 and b_cnt != 0 and a_cnt == b_cnt:
                continue
            a_cnt = 0
            b_cnt = 0
            for item in case[cut_pos:]:
                if item == 'A':
                    a_cnt += 1
                elif item == 'B':
                    b_cnt += 1
            if a_cnt != 0 and b_cnt != 0 and a_cnt == b_cnt:
                continue
            # 두 그룹에서 모두 남자와 여자의 수가 다름
            cnt += 1
        # 어디에서 끊더라도 모두 비율이 다를 경우
        if cnt == len(array) - 1:
            result.append(case)
    print(list(set(result)))

    return len(list(set(result)))


class Test09(unittest.TestCase):
    '''
    A 20, B 10의 '조합'에서 , 2그룹으로 나누었을 때 그룹당 A와 B의 비율이 일치하지 않는 경우 카운트 
    '''

    def test_answer_6(self):
        self.assertEqual(4, answer(['A', 'A', 'A', 'B', 'B', 'B']))

    def test_answer_8(self):
        self.assertEqual(10, answer(['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B']))

    # def test_answer_10(self):
    #     self.assertEqual(0, answer(
    #         ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B']))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test09)
    unittest.TextTestRunner(verbosity=2).run(suite)
