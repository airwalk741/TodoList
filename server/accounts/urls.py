from django.urls import path, include

app_name = 'articles'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
]
