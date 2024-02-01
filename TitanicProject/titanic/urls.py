from django.urls import path
from titanic import views

urlpatterns = [
    path('upload-model/',views.upload_model,name='upload-model'),
    path('predict/', views.predict_view, name='predict'),

]
