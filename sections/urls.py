from django.urls import path

from rest_framework.routers import DefaultRouter

from sections.apps import SectionsConfig
from sections.views import SectionListAPIView, SectionCreateAPIView, SectionRetrieveAPIView, SectionUpdateAPIView, \
    SectionDestroyAPIView, SectionContentListAPIView, SectionContentCreateAPIView, SectionContentRetrieveAPIView, \
    SectionContentUpdateAPIView, SectionContentDestroyAPIView

app_name = SectionsConfig.name

router = DefaultRouter()

urlpatterns = [
    # Section url patterns
    path('section/', SectionListAPIView.as_view(), name='section-list'),
    path('section/create/', SectionCreateAPIView.as_view(), name='section-create'),
    path('section/<int:pk>/', SectionRetrieveAPIView.as_view(), name='section-retrieve'),
    path('section/<int:pk>/update/', SectionUpdateAPIView.as_view(), name='section-update'),
    path('section/<int:pk>/destroy/', SectionDestroyAPIView.as_view(), name='section-destroy'),

    # SectionContent url patterns
    path('content/', SectionContentListAPIView.as_view(), name='section-content-list'),
    path('content/create/', SectionContentCreateAPIView.as_view(), name='section-content-create'),
    path('content/<int:pk>/', SectionContentRetrieveAPIView.as_view(), name='section-content-retrieve'),
    path('content/<int:pk>/update/', SectionContentUpdateAPIView.as_view(), name='section-content-update'),
    path('content/<int:pk>/destroy/', SectionContentDestroyAPIView.as_view(), name='section-content-destroy'),
] + router.urls
