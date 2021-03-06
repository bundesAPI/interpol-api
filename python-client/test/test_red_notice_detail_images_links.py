"""
    Interpol Notices API

    Interpol Red, Yellow and UN Notices API  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.interpol.model.red_notice_detail_images_links_notice import (
    RedNoticeDetailImagesLinksNotice,
)
from deutschland.interpol.model.red_notice_detail_images_links_self import (
    RedNoticeDetailImagesLinksSelf,
)
from deutschland.interpol.model.red_notice_detail_images_links_thumbnail import (
    RedNoticeDetailImagesLinksThumbnail,
)

from deutschland import interpol

globals()["RedNoticeDetailImagesLinksNotice"] = RedNoticeDetailImagesLinksNotice
globals()["RedNoticeDetailImagesLinksSelf"] = RedNoticeDetailImagesLinksSelf
globals()["RedNoticeDetailImagesLinksThumbnail"] = RedNoticeDetailImagesLinksThumbnail
from deutschland.interpol.model.red_notice_detail_images_links import (
    RedNoticeDetailImagesLinks,
)


class TestRedNoticeDetailImagesLinks(unittest.TestCase):
    """RedNoticeDetailImagesLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRedNoticeDetailImagesLinks(self):
        """Test RedNoticeDetailImagesLinks"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RedNoticeDetailImagesLinks()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
