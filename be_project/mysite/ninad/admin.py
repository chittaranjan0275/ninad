from django.contrib import admin
from .models import RagaDB

# class RagaDBAdmin(admin.ModelAdmin):
#     list_display = ('naam', 'thaat', 'vadi', 'samvadi', 'time', 'aaroh', 'aavaroh', 'info', 'link_slug')
#
# admin.site.register(RagaDB, RagaDBAdmin)


class RagaDBAdmin(admin.ModelAdmin):
    list_display = ('name', 'thaat', 'vadi', 'samvadi', 'time', 'aaroh', 'aavaroh', 'info', 'link_slug','name_hindi', 'thaat_hindi', 'vadi_hindi', 'samvadi_hindi', 'time_hindi', 'aaroh_hindi', 'aavaroh_hindi', 'info_hindi')

admin.site.register(RagaDB, RagaDBAdmin)