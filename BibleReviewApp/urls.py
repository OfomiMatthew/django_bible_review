from django.urls import path 
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # path('signup/', views.signup, name='signup')
  path('<int:bible_id>',views.detail,name='detail'),
  path('<int:bible_id>/create',views.createReview,name='create-review'),
  path('review/<int:review_id>',views.updateReview,name='update-review'),
  path('review/<int:review_id>/delete',views.deleteReview,name='delete-review'),
]