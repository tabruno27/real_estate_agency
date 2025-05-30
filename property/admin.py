from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address', 'owner')
    readonly_fields = ["created_at"]
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town', 'likes_count')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'town', 'construction_year')
    raw_id_fields = ('likes',)


    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = 'Количество лайков'

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
