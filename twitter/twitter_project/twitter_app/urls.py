from django.urls import path, include

from .views import api_user_list_view, api_update_tweet_view, api_create_tweet_view, api_user_id_list_view, \
  api_tweet_list_view, api_tweet_id_list_view

urlpatterns = [
  path('users/', api_user_list_view, name ='user'),
  path('users/id/',api_user_id_list_view, name='user_record'),
  path('create/',api_create_tweet_view,name="create_tweet"),
  path('update/',api_update_tweet_view,name='delete_post'),
  path('update/tweet',api_tweet_list_view, name = "update_tweet"),
  path('update/id/',api_tweet_id_list_view, name = 'update_tweet'),

]