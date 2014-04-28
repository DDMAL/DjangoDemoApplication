from django.contrib import admin

from timekeeper.models.activity import Activity
from timekeeper.models.person import Person
from timekeeper.models.place import Place


def reindex_in_solr(modeladmin, request, queryset):
    # calls the save method on every item, ensuring the
    # post_save handler is called
    for item in queryset:
        item.save()
reindex_in_solr.short_description = "Re-Index Selected Items"


class ActivityAdmin(admin.ModelAdmin):
    actions = [reindex_in_solr]


class PersonAdmin(admin.ModelAdmin):
    actions = [reindex_in_solr]


class PlaceAdmin(admin.ModelAdmin):
    actions = [reindex_in_solr]


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Place, PlaceAdmin)
