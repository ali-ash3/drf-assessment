from rest_framework import viewsets
from .models import Author, Book, Genre
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from datetime import datetime



# Create your views here.

# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 1000


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('title' ,'author', 'genre')



    
class AddAuthor(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        author_birth_date = request.data.get("birth_date")
        current_date = date.today()
        date_object = datetime.strptime(author_birth_date, '%Y-%m-%d').date()

        try:
            if not date_object >= current_date:
                if serializer.is_valid():
                    serializer.save()
                    return Response({"data": serializer.data})
            return Response({"error":"enter valid date"})
        except Exception as e:
            return Response({"error":str(e)})
        
    def get(self, request):
        books = Author.objects.all()
        serializer = AuthorSerializer(books, many=True)
        return Response({'data': serializer.data})

            
    


"""
access all fields form request
validate from serializer
then save and return response



"""
