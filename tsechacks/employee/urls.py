from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
path('edashboard/',views.edashboard,name="edashboard"),
path('charte/',views.charte,name="charte"),
path('table/',views.table,name="table"),
path('addevent/',views.addevent,name="addevent"),
path('addstudent/',views.addstudent,name="addstudent"),
path('events/',views.events,name="events"),
path('addeventactions/',views.addeventactions,name='addeventactions'),
path('studentreg/',views.studentreg,name="studentreg"),
path('tables/',views.tables,name="tables"),
]
