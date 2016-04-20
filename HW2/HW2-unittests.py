import unittest
import subprocess
import requests
import sys

port = '49160'
hostname = 'localhost'

class TestHW2(unittest.TestCase):

    def setUp(self):
        global hostname, port
        self.s = 'http://'+hostname+':'+port

    def test_a_put_nonexistent_key(self):
        res = requests.put(self.s+'/kvs/foo',data = {'val':'bart'})
        d = res.json()
        self.assertEqual(res.status_code,201)
        self.assertEqual(d['replaced'],0)
        self.assertEqual(d['msg'],'success')

    def test_b_put_existing_key(self):
        res = requests.put(self.s+'/kvs/foo',data= {'val':'bart'})
        d = res.json()
        self.assertEqual(d['replaced'],1)
        self.assertEqual(d['msg'],'success')

    def test_c_get_nonexistent_key(self):
        res = requests.get(self.s+'/kvs/faa')
        d = res.json()
        self.assertEqual(res.status_code,404)
        self.assertEqual(d['msg'],'error')
        self.assertEqual(d['error'],'key does not exist')

    def test_d_get_existing_key(self):
        res = requests.get(self.s+'/kvs/foo')
        d = res.json()
        self.assertEqual(d['msg'],'success')
        self.assertEqual(d['value'],'bart')

    def test_e_del_nonexistent_key(self):
        res = requests.delete(self.s+'/kvs/faa')
        d = res.json()
        self.assertEqual(res.status_code,404)
        self.assertEqual(d['msg'],'error')
        self.assertEqual(d['error'],'key does not exist')

    def test_f_del_existing_key(self):
        res = requests.delete(self.s+'/kvs/foo')
        d = res.json()
        self.assertEqual(d['msg'],'success')

if __name__ == '__main__':
    unittest.main()
