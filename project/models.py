from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from task.models import Task

# Project auth levels determine what
# permissions users have on a particular project
class ProjectAuthLevel(models.Model):
	task_add = models.BooleanField(default=True)
	task_edit = models.BooleanField(default=False)
	subproject_add = models.BooleanField(default=False)
	subproject_edit = models.BooleanField(default=False)
	
	class Meta:
		unique_together = ("task_add", "task_edit", "subproject_add", "subproject_edit")

# Links projects with assignees and auth levels
class ProjectMembership(models.Model):
	project = models.ForeignKey('project.Project')
	user = models.ForeignKey(User)
	level = models.ForeignKey(ProjectAuthLevel)

# A project
class Project(models.Model):
	parent = models.ForeignKey('project.Project', null=True)
	title = models.CharField(max_length=150)
	description = models.TextField()
	assignees = models.ManyToManyField(User, related_name='project_assignees', through='project.ProjectMembership')
	created_by = models.ForeignKey(User, related_name='project_created_by')
	created_on = models.DateTimeField(auto_now_add=True)
	
	@property
	def age(self):
		return (datetime.now() - self.created_on).days
	
	@property
	def number_of_assignees(self):
		return ProjectMembership.objects.filter(project=self).count()
	
	@property
	def tasks(self):
		return Task.objects.filter(project=self.pk)

# A target (like a milestone)
class Target(models.Model):
	project = models.ForeignKey(Project)
	title = models.CharField(max_length=150)
	description = models.TextField()
	created_by = models.ForeignKey(User)
	created_on = models.DateTimeField()
