#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
        tests the github client
    """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": True})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, test_payload, mock_get_json):
        """
            test the org object method
        """
        mock_get_json.return_value = MagicMock(return_value=test_payload)
        obj = GithubOrgClient(org_name)
        self.assertEqual(obj.org(), test_payload)
        mock_get_json.assert_called_once_with(
                      obj.ORG_URL.format(org=obj._org_name))
