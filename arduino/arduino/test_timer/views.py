from django.http import HttpResponse
from .models import Time
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
def timer(request):
    if request.method == 'POST':
        # print('тело запроса: ', request.body)
        rid, uid = request.body.decode().split(',')
        # print(rid)
        # print(uid)
        time_obj = Time.objects.filter(uid=uid, rid=rid).first()
        if not time_obj:
            return HttpResponse('1000')
        return HttpResponse(time_obj.timer)
    return HttpResponse('1111111')


