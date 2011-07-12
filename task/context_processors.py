from task.models import Task

def assigned_tasks(request):
	tasks = Task.objects.filter(assignees__id=request.user.id)
	return {"assigned_tasks":tasks}

