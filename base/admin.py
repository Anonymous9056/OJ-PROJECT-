<<<<<<< HEAD
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Problem, Submission, Contest, ContestParticipation, UserProblem

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'rating', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'rating')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    
    fieldsets = UserAdmin.fieldsets + (
        ('Online Judge Info', {'fields': ('bio', 'profile_picture', 'date_of_birth', 'rating')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Online Judge Info', {'fields': ('bio', 'profile_picture', 'date_of_birth', 'rating')}),
    )

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'created_by', 'is_active', 'created_at')
    list_filter = ('difficulty', 'is_active', 'created_at')
    search_fields = ('title', 'description', 'created_by__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'problem', 'language', 'status', 'execution_time', 'submitted_at')
    list_filter = ('status', 'language', 'submitted_at')
    search_fields = ('user__username', 'problem__title')
    ordering = ('-submitted_at',)
    readonly_fields = ('submitted_at', 'judged_at')

@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'is_active', 'created_by')
    list_filter = ('is_active', 'start_time', 'end_time')
    search_fields = ('title', 'description', 'created_by__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    filter_horizontal = ('problems',)

@admin.register(ContestParticipation)
class ContestParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'contest', 'score', 'rank', 'joined_at')
    list_filter = ('contest', 'joined_at')
    search_fields = ('user__username', 'contest__title')
    ordering = ('-joined_at',)
    readonly_fields = ('joined_at',)

@admin.register(UserProblem)
class UserProblemAdmin(admin.ModelAdmin):
    list_display = ('user', 'problem', 'solved_at', 'attempts')
    list_filter = ('solved_at', 'attempts')
    search_fields = ('user__username', 'problem__title')
    ordering = ('-solved_at',)
    readonly_fields = ('solved_at',)
=======
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Problem, Submission, Contest, ContestParticipation, UserProblem

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'rating', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'rating')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    
    fieldsets = UserAdmin.fieldsets + (
        ('Online Judge Info', {'fields': ('bio', 'profile_picture', 'date_of_birth', 'rating')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Online Judge Info', {'fields': ('bio', 'profile_picture', 'date_of_birth', 'rating')}),
    )

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'created_by', 'is_active', 'created_at')
    list_filter = ('difficulty', 'is_active', 'created_at')
    search_fields = ('title', 'description', 'created_by__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'problem', 'language', 'status', 'execution_time', 'submitted_at')
    list_filter = ('status', 'language', 'submitted_at')
    search_fields = ('user__username', 'problem__title')
    ordering = ('-submitted_at',)
    readonly_fields = ('submitted_at', 'judged_at')

@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'is_active', 'created_by')
    list_filter = ('is_active', 'start_time', 'end_time')
    search_fields = ('title', 'description', 'created_by__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    filter_horizontal = ('problems',)

@admin.register(ContestParticipation)
class ContestParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'contest', 'score', 'rank', 'joined_at')
    list_filter = ('contest', 'joined_at')
    search_fields = ('user__username', 'contest__title')
    ordering = ('-joined_at',)
    readonly_fields = ('joined_at',)

@admin.register(UserProblem)
class UserProblemAdmin(admin.ModelAdmin):
    list_display = ('user', 'problem', 'solved_at', 'attempts')
    list_filter = ('solved_at', 'attempts')
    search_fields = ('user__username', 'problem__title')
    ordering = ('-solved_at',)
    readonly_fields = ('solved_at',)
>>>>>>> origin/main
