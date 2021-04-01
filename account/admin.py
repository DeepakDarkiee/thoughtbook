from django.contrib import admin
from .models import RegisterUser


@admin.register(RegisterUser)
class RegisterUserAdmin(admin.ModelAdmin):
    class Meta:
        model = RegisterUser
        fields = '__all__'
