from re import M
from time import time
from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


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
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

class CaseHistory(models.Model):
    PLANE = (
        ('Right', 'Right'),
        ('Left', 'Left'),
    )
    name = models.CharField(max_length=200, null=True)
    statement = models.CharField(max_length=200, null=True)
    medicalHistory = models.CharField(max_length=200, null=True)
    allergies = models.CharField(max_length=200, null=True)
    treatments = models.CharField(max_length=200, null=True)        
    ocularHistory = models.CharField(max_length=200, null=True)
    physicalCondition = models.CharField(max_length=200, null=True)
    dominantHand = models.CharField(max_length=200, null=True, choices=PLANE)
    dominantEye = models.CharField(max_length=200, null=True, choices=PLANE)
    dm = models.FloatField(null=True)
    hpm = models.FloatField(null=True)
    ipd = models.CharField(max_length=200, null=True)
    anatomical = models.CharField(max_length=200, null=True)
    catastrophic = models.CharField(max_length=200, null=True)
    bp = models.FloatField(null=True)
    od = models.CharField(max_length=200, null=True, choices=PLANE)
    os = models.FloatField(null=True)
    tentativeDiagnosis = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    purpose = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)

class Case(models.Model):
    name = refer_to = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

class SignsAndSymptoms(models.Model):
    CHOICE = (
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
    )
    has_prescription = models.CharField(max_length=200, null=True, choices=CHOICE)
    granulation = models.CharField(max_length=200, null=True)
    amblyopia = models.CharField(max_length=200, null=True)
    epiphoria = models.CharField(max_length=200, null=True)
    photophobia = models.CharField(max_length=200, null=True)
    hordeolum = models.CharField(max_length=200, null=True)
    redenss = models.CharField(max_length=200, null=True, choices=CHOICE)
    muscae_volitantess = models.CharField(max_length=200, null=True)
    ptosis = models.CharField(max_length=200, null=True)
    diziness = models.CharField(max_length=200, null=True, choices=CHOICE)
    fatigue = models.CharField(max_length=200, null=True)
    nervousness = models.CharField(max_length=200, null=True)
    blur_far = models.CharField(max_length=200, null=True, choices=CHOICE)
    blur_near = models.CharField(max_length=200, null=True, choices=CHOICE)
    diplopia_far = models.CharField(max_length=200, null=True, choices=CHOICE)
    diplopia_near = models.CharField(max_length=200, null=True, choices=CHOICE)
    smarting = models.CharField(max_length=200, null=True)
    shooting = models.CharField(max_length=200, null=True)
    throbbing = models.CharField(max_length=200, null=True)
    eye_burn = models.CharField(max_length=200, null=True, choices=CHOICE)
    eye_ache = models.CharField(max_length=200, null=True, choices=CHOICE)
    eye_tired = models.CharField(max_length=200, null=True, choices=CHOICE)
    frontal = models.CharField(max_length=200, null=True)
    temporal = models.CharField(max_length=200, null=True)
    occipital = models.CharField(max_length=200, null=True)
    intraocular = models.CharField(max_length=200, null=True)
    parietal = models.CharField(max_length=200, null=True)
    intermittent = models.CharField(max_length=200, null=True)
    recurrent = models.CharField(max_length=200, null=True)
    constant = models.CharField(max_length=200, null=True)
    after_reading = models.CharField(max_length=200, null=True)

class oldRx(models.model):
    od_dist_vasc = models.CharField(max_length=200, null=True)
    od_dist_vacc = models.CharField(max_length=200, null=True)
    od_near_vasc = models.CharField(max_length=200, null=True)
    od_near_vacc = models.CharField(max_length=200, null=True)
    od_phv = models.CharField(max_length=200, null=True)
    os_dist_vasc = models.CharField(max_length=200, null=True)
    os_dist_vacc = models.CharField(max_length=200, null=True)
    os_near_vasc = models.CharField(max_length=200, null=True)
    os_near_vacc = models.CharField(max_length=200, null=True)
    os_phv = models.CharField(max_length=200, null=True)
    ou_dist_vasc = models.CharField(max_length=200, null=True)
    ou_dist_vacc = models.CharField(max_length=200, null=True)
    ou_phv = models.CharField(max_length=200, null=True)

class PupilMeasurement(models.model):
    od_horizontal = models.CharField(max_length=200, null=True)
    od_vertical = models.CharField(max_length=200, null=True)
    os_horizontal = models.CharField(max_length=200, null=True)
    os_vertical = models.CharField(max_length=200, null=True)
    maddox_rod = models.CharField(max_length=200, null=True)
    maddox_wing = models.CharField(max_length=200, null=True)
    vergence = models.CharField(max_length=200, null=True)
    others = models.CharField(max_length=200, null=True)

class Refraction(models.model):
    od_auto_refraction = models.CharField(max_length=200, null=True)
    od_retinoscopy = models.CharField(max_length=200, null=True)
    od_cycoplastic = models.CharField(max_length=200, null=True)
    od_subjective = models.CharField(max_length=200, null=True)
    cs_auto_refraction = models.CharField(max_length=200, null=True)
    cs_retinoscopy = models.CharField(max_length=200, null=True)
    cs_cycoplastic = models.CharField(max_length=200, null=True)
    cs_subjective = models.CharField(max_length=200, null=True)

class PupilReflex(models.Model):
    od_direct = models.CharField(max_length=200, null=True)
    od_consensual = models.CharField(max_length=200, null=True)
    od_swing = models.CharField(max_length=200, null=True)
    os_direct = models.CharField(max_length=200, null=True)
    os_consensual = models.CharField(max_length=200, null=True)
    os_swing = models.CharField(max_length=200, null=True)

class CoverTest(models.Model):
    od_far_unilateral = models.CharField(max_length=200, null=True)
    od_far_alternating = models.CharField(max_length=200, null=True)
    os_far_unilateral = models.CharField(max_length=200, null=True)
    os_far_alternating = models.CharField(max_length=200, null=True)
    od_near_unilateral = models.CharField(max_length=200, null=True)
    od_near_alternating = models.CharField(max_length=200, null=True)
    os_near_unilateral = models.CharField(max_length=200, null=True)
    os_near_alternating = models.CharField(max_length=200, null=True)

class Prescription(models.Model):
        description = models.CharField(max_length=200, null=True)

class PatientReferall(models.Model):
    refer_to = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    
class PatientReferall(models.Model):
    status = models.CharField(max_length=200, null=True)
    manufacturer = models.CharField(max_length=200, null=True)
    style = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    a = models.CharField(max_length=200, null=True)
    dbl = models.CharField(max_length=200, null=True)
    ed =models.CharField(max_length=200, null=True)
    lens_index  = models.CharField(max_length=200, null=True)
    od_spehere = models.CharField(max_length=200, null=True)
    od_cy = models.CharField(max_length=200, null=True)
    od_axis = models.CharField(max_length=200, null=True)
    od_height = models.CharField(max_length=200, null=True)
    od_base_prism = models.CharField(max_length=200, null=True)
    os_sphere = models.CharField(max_length=200, null=True)
    os_cy = models.CharField(max_length=200, null=True)
    os_axis = models.CharField(max_length=200, null=True)
    os_height = models.CharField(max_length=200, null=True)
    os_base_prism = models.CharField(max_length=200, null=True)
    sv = models.CharField(max_length=200, null=True)
    bifocal_style = models.CharField(max_length=200, null=True)
    progressive = models.CharField(max_length=200, null=True)
    tint = models.CharField(max_length=200, null=True)
    n_distance = models.CharField(max_length=200, null=True)
    d_distance = models.CharField(max_length=200, null=True)
    n_near = models.CharField(max_length=200, null=True)
    d_near =  models.CharField(max_length=200, null=True)
    uv_400 = models.CharField(max_length=200, null=True)
    anti_scratch = models.CharField(max_length=200, null=True)
    anti_reflective =  models.CharField(max_length=200, null=True)
    blue_block = models.CharField(max_length=200, null=True)
    s_instruction = models.CharField(max_length=200, null=True)

class VisualTask(models.Model):
    task_name = models.CharField(max_length=200, null=True)
    hobbies_name  = models.CharField(max_length=200, null=True)
    sport_name = models.CharField(max_length=200, null=True)
    others = models.CharField(max_length=200, null=True)

class Notification(models.Model):
    title = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    date =  models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, null=True)

class Schedule(models.Model):
    title =  models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True)

class Invoice(models.Model):
    product_name  = refer_to = models.CharField(max_length=200, null=True)
    product_type = refer_to = models.CharField(max_length=200, null=True)
    time = refer_to = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.CharField(max_length=200, null=True)
    amount = models.CharField(max_length=200, null=True)

class Dues(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, null=True)
    amount = models.CharField(max_length=200, null=True)
