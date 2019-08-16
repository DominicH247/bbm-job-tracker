from django.db import models
from products.models import PharmaProduct
from user.models import CustomUser


class Variation(models.Model):
    """Variation model"""
    # automatically assign reference
    lra_reference = models.CharField(max_length=100)
    product = models.ManyToManyField(PharmaProduct)
    procedure_number = models.CharField(
        max_length=50, blank=True, default='Awaiting')
    variation_description = models.TextField()
    date_recieived = models.DateField(auto_now_add=True)  # can be edited
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        related_name='owners'
    )
    personnel = models.ManyToManyField(CustomUser, blank=True)
    date_pre_submission = models.DateField(null=True, blank=True)
    date_submission = models.DateField(null=True, blank=True)
    date_approval = models.DateField(null=True, blank=True)
    date_internal_approval_completion = models.DateField(null=True, blank=True)
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
        default=''
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
        default=''
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


class PreSubmissionPhase(models.Model):
    """Pre submission phase"""
    variation = models.ForeignKey(
        Variation,
        on_delete=models.CASCADE,
        null=True,
        related_name='presubmissions'
    )
    actions = models.TextField()
    date_completed = models.DateField(null=True, blank=True)


class SubmissionPhase(models.Model):
    """Pre submission phase"""
    variation = models.ForeignKey(
        Variation,
        on_delete=models.CASCADE,
        null=True,
        related_name='submissions'
    )
    # CESP submission, direct submission
    CESP = 'CESP'
    DIRECT = 'Direct'

    SUBMISSION_TYPE_CHOICES = (
        (CESP, 'CESP'),
        (DIRECT, 'Direct'),

    )
    submission_type = models.CharField(
        choices=SUBMISSION_TYPE_CHOICES,
        max_length=10,
        default='CESP'
    )
    details = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_submitted = models.DateField(null=True, blank=True)


class DecisionPhase(models.Model):
    variation = models.ForeignKey(
        Variation,
        on_delete=models.CASCADE,
        null=True,
        related_name='decisions'
    )
    AWAITING = 'Awaiting'
    APPROVED = 'Approved'
    RFI_PVAR = 'RFI/PVAR'
    REJECTED = 'Rejected'
    DECISION_CHOICES = (
        (AWAITING, 'Awaiting'),
        (APPROVED, 'Approved'),
        (RFI_PVAR, 'RFI/PVAR'),
        (REJECTED, 'Rejected'),
    )
    decision = models.CharField(
        choices=DECISION_CHOICES,
        max_length=10,
        default='AWAITING'
    )
    addional_details = models.TextField()
    decision_date = models.DateField()


class PostDecisionPhase(models.Model):
    variation = models.ForeignKey(
        Variation,
        on_delete=models.CASCADE,
        null=True,
        related_name='postdecisions'
    )
    details = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_completed = models.DateField(null=True, blank=True)


class InternalApprovalPhase(models.Model):
    """internal approval class"""
    variation = models.ForeignKey(
        Variation,
        on_delete=models.CASCADE,
        null=True,
        related_name='approvals'
    )
    details = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_completed = models.DateField(null=True, blank=True)


class NationalPhase(models.Model):
    """national phase class"""
    variation = models.ForeignKey(
        Variation,
        on_delete=models.CASCADE,
        null=True,
        related_name='nationalphases'
    )
    #  national phase requirement choices
    YES = 'Yes'
    NO = 'N/A'
    NATIONALPHASE_REQUIERMENT_CHOICES = (
        (YES, 'Yes'),
        (NO, 'N/A'),
    )
    details = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_completed = models.DateField(null=True, blank=True)
