from django.contrib import admin
from practice_tracking.models import *

class UserProfAdmin(admin.ModelAdmin):
	list_display = ('user', 'bboyname', 'crew',)

class ParentMoveAdmin(admin.ModelAdmin):
	list_display = ('name', 'move_classification',)
	list_filter = ('name', 'move_classification',)
	ordering = ('move_classification',)

class MoveClassAdmin(admin.ModelAdmin):
	list_display = ('name',)

class MoveAdmin(admin.ModelAdmin):
	list_display = ('name', 'value', 'move_classification',)

admin.site.register(UserProfile, UserProfAdmin)
admin.site.register(ParentMove, ParentMoveAdmin)
admin.site.register(MoveClass, MoveClassAdmin)
admin.site.register(Move, MoveAdmin)

