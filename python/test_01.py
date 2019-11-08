'''
제 1장 1번 문제
'''
import unittest

# python unittest (https://docs.python.org/ko/3/library/unittest.html)


def answer(num):
    '''
    str[시작:끝:증감] , 시작 <= index < 끝
    '''
    while True:
        if str(num) == str(num)[::-1] \
                and bin(num)[2:] == bin(num)[2:][::-1] \
                and oct(num)[2:] == oct(num)[2:][::-1]:
            break
        else:
            num += 2
    return num


class Test01(unittest.TestCase):
    '''
    10/2/8진수 모두가 대칭수가 되는 수 중에 10(10진수)이상에서의 최솟값 구하기
    '''

    def test_example(self):
        '''
        예제 9
        '''
        self.assertEqual(9, answer(9))

    def test_answer(self):
        '''
        정답 585
        '''
        self.assertEqual(585, answer(11))


if __name__ == '__main__':
    '''
    unittest.main() 으로 호출하여 테스트를 진행하면 전체 OK, Not OK 여부가 나오고
    아래와 같이 두줄을 표시해 주면 상단의 test_answer ... ok, test_example ... ok 와 같이 출력됨.
    '''
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test01)
    unittest.TextTestRunner(verbosity=2).run(suite)
