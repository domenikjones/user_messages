from django.contrib import admin
from user_messages.models import Thread, UserThread


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('subject', )
    # list_filter = ()
    raw_id_fields = ('users', )
    
admin.site.register(Thread, ThreadAdmin)

class UserThreadAdmin(admin.ModelAdmin):
    list_display = ('thread', 'user', 'unread', 'deleted', )
    list_filter = ('unread', 'deleted', )
    raw_id_fields = ('user', )
    
admin.site.register(UserThread, UserThreadAdmin)