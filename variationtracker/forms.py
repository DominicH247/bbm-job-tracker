from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Variation, VariationPhase


class VariationCreateForm(forms.ModelForm):
    """form for creating variations"""
    planned_submission_date = forms.DateField(
        required=False, widget=AdminDateWidget(attrs={'placeholder': 'Planned Submission Date'}))
    date_variation_closed = forms.DateField(
        required=False, widget=AdminDateWidget(attrs={'placeholder': 'Variation Closing Date'}))

    class Meta:
        model = Variation
        fields = [
            'lra_reference',
            'product',
            'procedure_number',
            'variation_description',
            'owner',
            'personnel',
            'planned_submission_date',
            'date_variation_closed',
            'variation_status',
            'initiated_by',
            'variation_type',
            'variation_reason'
        ]

    def clean_lra_reference(self):
        """prevent duplicate entries of LRA ref"""
        lra_reference = self.cleaned_data['lra_reference']
        if Variation.objects.filter(lra_reference=lra_reference).exists():
            raise forms.ValidationError("This reference already exist.")
        return lra_reference
