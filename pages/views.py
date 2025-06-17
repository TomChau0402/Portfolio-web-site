from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

 # Create your views here.
def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method =="POST":
            form = ContactForm(request.POST)

            if form.is_valid():
                print("The Data is Valide")

                name = form.cleaned_data["name"]
                email = form.cleaned_data["email"]
                message = form.cleaned_data["message"]

                message_body =(
                    f"You have a new email from your portfolio \n"
                    f"Name: {name}\n"
                    f"Email: {email} \n"
                    f"Message: {message}"
                )

                try:
                    send_mail(
                        "Email from Portfolio",
                        message_body,
                        email,
                        ['tung.t.t.chau@gmail.com']
                    )

                    print("Email sent successfully")

                    return render(request, 'pages/contact.html', {
                        'form':form
                    })

                except Exception as e:
                    print(f"ERROR sending the email:  {e}")
                    return render(request, 'pages/contact.html', {
                        'form':form,
                        'error': str(e)
                    })
            else:
                print("The Data is not Valid")

    else:
        form = ContactForm()
        
    return render(request, 'pages/contact.html', {"form": form})


def website_view(request):
    return render(request, 'pages/website.html')

def template_view(request):
    return render(request, 'pages/template.html')

def resume_view(request):
    return render(request, 'pages/resume.html')