from project.models import Project

def assigned_projects(request):
	projects = Project.objects.filter(assignees__id=request.user.id)
	return {"assigned_projects":projects}

