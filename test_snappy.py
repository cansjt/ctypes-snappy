#!/usr/bin/env python

import snappy
import unittest

class TestCase(unittest.TestCase):
  def testSimple(self):
    for i in range(1, 100):
      str = 'abcdefg' * i
      cstr = snappy.compress(str)
      ustr = snappy.uncompress(cstr)
      self.assertEqual(str, ustr)


if __name__ == '__main__':
  unittest.main()
