
from django.db import models


class Appointment(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING"
        CONFIRMED = "CONFIRMED"
        CANCELLED = "CANCELLED"

    reason = models.TextField()

    prescription = models.FileField(
        upload_to="prescriptions/", blank=True
    )

    duration_minutes = models.PositiveIntegerField(default=30)

    appointment_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=9,
        choices=Status.choices,
        default=Status.PENDING
    )

    doctor = models.ForeignKey(
        "AccountApp.Doctor",
        on_delete=models.CASCADE
    )

    patient = models.ForeignKey(
        "AccountApp.Patient",
        on_delete=models.CASCADE
    )
