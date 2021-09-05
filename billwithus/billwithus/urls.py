"""billwithus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from bill_with_us import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('services/', views.services,name="services"),
    path('services/mobile-recharge', views.mobile_recharge,name="mobile_recharge"),
    path('services/dth-recharge', views.dth_recharge,name="dth_recharge"),
    path('services/credit-recharge', views.credit_recharge,name="credit_recharge"),
    path('services/metro-recharge', views.metro_recharge,name="metro_recharge"),
    path('services/water-recharge', views.water_recharge,name="water_recharge"),


    path('services/electricity-recharge', views.electricity_recharge,name="electricity_recharge"),
    # path('services/finalebill', views.finalebill,name="finalebill"),


    path('services/cylinder-pay', views.cylinder_pay,name="cylinder_pay"),
    path('services/fast_toll-recharge', views.fast_toll_recharge,name="fast_toll_recharge"),
    path('services/broad_band-recharge', views.broad_band_recharge,name="broad_band_recharge"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400='bill_with_us.views.error_400'
handler403='bill_with_us.views.error_403'
handler404='bill_with_us.views.error_404'
handler500='bill_with_us.views.error_500'