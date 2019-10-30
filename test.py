#!/usr/bin/env python3

import unittest

from ubiodexapi import create_app

class TestUbiodexApi(unittest.TestCase):

	def setUp(self):
		self.app = create_app().test_client()

	def test_index(self):
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()
