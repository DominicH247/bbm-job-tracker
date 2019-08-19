from django.contrib import admin
# Register your models here.

from .models import Variation, VariationPhase


# display foreignkey relationships
# using tabular inline display

class VariationPhaseInline(admin.TabularInline):
    model = VariationPhase
    # set number of additional rows
    extra = 0


class VariationAdmin(admin.ModelAdmin):
    inlines = [
        VariationPhaseInline
    ]


admin.site.register(Variation, VariationAdmin)
