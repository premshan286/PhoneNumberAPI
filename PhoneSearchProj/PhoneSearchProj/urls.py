"""PhoneSearchProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from PhoneSearchApi import views

urlpatterns = [
    path('search-api-index/', include('PhoneSearchApi.urls')),
    path('admin/', admin.site.urls),
    path('search-by-country-code-api/', views.search_by_countryCode_api),
    path('search-by-region-code-api/', views.search_by_regionCode_api),
    path('search-by-localexchange-code-api/', views.search_by_localExchangeCode_api),
    path('search-by-number-api/', views.search_by_number_api),
    path('search-api/', views.search_api),
    
]
