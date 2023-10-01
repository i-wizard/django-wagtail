from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from wagtail.models import Page

from streams.blocks import TitleAndTextBlock, SimpleRichTextBlock, CardBlock, CTABlock


class FlexPage(Page):
    template = "flex/flex_page.html"
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    content = StreamField(
        [
            ("tite_and_text", TitleAndTextBlock()),
            ("rich_text", SimpleRichTextBlock()),
            ("card_block", CardBlock()),
            ("cta_block", CTABlock())
        ],
        null=True,
        blank=True,
        use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("content")
    ]
