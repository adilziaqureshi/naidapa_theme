import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

BRAND_LOGO = "/assets/naidapa_theme/images/NE.svg"


def set_branding():
    website_settings = frappe.get_single("Website Settings")
    website_settings.app_logo = BRAND_LOGO
    website_settings.splash_image = BRAND_LOGO
    website_settings.favicon = BRAND_LOGO
    website_settings.save(ignore_permissions=True)

    navbar_settings = frappe.get_single("Navbar Settings")
    navbar_settings.app_logo = BRAND_LOGO
    navbar_settings.save(ignore_permissions=True)

    frappe.clear_cache()


def after_install():
    create_custom_fields({
        "Workspace": [
            {
                "fieldname": "custom_animated_icon",
                "label": "Animated Icon",
                "fieldtype": "Data",
                "insert_after": "icon",
                "description": "Iconify icon code (e.g. mdi:home)"
            }
        ]
    })
    set_branding()
    
def after_migrate():
    after_install()
