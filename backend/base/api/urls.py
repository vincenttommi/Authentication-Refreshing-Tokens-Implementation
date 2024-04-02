from  django.urls  import path,include
from   . import views




urlpatterns = [
    path('', views.getRoutes),
    path('api/', include('base.api.urls'))
    
]
