from django.contrib import admin
from .models import MyUser,Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','zhuozhe','created_date')
	search_fields = ('zhuozhe','title')
	list_filter = ('created_date',)
	date_hierarchy = 'created_date'
	ordering = ('-created_date',)
	fields = ('title','zhuozhe','created_date')
	
	

admin.site.register(Article,ArticleAdmin)
admin.site.register(MyUser)
# Register your models here.
