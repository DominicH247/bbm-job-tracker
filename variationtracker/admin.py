from django.contrib import admin
# Register your models here.

from .models import Variation, PreSubmissionPhase, SubmissionPhase, DecisionPhase, PostDecisionPhase, InternalApprovalPhase, NationalPhase


# display foreignkey relationships
# using tabular inline display

class PreSubmissionPhaseInline(admin.TabularInline):
    model = PreSubmissionPhase
    # set number of additional rows
    extra = 0


class SubmissionPhaseInline(admin.TabularInline):
    model = SubmissionPhase
    # set number of additional rows
    extra = 0


class DecisionPhaseInline(admin.TabularInline):
    model = DecisionPhase
    # set number of additional rows
    extra = 0


class PostDecisionPhaseInline(admin.TabularInline):
    model = PostDecisionPhase
    # set number of additional rows
    extra = 0


class InternalApprovalPhaseInline(admin.TabularInline):
    model = InternalApprovalPhase
    # set number of additional rows
    extra = 0


class NationalPhaseInline(admin.TabularInline):
    model = NationalPhase
    # set number of additional rows
    extra = 0


class VariationAdmin(admin.ModelAdmin):
    inlines = [
        PreSubmissionPhaseInline,
        SubmissionPhaseInline,
        DecisionPhaseInline,
        PostDecisionPhaseInline,
        InternalApprovalPhaseInline,
        NationalPhaseInline

    ]


admin.site.register(Variation, VariationAdmin)
