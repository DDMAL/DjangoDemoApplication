from django.contrib import admin
from codekeeper.models.snippet import Snippet
from codekeeper.models.person import Person
from codekeeper.models.tag import Tag


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass