from django.views.generic.simple import direct_to_template
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from project.models import Project
from task.models import Task
from settings import NUMBER_OF_WHATS_NEW

# This should return an ordered list of new projects, tasks, comments and changes
def whats_new():
	class Entry(object):
		date = 0
		value = ""
		url = ""
		def __init__(self, date, value, url):
			self.date = date
			self.value = value
			self.url = url
		def __str__(self): return self.value
		def __unicode__(self): return self.value
	
	# TODO - check permissions
	lst = []
	# Go through every project, get changes and add to list
	# TODO - currently only handles additions
	projects = Project.objects.all().order_by('-created_on')
	for project in projects:
		tasks = Task.objects.filter(project=project).order_by('-created_on')
		for task in tasks:
			e = Entry(	date=task.created_on, 
						value="New task entitled \"%s\" was created by %s in \"%s\"." % 
								(task.title, task.created_by, task.project.title),
						url="/tasks/%s/"%task.pk)
			lst.append(e)
			#if task.updated_on > task.created_on:
			#	e = Entry(	date=task.updated_on, 
			#			value="Task updated: \"%s\" on %s." % 
			#					(task.title, task.updated_on))
			#	lst.append(e)
		e = Entry(	date=project.created_on,
					value="New project entitled \"%s\" was created by %s." % 
							(project.title, project.created_by),
					url="/projects/%s/"%project.pk)
		lst.append(e)
	# Do the sorting!
	lst = sorted(lst, key=lambda a: a.date)
	lst.reverse()
	return lst[:NUMBER_OF_WHATS_NEW] # First 10 items (TODO: make configurable)

def index(request):
	return direct_to_template(request=request, template="index.html", extra_context={"whats_new":whats_new()})

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/') # TODO - page for this
        else:
            # Return a 'disabled account' error message
            return HttpResponseRedirect('/disabled') # TODO - page for this
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect('/invalid') # TODO - page for this
