'''
제 1장 7번 문제
'''
import unittest
import datetime


def same_date(date):
  reverse_num_2 = bin(date)[2:][::-1]
  if(date == int('0b'+str(reverse_num_2), 2)):
    return date
  else:
    return ''

def answer(start_date, end_date):
  result = []
  for i in range(start_date, end_date+1):
    try:
      date = datetime.datetime.strptime(str(i), '%Y%m%d').date()
      if same_date(i) != '':
        result.append(i)
    except:
      i+=1
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
