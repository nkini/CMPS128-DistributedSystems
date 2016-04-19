import unittest
import subprocess
import requests

class TestHW1(unittest.TestCase):

  def test_everything(self):
      #output = subprocess.check_output('curl -X GET http://localhost:49160/hello',shell=True)
      res = requests.get('http://localhost:49160/hello')
      self.assertEqual(res.text, 'Hello world!', msg='GET on the hello resource did not execute successfully')

      #def test_echo_get(self):
      #output = subprocess.check_output(['curl', '-X', 'GET', 'http://localhost:49160/echo'])
      res = requests.get('http://localhost:49160/echo')
      self.assertEqual(res.text, '', msg='GET echo without a msg =. Should have output a blank.')
      #output = subprocess.check_output(['curl', '-X', 'GET', 'http://localhost:49160/echo?msg=AnyColourYouLike'])
      res = requests.get('http://localhost:49160/echo?msg=AnyColourYouLike')
      self.assertEqual(res.text, 'AnyColourYouLike', msg='GET echo with a message did not execute successfully')

      #def test_invalid_output(self):
      #output = subprocess.check_output(['curl', '-s', '-i', '-X', 'GET', 'http://localhost:49160/anUnknownMethod', '|', 'head -n 1'])
      res = requests.get('http://localhost:49160/anUnknownMethod')
      self.assertEqual(res.status_code, 404, msg='GET on random unknown resource should have failed, but did not.')

      #output = subprocess.check_output(['curl', '-s', '-i', '-X', 'POST', 'http://localhost:49160/hello', '|', 'head -n 1'])
      res = requests.post('http://localhost:49160/hello')
      self.assertNotEqual(res.status_code, 200, msg='POST on hello should not have worked, but returned successfully.')
      self.assertEqual(res.status_code, 405, msg='POST should have returned a 405 METHOD NOT ALLOWED.')


if __name__ == '__main__':
    unittest.main()
