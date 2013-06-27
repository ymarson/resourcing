# Create your views here.

from django.http import HttpResponse
from res.models import Schedule, Employee, Manager
from django.utils import timezone
def index(request):

    #monthly_grid = Schedule.objects.filter(employee.manager=1).filter(day>timezone.now()-datetime.timedelta(days=30))
    #monthly_grid = Schedule.objects.filter(employee__manager__id=1).filter(day>timezone.now())
    monthly_grid = Schedule.objects.filter(day__year=timezone.now().year)
    output = ",".join([p.activity.name for p in monthly_grid])
	dddddd
    return HttpResponse(output)
