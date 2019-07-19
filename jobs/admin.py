from django.contrib import admin
from .models import Job, Objective
from comments.models import Comment, ObjectiveComment


# display foreignkey relationships
# using tabular inline display

class CommentInline(admin.TabularInline):
	model = Comment
	# set number of additional rows
	extra = 0


class ObjectiveInline(admin.TabularInline):
	model = Objective
	# set number of additional rows
	extra = 0


class ObjectiveCommentInline(admin.TabularInline):
	model = ObjectiveComment
	# set number of additional rows
	extra = 0



class JobAdmin(admin.ModelAdmin):
	inlines = [
		ObjectiveInline,
		CommentInline,
		
	]


class ObjectiveAdmin(admin.ModelAdmin):
	inlines = [
		ObjectiveCommentInline,
	]

admin.site.register(Job, JobAdmin)
admin.site.register(Objective, ObjectiveAdmin)


