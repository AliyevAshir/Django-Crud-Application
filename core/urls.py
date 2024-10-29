from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, PositionViewSet, EmployeeViewSet
from .views import UserRegisterView, UserLoginView
router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'employees', EmployeeViewSet)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', TokenRefreshView.as_view(), name='token_refresh'),  # Uncomment for JWT authentication
    path('register/', UserRegisterView.as_view(), name='register'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
# urls.py (add new paths)

# employees/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DepartmentViewSet, PositionViewSet, EmployeeViewSet,
    AttendanceViewSet, PerformanceReviewViewSet, TrainingViewSet,
    CompensationViewSet, DocumentViewSet, MessageViewSet,
    OnboardingItemViewSet, OffboardingItemViewSet
)

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'employees/(?P<employee_id>[^/.]+)/attendance', AttendanceViewSet, basename='attendance')
router.register(r'employees/(?P<employee_id>[^/.]+)/performance', PerformanceReviewViewSet, basename='performance')
router.register(r'employees/(?P<employee_id>[^/.]+)/training', TrainingViewSet, basename='training')
router.register(r'employees/(?P<employee_id>[^/.]+)/compensation', CompensationViewSet, basename='compensation')
router.register(r'employees/(?P<employee_id>[^/.]+)/documents', DocumentViewSet, basename='documents')
router.register(r'messages', MessageViewSet)
router.register(r'employees/(?P<employee_id>[^/.]+)/onboarding', OnboardingItemViewSet, basename='onboarding')
router.register(r'employees/(?P<employee_id>[^/.]+)/offboarding', OffboardingItemViewSet, basename='offboarding')

urlpatterns = [
    path('', include(router.urls)),
]

