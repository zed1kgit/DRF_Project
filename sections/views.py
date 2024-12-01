from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, SectionContent
from sections.permissions import IsModerator
from sections.serializers.section_serializers import SectionSerializer, SectionListSerializer
from sections.serializers.section_content_serializers import SectionContentListSerializer, SectionContentSerializer
from sections.paginators import SectionPaginator, SectionContentPaginator


class SectionListAPIView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    pagination_class = SectionPaginator
    permission_classes = (IsAuthenticated,)


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionContentListAPIView(ListAPIView):
    serializer_class = SectionContentListSerializer
    queryset = SectionContent.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SectionContentPaginator


class SectionContentCreateAPIView(CreateAPIView):
    serializer_class = SectionContentSerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionContentRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionContentSerializer
    queryset = SectionContent.objects.all()
    permission_classes = (IsAuthenticated,)


class SectionContentUpdateAPIView(UpdateAPIView):
    serializer_class = SectionContentSerializer
    queryset = SectionContent.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionContentDestroyAPIView(DestroyAPIView):
    serializer_class = SectionContentSerializer
    queryset = SectionContent.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)
