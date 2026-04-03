from django.contrib import admin
from plays.models import Play, Actor, Show

class ShowAdminInline(admin.StackedInline):
    model = Show
    extra = 0

class PlayAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [ShowAdminInline]

class ShowAdmin(admin.ModelAdmin):
    list_display = ("play_name", "starts_at",)

# Register your models here.
admin.site.register(Play, PlayAdmin)
admin.site.register(Actor, admin.ModelAdmin)
admin.site.register(Show, ShowAdmin)
