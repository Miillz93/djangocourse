import time
from django.contrib import admin
from musicapp.models import Album, Song

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
	readonly_fields = ('release_date',)
	search_fields = ['name', 'artist_name',]
	list_display = ('name', 'artist_name',)
	list_editable = ('artist_name',)
	list_filter = ('artist_name',)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
	save_on_top = True
	exclude = ('lyrics',)
	autocomplete_fields = ['album']
	list_display = ('name',
					'album',
					'duration_human_readable',)
	list_filter = ('album__name','album__artist_name',)
	search_fields = ['name', 'album__name', 'album__artist_name']
	autocomplete_fields = ['album']
	
	def duration_human_readable(self, obj):
		return  time.strftime('%M:%S', time.gmtime(obj.duration))
	duration_human_readable.short_description = "Duration"
	duration_human_readable.admin_order_field = "duration"
	


admin.site.register(Album, AlbumAdmin)
