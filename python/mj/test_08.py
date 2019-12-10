'''
제 1장 8번 문제
'''
import unittest

N = 12


def answer(log):
    if len(log) == N + 1:  # 12회 모두 이동할 경우 경로 탐색 종료
        return 1

    cnt = 0

    # Nested List
    # a = ['a', 'b', 'c']
    # n = [1, 2, 3]
    # x = [a, n]
    # x
    ## [['a', 'b', 'c'], [1, 2, 3]]
    # x[0]
    ## ['a', 'b', 'c']
    # x[0][1]
    # 'b'

    for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        # log[-1] 이면 뒤에서 1번째 요소(가장 마지막에 추가된 값)
        # 마지막 요소의 사방을 next_post로 두고 탐색
        next_pos = [log[-1][0] + d[0], log[-1][1] + d[1]]

        check = False
        for p in log:
            if p[0] == next_pos[0] and p[1] == next_pos[1]:  # log기록된 것에 포함이 되어있으면 skip
                check = True
        if check == False:  # 한 번도 logging된 적이 없는 좌표면
            cnt += answer(log + [next_pos])

    return cnt


class Test08(unittest.TestCase):
    '''
    로봇이 12회 이동할 때, 생각할 수 있는 이동 경로의 패턴이 몇 가지인지 구해 보세요.
    '''

    def test_answer(self):
        self.assertEqual(324932, answer([[0, 0]]))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test08)
    unittest.TextTestRunner(verbosity=2).run(suite)
