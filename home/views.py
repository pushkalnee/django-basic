from rest_framework.decorators import api_view
from rest_framework.response import Response 
from home.models import *
from .serializers import transSr,logSr
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

@api_view(["GET",
           "POST",
           "PUT",
           ])


def bike(request):
       qs=trans.objects.all()
       sr=transSr(qs,many=True)
       
       return Response(sr.data)

class tranaAPI(APIView):
       permission_classes = [IsAuthenticated]

       def get(self,request):
              qs=trans.objects.all()
              sr=transSr(qs,many=True)
              return Response(sr.data)
       def post(self,request):
              data=request.data
              sr=transSr(data=data)
              if not sr.is_valid():
                    return Response(
                     {"m": sr.errors}
                     )
              sr.save()
              return Response(
                     {
                            "m":"saved"
                     }
              )
              


       def put(self,request):
              return Response(
                     {"m": "put"}
              )
       



class loginAPI(APIView):
       def post(self,request):
              data=request.data
              sr=logSr(data=data)
              if not sr.is_valid():
                     return Response(
                            {
                                   "m":sr.errors
                            }
                     )
              username=sr.data["username"]
              password=sr.data["password"]
              user_obj=authenticate(username=username,password=password)
              
              if user_obj:
                     tk , _ =Token.objects.get_or_create()
                     return Response(
                            {
                                   "m": str(tk)
                            }
                     )
              else:
                     return Response(
                            {
                                   "m": "false"
                            }
                     )


class RegisterAPI(APIView):
       def post(self,rquest):
              data=rquest.data
              sr=logSr(data=data)
              if not sr.is_valid():
                     return Response(
                            {
                                   "m":sr.errors
                            }
                     )
              username=sr.validated_data["username"]
              password=sr.validated_data["password"]
              if User.objects.filter(username=username):
                     return Response({
                                "m": "Username already taken"
                       })
              user= User.objects.create_user(username=username, password=password)
              token , _ = Token.objects.get_or_create(user=user)
        
              return Response({
                                 "m": str(token)
                                })