from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages
from django.template.loader import get_template
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    a=About.objects.all()
    e=Experience.objects.all()
    ed=Education.objects.all()
    i=Interest.objects.all()
    s=Skill.objects.all()
    p=Project.objects.all()
    if request.method =="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        message=request.POST["message"]
        
        data=Contact(name=name,email=email,message=message)
        data.save()
        msg_plain = render_to_string('email.txt')
        msg_html = render_to_string('thankyou.html')
        recipient = request.POST.get('email')
        send_mail("Thank you for contacting us", msg_plain, settings.EMAIL_HOST_USER,
                    [recipient], html_message = msg_html)

        subject = 'Message Received from ' + email 
        message = request.POST.get('message')
        sender = settings.EMAIL_HOST_USER
        recipient = (settings.EMAIL_HOST_USER)

        send_mail(
            subject,
            message,
            sender,
            [recipient]
        )
        
    return render(request,'index.html',{'about':a,'exp':e,'edu':ed,'interest':i,'skill':s,'project':p })