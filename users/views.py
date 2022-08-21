from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import New
from .serializers import NewSerializer
# Create your views here.


class CustomUserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = New.objects.all()
    serializer_class = NewSerializer


#problem is here
class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            refresh_token = request.data("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

