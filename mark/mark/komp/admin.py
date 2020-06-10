from django.contrib import admin
from .models import Buy, Author
# Register your models here.

class BuyModelAdmin(admin.ModelAdmin):
  list_display = ['title','timestamp']
  list_display_links = ['title', 'timestamp']
  list_filter = ['timestamp']
  search_fields = ['title', 'content']
  extra = 2
  ordering = ['timestamp']
  class Meta:
    model = Buy

class AuthorModelAdmin(admin.ModelAdmin):
  list_display = ['first_name','second_name','email']
  list_display_links = ['first_name','second_name','email']
  search_fields = ['first_name','second_name']
  class Meta:
    model = Author


admin.site.register(Buy,BuyModelAdmin)
admin.site.register(Author,AuthorModelAdmin)
