from django.views.generic.simple import direct_to_template
from project.models import Project, ProjectMembership, ProjectAuthLevel
from django.http import HttpResponse

def projects_view(request):
	#TODO - check permissions
	return direct_to_template(request=request, template="projects/projects.html")
    
def project_view(request, id):
	#TODO - check permissions
	project = Project.objects.get(pk=id)
	return direct_to_template(request=request, template="projects/project.html", extra_context={"project":project})


def projects_new_view(request):
	#TODO - check permissions
	try:
		o = Project(title=request.GET['title'], description=request.GET['description'], created_by=request.user)
		o.save()
		auth, created = ProjectAuthLevel.objects.get_or_create(task_add=True, task_edit=True, subproject_add=True, subproject_edit=True)
		no = ProjectMembership(project=o, user=request.user, level=auth)
		no.save()
	except:
		return HttpResponse("Something went wrong!")
	return HttpResponse("1")
