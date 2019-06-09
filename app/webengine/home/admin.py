from django.contrib import admin
from .models import FeedBack

# Register your models here.


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'date')
    list_filter = ('customer_name', 'date')
    search_fields = ('customer_name__name', 'message')
    
    class Meta:
        model = FeedBack


admin.site.register(FeedBack, FeedbackAdmin)
