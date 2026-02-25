from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        message = request.POST.get("message")

        subject = f"New Contact Form Message from {name}"
        body = f"""
        Name: {name}
        Email: {email}
        Contact No: {contact}

        Message:
        {message}
        """

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],  # SEND TO YOU
            fail_silently=False,
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect('/contact/')

    return render(request, "contact.html")