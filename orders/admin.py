from django.contrib import admin
from .models import Order,OrderedItem

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_filter=("order_status","owner","created_at")
    list_display = ("id","owner","get_customer_address")
    search_fields = ("id","owner__name")
    def get_customer_address(self,obj):
        return obj.owner.address
    get_customer_address.short_description = "Address"

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderedItem)