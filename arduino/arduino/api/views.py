from django.http import JsonResponse, HttpResponse
from test_timer.models import Players
from rest_framework import viewsets
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = TaskSerializer

def user_playtime(request):
    if request.method == 'POST':
        rid, uid = request.body.decode().split(',')
        player_now = Players.objects.filter(uid=uid, rid=rid).order_by('user_time_start')
        player_now.save()
        return HttpResponse(player_now.user_number)
        print(HttpResponse)
    return HttpResponse('jopa')
    print(HttpResponse)
