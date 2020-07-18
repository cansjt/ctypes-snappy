#!/usr/bin/env python

import snappy
import unittest

class TestCase(unittest.TestCase):
  def testSimple(self):
    for i in range(1, 100):
      buf = b'abcdefg' * i
      cstr = snappy.compress(buf)
      ustr = snappy.uncompress(cstr)
      self.assertEqual(buf, ustr)


if __name__ == '__main__':
  unittest.main()
