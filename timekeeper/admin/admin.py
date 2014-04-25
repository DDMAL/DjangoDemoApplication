from django.contrib import admin

from timekeeper.models.activity import Activity
from timekeeper.models.person import Person
from timekeeper.models.place import Place


class ActivityAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


class PlaceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Place, PlaceAdmin)