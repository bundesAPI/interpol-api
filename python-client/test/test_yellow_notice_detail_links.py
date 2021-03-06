"""
    Interpol Notices API

    Interpol Red, Yellow and UN Notices API  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.interpol.model.yellow_notice_detail_links_images import (
    YellowNoticeDetailLinksImages,
)
from deutschland.interpol.model.yellow_notice_detail_links_self import (
    YellowNoticeDetailLinksSelf,
)
from deutschland.interpol.model.yellow_notice_detail_links_thumbnail import (
    YellowNoticeDetailLinksThumbnail,
)

from deutschland import interpol

globals()["YellowNoticeDetailLinksImages"] = YellowNoticeDetailLinksImages
globals()["YellowNoticeDetailLinksSelf"] = YellowNoticeDetailLinksSelf
globals()["YellowNoticeDetailLinksThumbnail"] = YellowNoticeDetailLinksThumbnail
from deutschland.interpol.model.yellow_notice_detail_links import (
    YellowNoticeDetailLinks,
)


class TestYellowNoticeDetailLinks(unittest.TestCase):
    """YellowNoticeDetailLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testYellowNoticeDetailLinks(self):
        """Test YellowNoticeDetailLinks"""
        # FIXME: construct object with mandatory attributes with example values
        # model = YellowNoticeDetailLinks()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
