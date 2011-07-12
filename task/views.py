from django.views.generic.simple import direct_to_template
from django.http import HttpResponse
from task.models import Task
from project.models import Project

def tasks_view(request):
	#TODO - check permissions
	return direct_to_template(request=request, template="tasks/tasks.html")
    
def task_view(request, id):
	#TODO - check permissions
	task = Task.objects.get(pk=id)
	return direct_to_template(request=request, template="tasks/task.html", extra_context={"task":task})

def tasks_new_view(request):
	#TODO - check permissions
	try:
		o = Task(	project=Project.objects.get(id=request.GET['project']),
					title=request.GET['title'],
					type=request.GET['type'],
					severity=request.GET['severity'],
					description=request.GET['description'],
					created_by=request.user)
		o.save()
	except:
		return HttpResponse("Something went wrong!")
	return HttpResponse("1")
