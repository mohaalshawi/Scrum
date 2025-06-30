from django.views import generic
from .models import UserProfile

class UserDashboardView(generic.ListView):
    model = UserProfile
    template_name = 'user_dashboard.html'
    context_object_name = 'user_profiles'

    def get_queryset(self):
        return UserProfile.objects.all().order_by('-registration_date')