'''
제 1장 6번 문제
'''
import unittest

def collatz(n) :
  if n % 2 == 0 :
    return n/2
  else :
    return n * 3 + 1


def answer(num):
  i=2
  cnt=0

  while i <=num and i % 2 ==0: # num 이하의 짝수
    ans = i * 3 +1

    while True:
      ans = collatz(ans) 
      if  int(ans) == i:
        cnt += 1
        break
      elif collatz(ans) == 1:
        break
    
    i += 2

  return cnt

class Test06(unittest.TestCase):
    '''
    10,000 이하의 짝수 중 앞의 2나 4와 같이 '처음의 수로 돌아가는 수'가 몇 개 있는지 구해보세요
    '''

    def test_answer(self):
        '''
        10000 이하는 34개
        '''
        self.assertEqual(34, answer(10000))
    def test_example2(self):

        '''
        숫자를 늘려도 여전히 34개!
        '''
        self.assertEqual(34, answer(100000))

if __name__ == '__main__':
    '''
    unittest.main() 으로 호출하여 테스트를 진행하면 전체 OK, Not OK 여부가 나오고
    아래와 같이 두줄을 표시해 주면 상단의 test_answer ... ok, test_example ... ok 와 같이 출력됨.
    '''
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test06)
    unittest.TextTestRunner(verbosity=2).run(suite)
