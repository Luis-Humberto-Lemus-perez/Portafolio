from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .serializers import NoteSerializer
from .models import Note
from django.contrib.auth.hashers import check_password
from rest_framework import status
from django.http import HttpResponse

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    
@api_view(['GET'])
def getRoutes(request):
    routes = [
       '/api/token',
       '/api/token/refresh',
    ]
    return JsonResponse(routes, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    superuser = User.objects.filter(is_superuser=True).first()
   
    
    
       
        
    
    
    if check_password(request.data['password'], superuser.password):
        serializer = MyTokenObtainPairSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

   
            user = serializer.user
            #user = serializer.user
            refresh = serializer.get_token(user)
            access = refresh.access_token

        response_data = {
            
            'token': str(access),
            'user': {
            'pk': superuser.pk,
            'username': superuser.username,
            'email': superuser.email,
            }
        }
        
        return Response(response_data, status=200)
        
    message = "Invalid user or  password"
    return JsonResponse(status=401, data={'status':'false','message':message})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSuperUserInfo(request):
    try:
        superuser = User.objects.filter(is_superuser=True).first()
        if superuser:
           
            user_data = [{'pk': superuser.pk,
                
                    
                    'username': superuser.username,
                    'email': superuser.email,
                    },]

                    
                
                
        
            return Response(user_data, status=200)
        else:
            return JsonResponse({"mensaje": "No superuser found"}, status=404)
    except Exception as e:
        return JsonResponse({"mensaje": f"Error: {str(e)}"}, status=400)

        
        
        
    except:
        return Response({"mensaje": "Error"}, status=400)
    

