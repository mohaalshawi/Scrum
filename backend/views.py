from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from twilio.rest import Client
import random

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Generate OTP
            otp = random.randint(100000, 999999)
            user.set_password(otp)
            user.save()

            # Send OTP to user's phone number
            account_sid = 'your_twilio_account_sid'
            auth_token = 'your_twilio_auth_token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                     body=f"Your OTP is {otp}",
                     from_='+1234567890',  # Your Twilio number
                     to=f"+{user.phone_number}"
                 )
            return redirect('otp_verification')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})