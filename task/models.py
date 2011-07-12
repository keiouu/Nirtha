from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = (('0', 'Bug'),('1', 'Feature'),('2', 'Enhancement'))
SEVERITY_CHOICES = (('0', 'Critical'),('1', 'High'),
                    ('2', 'Medium'),('3', 'Low'))

# A task
class Task(models.Model):
	project = models.ForeignKey('project.Project')
	title = models.CharField(max_length=150)
	type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='0')
	severity = models.CharField(max_length=2, choices=SEVERITY_CHOICES, default='2')
	progress = models.PositiveIntegerField(default=0)
	description = models.TextField()
	assignees = models.ManyToManyField(User, related_name='task_assignees')
	created_by = models.ForeignKey(User, related_name='task_created_by')
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
