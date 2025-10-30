from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename='employee')
urlpatterns = [
    path('students/',views.studentView),
    path('student/<int:pk>/',views.studentdetailview),
    # path('employees/',views.Employees.as_view()), # class based view
    # path('employees/<int:pk>/',views.EmployeeDetail.as_view()), # class based view  
    path('',include(router.urls))
]