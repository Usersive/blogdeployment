from django.shortcuts import render, redirect
from django.contrib import messages
from subscribe.models import Subscribe

# Create your views here.
def subscribe(requests):
    email_error_empty=""
    if requests.POST:
        name = requests.POST['name']
        email = requests.POST['email']
        subject = requests.POST['subject']
        message = requests.POST['message']
        print('Post Request', email)
        if email=="":
            email_error_empty = 'No email entered'
            
            
        subscribe = Subscribe(name = name, email=email, subject=subject, message=message) 
        subscribe.save() 
        messages.success(requests, "Your message sent successfully!")
        return redirect('subscribe')
        
        
              
                    
    
    contexts ={"email_error_empty": email_error_empty}
    return render (requests, 'subscribe/subscribe.html', contexts )
    
