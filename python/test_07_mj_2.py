'''
제 1장 7번 문제
'''
import unittest
from datetime import datetime, timedelta


def answer(start, end):
  result = []
  start_date = datetime.strptime(str(start), '%Y%m%d')
  end_date = datetime.strptime(str(end), '%Y%m%d')

  while start_date <= end_date :
    start_date_integer = int(start_date.strftime('%Y%m%d'))
    binary_date = bin(date)[2:]
    if(binary_date == binary_date[::-1]):
      result.append(start_date_integer)
    start_date += timedelta(days=1)
  return result
  
class Test07(unittest.TestCase):
    '''
    YYYYMMDD 8자리 10진수 -> 2진수 변화 -> 거꾸로 나열 -> 10진수 변환했을 때 최초의 수와 같은 경우 찾기 (19641010~20200724)
    '''

    def test_answer(self):
        '''
        1964/10/10 부터 2020/07/24 유효한 날에 한하여 탐색
        '''
        self.assertEquals([19660713, 19660905, 19770217, 19950617, 20020505, 20130201], answer(19641010, 20200724) )

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test07)
    unittest.TextTestRunner(verbosity=2).run(suite)
