from django.contrib import admin
from user_messages.models import Thread, UserThread, Message


class UserThreadAdmin(admin.ModelAdmin):
    list_display = ('thread', 'user', 'unread', 'deleted', )
    list_filter = ('unread', 'deleted', )
    raw_id_fields = ('user', )

admin.site.register(UserThread, UserThreadAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('thread', 'sender', 'sent_at', )
    list_filter = ('sent_at', 'thread', )
    raw_id_fields = ('sender', )

admin.site.register(Message, MessageAdmin)