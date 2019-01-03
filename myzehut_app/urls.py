from django.urls import path
from . import views

app_name = 'myzehut_app'

urlpatterns = [
  path('', views.index, name='index'),
  path('products/', views.tehudas, name='product'),
  path('products/<int:tehuda_id>', views.tehuda, name='product'),
  path('passeports/',views.passeports, name='passeports'),
  path('passeports/<int:passeport_id>',views.passeport, name='passeport'),
  path('portecartes/',views.portecartes, name='portecartes'),
  path('portecartes/<int:portecarte_id>',views.portecarte, name='portecarte'),
  path('chekout/',views.chekout, name='chekout'),
  path('login/', views.login_auth, name='login'),
  path('logout/',views.logout_auth , name='logout'),
  path('contact/', views.contact, name='contact'),
]
