from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
  path('upload', views.upload_view, name='upload-view'),
  path('upload_hfd', views.upload_hfd, name='upload-hfd'),
  path('update_data/<data_id>', views.update_data, name='update-data'),
  path('update_hfd/<hfd_id>', views.update_hfd, name='update-hfd'),
  path('delete_data/<data_id>', views.delete_data, name='delete-data'),
  path('delete_hfd/<hfd_id>', views.delete_hfd, name='delete-hfd'),
  path('show_data/all', views.list_data, name='list-data'),
  path('show_data/<data_id>', views.show_data, name='show-data'),
  path('show_hfd/<hfd_id>', views.show_hfd, name='show-hfd'),
  path('show_indicator/<data_id>', views.show_indicator, name='show-indicator'),
  path('fillout_timeliness/<data_id>', views.fillout_timeliness, name='fillout-timeliness'),
  path('fillout_security/<data_id>', views.fillout_security, name='fillout-security'),
  path('download_rawdata', views.download_rawdata, name='download-rawdata'),
  path('download_attrdata', views.download_attrdata, name='download-attrdata'),
  path('download_used_data/<data_id>', views.download_used_data, name='download-used-data'),
  path('recalculate_indicator/<data_id>', views.recalculate_indicator, name='recalculate-indicator'),
  path('transform_hfd/<hfd_id>', views.transform_hfd, name='transform-hfd'),
]