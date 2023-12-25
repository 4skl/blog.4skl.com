from django.urls import path
from .views import DumpDataView, LoadDataView

app_name = 'loaddumpdata'

urlpatterns = [
    path('dump-data/', DumpDataView.as_view(), name='dump_data'),
    path('load-data/', LoadDataView.as_view(), name='load_data'),
]
