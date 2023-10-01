from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Subscribers


class SubscriberAdmin(ModelAdmin):
    model = Subscribers
    menu_label = "Email Subscribers"
    menu_icon = "palceholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_exploree = False
    list_display = ("email", "full_name")
    search_fields = ("email", "full_name")

modeladmin_register(SubscriberAdmin)
