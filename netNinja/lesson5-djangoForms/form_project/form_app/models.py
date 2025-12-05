from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# --------------------------
# USER PROFILE
# --------------------------
class Profile(models.Model):
    ROLE_CHOICES = [
        ('burner', 'Burner'),
        ('leader', 'Leader'),
        ('admin', 'Admin'),
    ]

    ACCOUNT_TYPES = [
        ('individual', 'Individual Burner'),
        ('cooperative', 'Cooperative'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='burner')
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, default='individual')

    phone = models.CharField(max_length=20, null=True, blank=True)

    # Burner home address
    province = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)
    cell = models.CharField(max_length=100, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)

    # Cooperative name (if account_type = cooperative)
    coop_name = models.CharField(max_length=255, null=True, blank=True)

    # Leader jurisdiction (work address)
    leader_district = models.CharField(max_length=100, blank=True, null=True)
    leader_sector = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} – {self.role}"


# --------------------------
# KILN
# --------------------------
class Kiln(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Work location (NOT home address)
    work_district = models.CharField(max_length=100)
    work_sector = models.CharField(max_length=100)
    work_cell = models.CharField(max_length=100)
    work_village = models.CharField(max_length=100)

    gps_coordinates = models.CharField(max_length=100, blank=True, null=True)
    location_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# --------------------------
# PERMISSION REQUEST
# --------------------------
class PermissionRequest(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('appointment_required', 'Appointment Required'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kiln = models.ForeignKey(Kiln, on_delete=models.CASCADE)

    message = models.TextField(blank=True, null=True)

    # Work location of the kiln
    kiln_district = models.CharField(max_length=100)
    kiln_sector = models.CharField(max_length=100)
    kiln_cell = models.CharField(max_length=100)
    kiln_village = models.CharField(max_length=100)

    # Uploaded documents
    id_document = models.FileField(upload_to="docs/id/", null=True, blank=True)
    land_certificate = models.FileField(upload_to="docs/land/", null=True, blank=True)
    coop_certificate = models.FileField(upload_to="docs/coop/", null=True, blank=True)
    tree_age_proof = models.FileField(upload_to="docs/tree/", null=True, blank=True)

    status = models.CharField(max_length=30, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request #{self.id} – {self.status}"


# --------------------------
# APPOINTMENTS
# --------------------------
class Appointment(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leader_appointments")
    burner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="burner_appointments")

    permission = models.ForeignKey(PermissionRequest, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    purpose = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS, default='pending')

    def __str__(self):
        return f"{self.date} – {self.burner.username}"

