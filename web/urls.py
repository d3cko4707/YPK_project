from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'web_app'

urlpatterns = [
                  url(r'^$', views.Homepage, name='home_page'),
                  url(r'^about/$', views.About, name='about_page'),
                  url(r'^event/$', views.Event, name='events_page'),
                  url(r'^news/$', views.NewsRoom, name='news_page'),
                  url(r'^member/$', views.Membership, name='membership_page'),
                  url(r'^join/$', views.Join, name='join_page'),
                  url(r'^donate/$', views.Donate, name='donate_page'),
                  url(r'^sing-in/$', views.Sign_in, name='sign_in_page'),
                  url(r'^sign-in/(?P<goto>\w+:\w+)/$', views.Sign_in, name='sign_in_goto'),
                  url(r'^register/$', views.Register, name='register_page'),
                  url(r'^sign_out/$', views.Sign_out, name='sign_out_page'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
