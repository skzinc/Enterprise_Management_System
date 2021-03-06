from django.urls import path
from django.views.generic import TemplateView,ListView
from .import views
from django.conf.urls.static import static
from configs import settings

app_name = 'leads'
urlpatterns =[
    #path('i',views.LeadIndex.as_view(),name='LeadIndex'),
    path('details/',views.LeadDetails.as_view(),name='LeadDetails'),
    path('create/',views.LeadCreate.as_view(),name='LeadCreate'),
    path('edit/<pk>',views.LeadEdit.as_view(),name='LeadEdit'),
    path('delete/<pk>',views.LeadDelete.as_view(),name='LeadDelete'),
    path('details/assign/',views.LeadsAssign,name='leadsassign'),
    path('editajax/<int:id>',views.check),

    path('upload/csv/', views.upload_csv, name='upload_csv'),
    path('downloadpdf/<int:id>',views.DownloadPdf,name='LeadDownloadpdf'),
    path('downloadcsv/<int:id>',views.DownloadCsv,name='LeadDownloadcsv'),



]
