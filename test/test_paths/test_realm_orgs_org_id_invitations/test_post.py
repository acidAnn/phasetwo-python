# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import phasetwo
from phasetwo.paths.realm_orgs_org_id_invitations import post  # noqa: E501
from phasetwo import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRealmOrgsOrgIdInvitations(ApiTestMixin, unittest.TestCase):
    """
    RealmOrgsOrgIdInvitations unit test stubs
        Create an invitation to an organization  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 201
    response_body = ''




if __name__ == '__main__':
    unittest.main()
