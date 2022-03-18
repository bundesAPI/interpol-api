# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.interpol.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.interpol.model.red_notice_detail import RedNoticeDetail
from deutschland.interpol.model.red_notice_detail_arrest_warrants import (
    RedNoticeDetailArrestWarrants,
)
from deutschland.interpol.model.red_notice_detail_embedded import (
    RedNoticeDetailEmbedded,
)
from deutschland.interpol.model.red_notice_detail_images import RedNoticeDetailImages
from deutschland.interpol.model.red_notice_detail_images_embedded import (
    RedNoticeDetailImagesEmbedded,
)
from deutschland.interpol.model.red_notice_detail_images_embedded_images import (
    RedNoticeDetailImagesEmbeddedImages,
)
from deutschland.interpol.model.red_notice_detail_images_embedded_links import (
    RedNoticeDetailImagesEmbeddedLinks,
)
from deutschland.interpol.model.red_notice_detail_images_embedded_links_self import (
    RedNoticeDetailImagesEmbeddedLinksSelf,
)
from deutschland.interpol.model.red_notice_detail_images_links import (
    RedNoticeDetailImagesLinks,
)
from deutschland.interpol.model.red_notice_detail_images_links_notice import (
    RedNoticeDetailImagesLinksNotice,
)
from deutschland.interpol.model.red_notice_detail_images_links_self import (
    RedNoticeDetailImagesLinksSelf,
)
from deutschland.interpol.model.red_notice_detail_images_links_thumbnail import (
    RedNoticeDetailImagesLinksThumbnail,
)
from deutschland.interpol.model.red_notice_detail_links import RedNoticeDetailLinks
from deutschland.interpol.model.red_notices import RedNotices
from deutschland.interpol.model.red_notices_embedded import RedNoticesEmbedded
from deutschland.interpol.model.red_notices_links import RedNoticesLinks
from deutschland.interpol.model.red_notices_links_last import RedNoticesLinksLast
from deutschland.interpol.model.red_notices_links_next import RedNoticesLinksNext
from deutschland.interpol.model.red_notices_links_self import RedNoticesLinksSelf
from deutschland.interpol.model.red_notices_query import RedNoticesQuery
from deutschland.interpol.model.un_notice_detail import UNNoticeDetail
from deutschland.interpol.model.un_notice_detail_images import UNNoticeDetailImages
from deutschland.interpol.model.un_notice_detail_images_embedded import (
    UNNoticeDetailImagesEmbedded,
)
from deutschland.interpol.model.un_notice_detail_images_embedded_images import (
    UNNoticeDetailImagesEmbeddedImages,
)
from deutschland.interpol.model.un_notice_detail_images_embedded_links import (
    UNNoticeDetailImagesEmbeddedLinks,
)
from deutschland.interpol.model.un_notice_detail_images_embedded_links_self import (
    UNNoticeDetailImagesEmbeddedLinksSelf,
)
from deutschland.interpol.model.un_notice_detail_images_links import (
    UNNoticeDetailImagesLinks,
)
from deutschland.interpol.model.un_notice_detail_images_links_notice import (
    UNNoticeDetailImagesLinksNotice,
)
from deutschland.interpol.model.un_notice_detail_images_links_self import (
    UNNoticeDetailImagesLinksSelf,
)
from deutschland.interpol.model.un_notice_detail_images_links_thumbnail import (
    UNNoticeDetailImagesLinksThumbnail,
)
from deutschland.interpol.model.un_notice_detail_links import UNNoticeDetailLinks
from deutschland.interpol.model.un_notice_detail_links_images import (
    UNNoticeDetailLinksImages,
)
from deutschland.interpol.model.un_notice_detail_links_self import (
    UNNoticeDetailLinksSelf,
)
from deutschland.interpol.model.un_notices import UNNotices
from deutschland.interpol.model.un_notices_links import UNNoticesLinks
from deutschland.interpol.model.un_notices_links_last import UNNoticesLinksLast
from deutschland.interpol.model.un_notices_links_next import UNNoticesLinksNext
from deutschland.interpol.model.un_notices_links_self import UNNoticesLinksSelf
from deutschland.interpol.model.yellow_notice_detail import YellowNoticeDetail
from deutschland.interpol.model.yellow_notice_detail_images import (
    YellowNoticeDetailImages,
)
from deutschland.interpol.model.yellow_notice_detail_images_embedded import (
    YellowNoticeDetailImagesEmbedded,
)
from deutschland.interpol.model.yellow_notice_detail_images_embedded_images import (
    YellowNoticeDetailImagesEmbeddedImages,
)
from deutschland.interpol.model.yellow_notice_detail_images_embedded_links import (
    YellowNoticeDetailImagesEmbeddedLinks,
)
from deutschland.interpol.model.yellow_notice_detail_images_embedded_links_self import (
    YellowNoticeDetailImagesEmbeddedLinksSelf,
)
from deutschland.interpol.model.yellow_notice_detail_images_links import (
    YellowNoticeDetailImagesLinks,
)
from deutschland.interpol.model.yellow_notice_detail_images_links_notice import (
    YellowNoticeDetailImagesLinksNotice,
)
from deutschland.interpol.model.yellow_notice_detail_images_links_self import (
    YellowNoticeDetailImagesLinksSelf,
)
from deutschland.interpol.model.yellow_notice_detail_links import (
    YellowNoticeDetailLinks,
)
from deutschland.interpol.model.yellow_notice_detail_links_images import (
    YellowNoticeDetailLinksImages,
)
from deutschland.interpol.model.yellow_notice_detail_links_self import (
    YellowNoticeDetailLinksSelf,
)
from deutschland.interpol.model.yellow_notice_detail_links_thumbnail import (
    YellowNoticeDetailLinksThumbnail,
)
from deutschland.interpol.model.yellow_notices import YellowNotices
from deutschland.interpol.model.yellow_notices_links import YellowNoticesLinks
from deutschland.interpol.model.yellow_notices_links_last import YellowNoticesLinksLast
from deutschland.interpol.model.yellow_notices_links_next import YellowNoticesLinksNext
from deutschland.interpol.model.yellow_notices_links_self import YellowNoticesLinksSelf
