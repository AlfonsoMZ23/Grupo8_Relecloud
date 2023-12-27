##NOT GLOBAL (relecloud)

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('destinations', views.destinations, name='destinations'),
    path('destination/<int:pk>', views.DestinationDetailView.as_view(), name='destination_detail'),
    path('opinions', views.opinions, name='opinions'),
    path('cruise/<int:pk>', views.CruiseDetailView.as_view(), name='cruise_detail'),
    path('info_request', views.InfoRequestCreate.as_view(), name='info_request'),
    path('destination/add', views.DestinationCreateView.as_view(), name='destination_form'),
    path('destination/<int:pk>/update', views.DestinationUpdateView.as_view(), name='destination_form'),
    path('destination/<int:pk>/delete', views.DestinationDeleteView.as_view(), name='destination_confirm_delete'),
    path('opinions_form', views.OpinionForm.as_view(), name='opinions_form')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)