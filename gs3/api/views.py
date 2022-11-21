
from django.shortcuts import render,HttpResponse
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentApi(View):
    def get(self,request,*args,**kwargs):
         jason_data = request.body
         stream = io.BytesIO(jason_data)
         pythondata =JSONParser().parse(stream)
         print(pythondata)
         id = pythondata.get('id',None)
         if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            jason_data=JSONRenderer().render(serializer.data)
            return HttpResponse(jason_data, content_type='appliction/jason') 
         stu=Student.objects.all()
         serializer=StudentSerializer(stu,many=True)
         jason_data=JSONRenderer().render(serializer.data)
         return HttpResponse(jason_data, content_type='appliction/jason')
        









# def get(request):
#     if request.method == 'GET':
#         jason_data = request.body
#         stream = io.BytesIO(jason_data)
#         pythondata =JSONParser().parse(stream)
#         print(pythondata)
#         id = pythondata.get('id',None)
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             jason_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(jason_data, content_type='appliction/jason')
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         jason_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(jason_data, content_type='appliction/jason')
    def post(self,request,*args,**kwargs):
         json_data=request.body
         stream=io.BytesIO(json_data)
         pythondata=JSONParser().parse(stream)
         serializer=StudentSerializer(data=pythondata)
         if serializer.is_valid():
            serializer.save()
            res={'msg':'create sussesfully'}
            jason_data=JSONRenderer().render(res)
            return HttpResponse(jason_data,content_type='appliction/jason')

         jason_data=JSONRenderer().render(serializer.errors)
         return HttpResponse(jason_data,content_type='appliction/jason')

    def put(self,request,*args,**kwargs):
        if request.method=='PUT':
         jason_data=request.body
         stream=io.BytesIO(jason_data)
         pythondata=JSONParser().parse(stream)
         id=pythondata.get('id')
         stu=Student.objects.get(id=id)
         serializer=StudentSerializer( stu,data=pythondata)
         if serializer.is_valid():
            serializer.save()
            res={'msg':'create sussesfully'}
            jason_data=JSONRenderer().render(res)
            return HttpResponse(jason_data,content_type='appliction/jason')

         jason_data=JSONRenderer().render(serializer.errors)
         return HttpResponse(jason_data,content_type='appliction/jason')

        

    def delete(self,request,*args,**kwargs):
        if request.method=='DELETE':
         jason_data=request.body
         stream=io.BytesIO(jason_data)
         pythondata=JSONParser().parse(stream)
         id=pythondata.get('id')
         stu=Student.objects.get(id=id)
         stu.delete()
         res={'msg':'delete data'}
         jason_data=JSONRenderer().render(res)
         return HttpResponse(jason_data,content_type='appliction/jason')
        

        


        


