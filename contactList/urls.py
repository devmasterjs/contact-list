from django.contrib import admin
from django.urls import path

admin.site.index_title = 'Administration Panel'
admin.site.site_header = 'Contact List'
admin.site.site_title = 'Contact List'

urlpatterns = [
    path('admin/', admin.site.urls),
]
