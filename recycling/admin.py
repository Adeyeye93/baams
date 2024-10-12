from django.contrib import admin
from .models import TrashRequest, FundRequest  # import your models

# For TrashRequest
class TrashRequestAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = (
        'user', 
        'get_trash_types',  # Use custom method to display trash_types
        'pickup', 
        'DropOff', 
        'request_date', 
        'seen', 
        'finished', 
        'weight', 
        'earned', 
        'trash_type', 
        'location', 
        'Phone'
    )

    # Filter options in the admin panel
    list_filter = ('pickup', 'DropOff', 'seen', 'finished')

    # Fields to search in the search bar
    search_fields = ('user__username', 'trash_type', 'Phone', 'location')

    # Custom method to handle MultiSelectField display
    def get_trash_types(self, obj):
        return ", ".join(obj.trash_types)  # Converts list to a comma-separated string
    get_trash_types.short_description = 'Trash Types'  # Label for the column


# For FundRequest
class FundRequestAdmin(admin.ModelAdmin):
    list_display = (
        'user', 
        'withdraw_type', 
        'request_date', 
        'disbursed', 
        'amount', 
        'account_no', 
        'seen', 
        'finished'
    )

    # Filter options in the admin panel
    list_filter = ('withdraw_type', 'disbursed', 'seen', 'finished')

    # Fields to search in the search bar
    search_fields = ('user__username', 'withdraw_type', 'account_no')


# Register models with their respective admin classes
admin.site.register(TrashRequest, TrashRequestAdmin)
admin.site.register(FundRequest, FundRequestAdmin)
