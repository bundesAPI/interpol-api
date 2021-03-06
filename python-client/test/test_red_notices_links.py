"""
    Interpol Notices API

    Interpol Red, Yellow and UN Notices API  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.interpol.model.red_notices_links_last import RedNoticesLinksLast
from deutschland.interpol.model.red_notices_links_next import RedNoticesLinksNext
from deutschland.interpol.model.red_notices_links_self import RedNoticesLinksSelf

from deutschland import interpol

globals()["RedNoticesLinksLast"] = RedNoticesLinksLast
globals()["RedNoticesLinksNext"] = RedNoticesLinksNext
globals()["RedNoticesLinksSelf"] = RedNoticesLinksSelf
from deutschland.interpol.model.red_notices_links import RedNoticesLinks


class TestRedNoticesLinks(unittest.TestCase):
    """RedNoticesLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRedNoticesLinks(self):
        """Test RedNoticesLinks"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RedNoticesLinks()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
