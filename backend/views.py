from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Invitation
from .forms import InvitationForm

@login_required
def invite_view(request):
    if request.method == 'POST':
        form = InvitationForm(request.POST)
        if form.is_valid():
            invitation = form.save(commit=False)
            invitation.sent_by = request.user
            invitation.save()
            # Here you can add email sending logic
            return redirect('home')
    else:
        form = InvitationForm()
    return render(request, 'invite.html', {'form': form})