from django.db import models
from django.urls import reverse
from products.models import PharmaProduct
from user.models import CustomUser


class Variation(models.Model):
    """Variation model"""
    # automatically assign reference
    lra_reference = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    product = models.ManyToManyField(PharmaProduct)
    procedure_number = models.CharField(
        max_length=50, blank=True, default='Awaiting')
    variation_description = models.TextField()
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        related_name='owners'
    )
    personnel = models.ManyToManyField(CustomUser, blank=True)
    planned_submission_date = models.DateField(null=True, blank=True)
    date_variation_closed = models.DateField(null=True, blank=True)
    # Variation status choices
    OPEN = 'Open'
    CLOSED = 'Closed'
    VARIATION_STATUS_CHOICES = (
        (OPEN, 'Open'),
        (CLOSED, 'Closed')
    )
    variation_status = models.CharField(
        choices=VARIATION_STATUS_CHOICES,
        max_length=15,
        null=True,
        blank=True,
        default='Open'
    )
    # Raised by choices
    LRA = 'LRA'
    GRA = 'GRA'
    MHRA = 'MHRA'
    OTHER = 'Other'
    RAISED_BY_CHOICES = (
        (LRA, 'LRA'),
        (GRA, 'GRA'),
        (MHRA, 'MHRA'),
        (OTHER, 'Other')
    )
    initiated_by = models.CharField(
        choices=RAISED_BY_CHOICES,
        max_length=10,
        null=True,
        blank=True,
        default='GRA'
    )

    # Variation Type
    IAN = 'IAN'
    IA = 'IA'
    IIB = 'IB'
    II = 'II'
    VARIATION_TYPE_CHOICES = (
        (IAN, 'IAN'),
        (IA, 'IA'),
        (IIB, 'IB'),
        (II, 'II')
    )
    variation_type = models.CharField(
        choices=VARIATION_TYPE_CHOICES,
        max_length=10,
        null=True,
        blank=True,
        default=''
    )
    # Variation Reason
    QUALITY = 'Quality'
    PI = 'Patient Information'
    VARIATION_REASON_CHOICES = (
        (QUALITY, 'Quality'),
        (PI, 'Patient Information')
    )
    variation_reason = models.CharField(
        choices=VARIATION_REASON_CHOICES,
        max_length=20,
        null=True,
        blank=True,
        default=''
    )

    # def autoset_close_date(self):
    #     """set closing date automatically when status set to CLOSED """
    #     if VARIATION_STATUS_CHOICES == CLOSED:
    #         date_variation_closed = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.lra_reference

    def get_absolute_url(self):
        """absolute URL of Variation model"""
        return reverse('variation_detail', kwargs={'pk': self.pk})


class VariationPhase(models.Model):
    """Variation log"""
    variation = models.ForeignKey(
        Variation,
        on_delete=models.CASCADE,
        null=True,
        related_name='logs'
    )
    #  variation log choices
    PRE_SUBMISSION_PHASE = 'Pre-submission Phase'
    SUBMISSION_PHASE = 'Submission Phase'
    POST_SUBMISSION_PHASE = 'Post Submission Phase'
    INTERNAL_APPROVAL_PHASE = 'Internal Approval Phase'
    NATIONAL_PHASE = 'National Phase'
    DECISION_CHOICES = (
        (PRE_SUBMISSION_PHASE, 'Pre-Submission Phase'),
        (SUBMISSION_PHASE, 'Submission Phase'),
        (POST_SUBMISSION_PHASE, 'Post Submission Phase'),
        (INTERNAL_APPROVAL_PHASE, 'Internal Approval Phase'),
        (NATIONAL_PHASE, 'National Phase'),
    )
    phase = models.CharField(
        choices=DECISION_CHOICES,
        max_length=30,
        default='PresubmissionPhase'
    )
    details = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.phase
