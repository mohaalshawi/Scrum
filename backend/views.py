from django.http import JsonResponse
from django.views import View
from .models import User

class UserDashboardView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all().values()  # get all users
        user_list = list(users)  # convert to list
        return JsonResponse(user_list, safe=False)  # return response as JSON