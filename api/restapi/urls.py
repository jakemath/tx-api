"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin
from api.resources import TransactionResource
from api import views

transaction_resource = TransactionResource() #Resource instance for accessing specific record

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'dataengr/',include(transaction_resource.urls)), #Path to generate a record of choice
    path(r'dataengr/revenue/', views.Revenue,name='Revenue'),	#Path to generate revenue computation
    path(r'dataengr/activeusers/', views.ActiveUserCount),	#Path to generate activeusers computation
    path(r'dataengr/newusercount/',views.NewUserCount),		#Path to generate newusers computation
    path(r'dataengr/arpau/',views.AverageRevenue),	#Path to generate averagerevenue computation 
]
