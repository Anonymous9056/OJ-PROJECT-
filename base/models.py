from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    """Custom User model for the online judge system"""
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    rating = models.IntegerField(default=1200)
    solved_problems = models.ManyToManyField('Problem', through='UserProblem', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Problem(models.Model):
    """Model for coding problems"""
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    time_limit = models.IntegerField(default=1000)  # in milliseconds
    memory_limit = models.IntegerField(default=256)  # in MB
    input_format = models.TextField()
    output_format = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    test_cases = models.JSONField()  # Store test cases as JSON
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_problems')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Submission(models.Model):
    """Model for code submissions"""
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('java', 'Java'),
        ('cpp', 'C++'),
        ('c', 'C'),
        ('javascript', 'JavaScript'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('accepted', 'Accepted'),
        ('wrong_answer', 'Wrong Answer'),
        ('time_limit_exceeded', 'Time Limit Exceeded'),
        ('memory_limit_exceeded', 'Memory Limit Exceeded'),
        ('runtime_error', 'Runtime Error'),
        ('compilation_error', 'Compilation Error'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='submissions')
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    code = models.TextField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='pending')
    execution_time = models.FloatField(blank=True, null=True)  # in seconds
    memory_used = models.FloatField(blank=True, null=True)  # in MB
    submitted_at = models.DateTimeField(auto_now_add=True)
    judged_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {self.status}"

class Contest(models.Model):
    """Model for programming contests"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    problems = models.ManyToManyField(Problem, blank=True)
    participants = models.ManyToManyField(User, through='ContestParticipation', blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_contests')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def is_running(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time

class ContestParticipation(models.Model):
    """Model for contest participation"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'contest']

    def __str__(self):
        return f"{self.user.username} - {self.contest.title}"

class UserProblem(models.Model):
    """Model to track user's solved problems"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    solved_at = models.DateTimeField(auto_now_add=True)
    attempts = models.IntegerField(default=1)
    best_submission = models.ForeignKey(Submission, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        unique_together = ['user', 'problem']

    def __str__(self):
        return f"{self.user.username} solved {self.problem.title}"
