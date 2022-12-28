from django.shortcuts import render
from.models import Course, Students
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.

@csrf_exempt
def courseview(request):
    if request.method == 'GET':

        model = Course.objects.all()

        context = {
            'model' : model,
        }
        return render(request, 'home.html', context)

    elif request.method == 'POST':

        var1 = request.POST['arg1']
        var2 = request.POST['arg2']
        course_instance = Course.objects.get(course_id=request.POST['arg3'])
        new_rating = (float(var2) +course_instance.course_ratings)/2.0
        new_comment = course_instance.course_reviews + "\n" + var1
        course_instance.course_ratings = new_rating
        course_instance.course_reviews = new_comment
        course_instance.save()

        response = {'id': course_instance.course_id, 'name': course_instance.course_name, 'rating': course_instance.course_ratings, 'review': course_instance.course_reviews}
        return JsonResponse(response)
