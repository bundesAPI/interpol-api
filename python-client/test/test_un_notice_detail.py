"""
    Interpol Notices API

    Interpol Red, Yellow and UN Notices API  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.interpol.model.red_notice_detail_embedded import (
    RedNoticeDetailEmbedded,
)
from deutschland.interpol.model.un_notice_detail_links import UNNoticeDetailLinks

from deutschland import interpol

globals()["RedNoticeDetailEmbedded"] = RedNoticeDetailEmbedded
globals()["UNNoticeDetailLinks"] = UNNoticeDetailLinks
from deutschland.interpol.model.un_notice_detail import UNNoticeDetail


class TestUNNoticeDetail(unittest.TestCase):
    """UNNoticeDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUNNoticeDetail(self):
        """Test UNNoticeDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UNNoticeDetail()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
