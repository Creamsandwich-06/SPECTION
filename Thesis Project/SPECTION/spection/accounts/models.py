from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    occupation = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(
        default="pexels-misael-garcia-1707828.jpg", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)

    street = models.CharField(max_length=200, null=True, blank=True)
    barangay = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    zip = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username


class Schedule(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    badge = models.CharField(max_length=200, null=True, blank=True)
    date = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    everyYear = models.BooleanField(
        default=False, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    color = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Appointment(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    purpose = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    status = models.CharField(
        max_length=200, null=True, blank=True, default='Not Approved')


class News(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    desc = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(
        default="pexels-misael-garcia-1707828.jpg", null=True, blank=True)
    headline = models.BooleanField(
        default=False, max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Contact(models.Model):
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.CharField(max_length=500, null=True, blank=True)

class Patient(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    pd = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username


class Notification(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, null=True)


class Case(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class History(models.Model):
    user = models.OneToOneField(
        Case, null=True, blank=True, on_delete=models.CASCADE)
    statement = models.CharField(max_length=200, null=True, blank=True)
    dm = models.BooleanField(
        default=False, null=True, blank=True)
    hpn = models.BooleanField(
        default=False, null=True, blank=True)
    allergies = models.BooleanField(
        default=False, null=True, blank=True)
    medical_history = models.CharField(
        max_length=200, null=True, blank=True)
    treatments = models.CharField(max_length=200, null=True, blank=True)
    ocular_history = models.CharField(
        max_length=200, null=True, blank=True)
    physical_condition = models.CharField(
        max_length=200, null=True, blank=True)
    dominant_hand = models.CharField(
        max_length=200, null=True, blank=True, default='Left')
    dominant_eye = models.CharField(max_length=200, null=True, blank=True)
    ipd = models.CharField(max_length=200, null=True, blank=True)
    bp = models.CharField(max_length=200, null=True, blank=True)
    od = models.CharField(max_length=200, null=True, blank=True)
    os = models.CharField(max_length=200, null=True, blank=True)
    anatomical = models.BooleanField(
        default=False, null=True, blank=True)
    catopric = models.BooleanField(
        default=False, null=True, blank=True)
    tentative_diag = models.CharField(
        max_length=200, null=True, blank=True)


class Signs(models.Model):
    user = models.OneToOneField(
        Case, null=True, blank=True, on_delete=models.CASCADE)
    signs_details = models.CharField(default='After Reading:',max_length=200, null=True, blank=True)
    activity_details = models.CharField(default='Reading:',max_length=200, null=True, blank=True)


class Refraction(models.Model):
    user = models.OneToOneField(
        Case, null=True, blank=True, on_delete=models.CASCADE)
    od_auto_refraction = models.CharField(
        max_length=200, null=True, blank=True)
    os_auto_refraction = models.CharField(
        max_length=200, null=True, blank=True)
    os_retinoscopy = models.CharField(max_length=200, null=True, blank=True)
    od_retinoscopy = models.CharField(max_length=200, null=True, blank=True)
    od_cycoplastic = models.CharField(max_length=200, null=True, blank=True)
    os_cycoplastic = models.CharField(max_length=200, null=True, blank=True)
    od_subjective = models.CharField(max_length=200, null=True, blank=True)
    os_subjective = models.CharField(max_length=200, null=True, blank=True)


class CoverTest(models.Model):
    user = models.OneToOneField(
        Case, null=True, blank=True, on_delete=models.CASCADE)
    od_far_unilateral = models.CharField(max_length=200, null=True, blank=True)
    os_far_unilateral = models.CharField(max_length=200, null=True, blank=True)
    od_far_alternating = models.CharField(
        max_length=200, null=True, blank=True)
    os_far_alternating = models.CharField(
        max_length=200, null=True, blank=True)
    od_near_unilateral = models.CharField(
        max_length=200, null=True, blank=True)
    os_near_unilateral = models.CharField(
        max_length=200, null=True, blank=True)
    od_near_alternating = models.CharField(
        max_length=200, null=True, blank=True)
    os_near_alternating = models.CharField(
        max_length=200, null=True, blank=True)


class PupilReflex(models.Model):
    user = models.OneToOneField(
        Case, null=True, blank=True, on_delete=models.CASCADE)
    od_direct = models.CharField(max_length=200, null=True, blank=True)
    od_consensual = models.CharField(max_length=200, null=True, blank=True)
    od_swing = models.CharField(max_length=200, null=True, blank=True)
    os_direct = models.CharField(max_length=200, null=True, blank=True)
    os_consensual = models.CharField(max_length=200, null=True, blank=True)
    os_swing = models.CharField(max_length=200, null=True, blank=True)


class PupilMeasurement(models.Model):
    user = models.OneToOneField(
        Case, null=True, blank=True, on_delete=models.CASCADE)
    od_horizontal = models.CharField(max_length=200, null=True, blank=True)
    od_vertical = models.CharField(max_length=200, null=True, blank=True)
    os_horizontal = models.CharField(max_length=200, null=True, blank=True)
    os_vertical = models.CharField(max_length=200, null=True, blank=True)
    maddox_rod = models.CharField(max_length=200, null=True, blank=True)
    maddox_wing = models.CharField(max_length=200, null=True, blank=True)
    vergence = models.CharField(max_length=200, null=True, blank=True)


class Rx(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    od_old_rx = models.CharField(max_length=200, null=True, blank=True)
    od_dist_vasc = models.CharField(max_length=200, null=True, blank=True)
    od_dist_vacc = models.CharField(max_length=200, null=True, blank=True)
    od_near_vasc = models.CharField(max_length=200, null=True, blank=True)
    od_near_vacc = models.CharField(max_length=200, null=True, blank=True)
    od_phv = models.CharField(max_length=200, null=True, blank=True)
    os_old_rx = models.CharField(max_length=200, null=True, blank=True)
    os_dist_vasc = models.CharField(max_length=200, null=True, blank=True)
    os_dist_vacc = models.CharField(max_length=200, null=True, blank=True)
    os_near_vasc = models.CharField(max_length=200, null=True, blank=True)
    os_near_vacc = models.CharField(max_length=200, null=True, blank=True)
    os_phv = models.CharField(max_length=200, null=True, blank=True)
    ou_old_rx = models.CharField(max_length=200, null=True, blank=True)
    ou_dist_vasc = models.CharField(max_length=200, null=True, blank=True)
    ou_dist_vacc = models.CharField(max_length=200, null=True, blank=True)
    ou_near_vasc = models.CharField(max_length=200, null=True, blank=True)
    ou_near_vacc = models.CharField(max_length=200, null=True, blank=True)
    ou_phv = models.CharField(max_length=200, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    TYPE = (
        ('Glasses', 'Glasses'),
        ('Product', 'Product'),
    )

    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    price = models.FloatField(null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    due = models.FloatField(null=True,blank=True)
    type = models.CharField(max_length=200, null=True,blank=True, choices=TYPE)
    date_created = models.DateTimeField(auto_now_add=True)
    product_details = models.CharField(default='None:',max_length=200, null=True, blank=True)
    dispense_details = models.CharField(default='None:',max_length=200, null=True, blank=True)
    lab_details = models.CharField(default='None:',max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True,blank=True)
    note = models.CharField(max_length=200, null=True,blank=True)

class Billing(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True,on_delete=models.CASCADE)
    amount = models.FloatField(null=True,blank=True)
    remain_due = models.FloatField(null=True,blank=True)
    description = models.CharField(max_length=200, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)