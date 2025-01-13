from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import College
from .serializers import CollegeSerializer

class CollegeListView(APIView):
    def get(self, request):
        colleges = College.objects.all()  # Fetch all college records
        serializer = CollegeSerializer(colleges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CollegeDetailView(APIView):
    def get(self, request, pk):
        try:
            college = College.objects.get(pk=pk)
        except College.DoesNotExist:
            return Response({"error": "College not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CollegeSerializer(college)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            college = College.objects.get(pk=pk)
        except College.DoesNotExist:
            return Response({"error": "College not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CollegeSerializer(college, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            college = College.objects.get(pk=pk)
        except College.DoesNotExist:
            return Response({"error": "College not found"}, status=status.HTTP_404_NOT_FOUND)
        college.delete()
        return Response({"message": "College deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
