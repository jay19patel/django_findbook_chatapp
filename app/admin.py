from django.contrib import admin

# Register your models here.
from.models import Room,Topic,Message,Profilemodel,Post

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Profilemodel)
admin.site.register(Post)