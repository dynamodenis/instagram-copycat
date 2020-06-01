from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name='instagram'
urlpatterns=[
    path('',views.index, name='index'),
    path('create/post/',views.new_image, name='new_image'),
    path('profile/',views.profile, name='profile'),
    path('<int:image_id>/comment/',views.comment, name='comment'),
    path('like/',views.likes, name='likes'),
    path('follow/',views.follow, name='follow'),
    path('search/',views.search, name='search'),
    path('<int:user_id>/profile',views.post_user, name='post_user'),
    path('update/',views.update_profile, name='update_profile'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
