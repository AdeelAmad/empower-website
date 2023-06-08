from django.contrib import admin

from empower.models import homePage, contactPage, event, image

# Register your models here.
admin.site.register(homePage)
admin.site.register(contactPage)
admin.site.register(event)
admin.site.register(image)