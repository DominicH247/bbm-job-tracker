from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
	model = CustomUser
	list_display = ['username', 'email',  'Position' , 'is_staff']
	#  overwrite field sets of the UserAdmin class to add custom own fields
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
	    (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'Position')}),
	    (('Permissions'), {
	        'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
	    }),
	    (('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	# overwrite field sets of UserAdmin class for customised fields in add  admin form
	add_fieldsets = (
		(None, {
			'classes': ('wide',), 
			'fields': ('username', 'email', 'first_name', 'last_name','password1', 'password2'),
			}),
		)


admin.site.register(CustomUser, CustomUserAdmin)
