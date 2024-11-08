#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """
        tests the github client
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, test_payload: Dict, mock_get_json: MagicMock) -> None:
        """
            test the org object method
        """
        mock_get_json.return_value = MagicMock(return_value=test_payload)
        obj = GithubOrgClient(org_name)
        self.assertEqual(obj.org(), test_payload)
        mock_get_json.assert_called_once_with(
                      "https://api.github.com/orgs/{}".format(org_name))
