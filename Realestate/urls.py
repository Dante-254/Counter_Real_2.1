# from django.urls import path
# from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('aboutus', views.aboutus, name='aboutus'),
    # path('', views.as_view, name='home'),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)