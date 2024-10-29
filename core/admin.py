from django.contrib import admin
from .models import (
    Department,
    Position,
    Employee,
    Attendance,
    PerformanceReview,
    Training,
    Compensation,
    Document,
    Message,
    OnboardingItem,
    OffboardingItem,
)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'department', 'created_at', 'updated_at')
    search_fields = ('name', 'department__name')
    list_filter = ('department', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

from django.utils.html import format_html

from django.contrib import admin
from django.utils.html import format_html
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = (
        'id',
        'name',
        'surname',
        'email',
        'department',
        'position',
        'status',
        'created_at',
        'updated_at',
        'display_profile_picture'
    )

    # Fields to search within the admin interface
    search_fields = (
        'name',
        'surname',
        'email',
        'department__name',
        'position__name'
    )

    # Fields to filter the admin list view
    list_filter = (
        'department',
        'position',
        'status',
        'created_at',
        'updated_at'
    )

    # Read-only fields for the admin interface
    readonly_fields = ('created_at', 'updated_at')

    def display_profile_picture(self, obj):
        """Display the profile picture from the related documents."""
        # Get the first document with a profile picture for the employee
        document = obj.documents.filter(profile_picture__isnull=False).first()
        if document and document.profile_picture:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px;"/>',
                document.profile_picture.url
            )
        return "No Image"

    display_profile_picture.short_description = 'Profile Picture'

# Register the Employee model with the EmployeeAdmin



class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    search_fields = ('employee__name', 'date')
    list_filter = ('status', 'date')

class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ('employee', 'review_date', 'rating')
    search_fields = ('employee__name', 'comments')
    list_filter = ('review_date', 'rating')

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('employee', 'training_name', 'date_completed')
    search_fields = ('employee__name', 'training_name')
    list_filter = ('date_completed',)

class CompensationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'amount', 'date')
    search_fields = ('employee__name', 'amount')
    list_filter = ('date',)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'file', 'upload_date')
    search_fields = ('employee__name',)
    list_filter = ('upload_date',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp')
    search_fields = ('sender__name', 'recipient__name', 'content')
    list_filter = ('timestamp',)

class OnboardingItemAdmin(admin.ModelAdmin):
    list_display = ('employee', 'item', 'completed')
    search_fields = ('employee__name', 'item')
    list_filter = ('completed',)

class OffboardingItemAdmin(admin.ModelAdmin):
    list_display = ('employee', 'item', 'completed')
    search_fields = ('employee__name', 'item')
    list_filter = ('completed',)

# Register models with their respective admin classes
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(PerformanceReview, PerformanceReviewAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Compensation, CompensationAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(OnboardingItem, OnboardingItemAdmin)
admin.site.register(OffboardingItem, OffboardingItemAdmin)
