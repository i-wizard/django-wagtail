from wagtail  import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "title_and_textw"

# class RichTextBlock(blocks.RichTextBlock):
#     class Meta:
#         template = "streams/richtext_block.html"
#         icon = "edit"
#         label = "Full richtext"

class SimpleRichTextBlock(blocks.RichTextBlock):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link"
        ]
    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full richtext"

class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title help text")
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image",ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.CharBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False))
            ]
        )
    )
    class Meta:
        template = "streams/card_block.html"
        icon = "edit"
        label = "card block"

class CTABlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=50)
    text = blocks.CharBlock(required=True, max_length=200)
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=False, max_length=15, default="Call to Action")

    class Meta:
        template = "streams/cta.html"
        label = "Call to action"
        icon = "palceholder"