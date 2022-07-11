from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class AccountInLine(admin.StackedInline):
    model = Account
    can_delete: False
    verbose_name_plural: 'Account'


class CustomizedUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'email', 'is_staff']
    inlines = (AccountInLine,)
    empty_value_display = '-empty-'


admin.site.register(Case)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Signs)
admin.site.register(Notification)
admin.site.register(History)
admin.site.register(Refraction)
admin.site.register(CoverTest)
admin.site.register(PupilReflex)
admin.site.register(PupilMeasurement)
admin.site.register(Appointment)
admin.site.register(News)
admin.site.register(Schedule)


@admin.register(Rx)
class RxAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'od_old_rx']
    empty_value_display = '-empty-'


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', ]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'user',
                    'first_name', 'middle_name', 'last_name']
