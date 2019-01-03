from django.shortcuts import render
from myzehut_app.models import PorteCarte, TehudaZehut, Passeport
from myzehut_app.forms import  LoginForm
# from myzehut_app.forms import ContactForm



# Create your views here.
def index(request):
  return render(request,'index.html')

def tehudas(request):
  tzs = TehudaZehut.objects.all()
  return render(request, 'tehuda.html', context={'tzs': tzs })

def tehuda(request , tehuda_id):
  tehuda = TehudaZehut.objects.get(id=tehuda_id)
  return render(request, 'tehud.html',context={'tehuda':tehuda})


def passeports(request):
  pss=Passeport.objects.all()
  return render (request , 'passeport.html', context={'pss':pss})

def passeport(request , passeport_id):
  ps=Passeport.objects.get(id=passeport_id)
  return render (request , 'passepor.html' , context={'ps':ps})

def portecartes(request):
  pts=PorteCarte.objects.all()
  return render ( request , 'portecarte.html' , context={'pts':pts})

def portecarte(request , portecarte_id):
  pt =PorteCarte.objects.get(id=portecarte_id)
  return render ( request , 'portecart.html' , context={'pt':pt})

def contact(request):
  if request.method == 'POST':
    subject = request.POST.get('subject')
    email = request.POST.get('email')
    text = request.POST.get('text')
    Contact.objects.get_or_create(subject=subject, email=email, text=text)
    return redirect('success/')

  return render(request, 'contact.html', context={ 'contact_form': ContactForm() })

def chekout (request):
  return render(request ,'chekout.html' )

def login_auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('/profile_app/profile/{}'.format(user.id))

    return render(request, 'login.html', context= {'login_form': LoginForm()})
  
def logout_auth(request):
    logout(request)
    return redirect('/myzehut_app/')


