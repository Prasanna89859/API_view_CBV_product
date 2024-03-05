from django.shortcuts import render
from app.models import *
from app.serialzers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response



# Create your views here.

class productcrud(APIView):
    def get(self,request,id):
        PDO=product.objects.all() #orm
        PJO=productModelserializers(PDO,many=True) #json
        return Response(PJO.data)
    
    def post(self,request,id):
        JDO=request.data
        PDO=productModelserializers(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is Done...'})
        else:
            return Response({'Error':'invalid data'})
    def put(self,request,id):
        po=product.objects.get(id=id)
        #po=product.objects.all()
        UPDO=productModelserializers(po,data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'insert':'Push Data is Successfully...'})
        else:
            return Response({'Error':'Push Data is Not done....'})
    def patch(self,request,id):
        po=product.objects.get(id=id)
        UPDO=productModelserializers(po,data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'updata':'Updata Data is Done....'})
        else:
            return Response({'Error':'invalid Data.....'})
    def delete(self,request,id):
        product.objects.get(id=id).delete()
        
        return Response({'delete':'Delete is Done.....'})




        
        





