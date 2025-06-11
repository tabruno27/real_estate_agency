from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    extra = 4
    raw_id_fields = ['owner']
    verbose_name = 'Собственник'
    verbose_name_plural = 'Собственники'

    def owner(self, obj):
        return obj.owner.full_name

    owner.short_description = 'Имя владельца'

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'town_district', 'address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony', 'floor',)
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline]
    exclude = ['owners']

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text')
    raw_id_fields = ('user', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'owner_pure_phone')
    raw_id_fields = ('flat_owner',)


admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Owner, OwnerAdmin)
