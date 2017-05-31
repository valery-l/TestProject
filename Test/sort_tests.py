import subprocess, unittest, os
from shutil import copyfile
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

def runTest(num):
      copyfile('input_test' + num + '.txt', 'input.txt')
      subprocess.call('./Sort', timeout=10)
      with open ('output.txt', 'r') as output_file:
          result=output_file.readlines()
      with open ('output_test' + num +'.txt', "r") as output_test_file:
          test_result=output_test_file.readlines()
      return result, test_result

class TestSortProgramm(unittest.TestCase):

  def tearDown(self):
      os.remove('output.txt')
      os.remove('input.txt')

  def test_input1(self):
      result, test_result = runTest('1')
      self.assertEqual(result, test_result)
      
  def test_input2(self):
      result, test_result = runTest('2')
      self.assertEqual(result, test_result)
      
  def test_input3(self):
      result, test_result = runTest('3')
      self.assertEqual(result, test_result)
      
if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)