from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Assignment, AssignmentType, Class
from .serializer import UserSerializer, AssignmentSerializer, AssignmentTypeSerializer, ClassSerializer
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.core import serializers
import json
import datetime as dt
from datetime import datetime

# Create your views here.

@api_view(['GET'])
def get_assignments(request):
    asses1 = Assignment.objects.filter(user=int(request.GET.get('user')))    
    ass_serializer = AssignmentSerializer(asses1, many=True)
    data = ass_serializer.data
    filtered_data = []
    filtered_count = 0
    for count in range(0, len(data)):
        try:
            due_date = datetime.strptime(data[count]['due_date'], "%Y-%m-%dT%H:%M:%SZ")
        except:
            due_date = datetime.strptime(data[count]['due_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        if(datetime.now() + dt.timedelta(days=7) > due_date and datetime.now()  < due_date):
            print(datetime.now() + dt.timedelta(days=7) < due_date)
            data[count]['class'] = asses1[count].assignmentType.klass.name
            data[count]['assignment_type_name'] = asses1[count].assignmentType.name
            data[count]['pk'] = asses1[count].pk
            filtered_data.append(data[count])
            

    return Response(filtered_data)

@api_view(['GET'])
def get_classes(request):
    classes = Class.objects.filter(user=int(request.GET.get('user')))
    class_serializer = ClassSerializer(classes, many=True)
    data = class_serializer.data
    for count in range(0, len(data)):
        data[count]['pk'] = classes[count].pk

    return Response(data)

@api_view(['GET'])
def log_me_in(request):
    try:
        user = User.objects.get(email=request.GET.get('email'))
    except:
        return Response(-1)
    
    if(user.password == request.GET.get('password')):
        print("Success")
        return Response(user.pk)
    else:
        print("Failed")
        return Response(-1)

@api_view(['POST'])
def sign_me_up(request):
    body_uni = request.body.decode('utf-8')
    body = json.loads(body_uni)
    print(body)
    nu = User.objects.create(username=body['email'], email=body['email'], password=body['password'])
    
    return Response(nu.pk)

@api_view(['GET'])
def get_ass_types_class(request):
    print(request.GET.get('classId'))
    klass = Class.objects.get(pk=request.GET.get('classId'))
    class_serializer = ClassSerializer(klass)
    data = class_serializer.data

    ass_types = data['assignmenttype_set']
    ass_objects_dict = {}
    for ass_type in ass_types:
        ass_type_object = AssignmentType.objects.get(pk=ass_type)
        ass_objects_dict[ass_type_object.name] = AssignmentSerializer(ass_type_object.assignment_set, many=True).data
        ass_objects_dict[ass_type_object.name].insert(len(ass_objects_dict[ass_type_object.name]), ass_type_object.weight)
    return Response(ass_objects_dict)

@api_view(['POST'])
def create_class(request):
    body_uni = request.body.decode('utf-8')
    body = json.loads(body_uni)
    _user = User.objects.get(pk = body['classObject']['user'])
    c = Class.objects.create(name=body['classObject']['name'], grade = 0, user = _user)
    
    #Now I want to create all of the appropriate assignment type objects
    assTypes = []
    for assType in body['assignmentTypeObjects']:
        assTypes.append(AssignmentType.objects.create(name=assType['name'], weight=assType['weight'], number_of_assignments=assType['numberOfAssignments'], klass=c))

    # Now for each assType I need to create the appropriate amount of assignments
    count = 0
    for assType in body['assignmentTypeObjects']:
        ass_count = 1
        for ass in range(0, assType['numberOfAssignments']):
            Assignment.objects.create(grade=0, due_date=dt.datetime(2000,6,13,0,0), assignmentType=assTypes[count], completed=False, user = _user, ass_number = ass_count)
            ass_count = ass_count + 1

        count = count + 1    
    return Response('Dope it worked')

@api_view(['PUT'])
def set_completed(request):
    body_uni = request.body.decode('utf-8')
    body = json.loads(body_uni)

    ass = Assignment.objects.get(pk=body['assignmentId'])
    ass.completed = not ass.completed
    ass.save()

    return Response("Completed changing completed")

@api_view(['PUT'])
def update_due_date(request):
    body_uni = request.body.decode('utf-8')
    body = json.loads(body_uni)

    ass = Assignment.objects.get(pk=body['assignmentId'])
    ass.due_date = body['newDate']
    ass.save()

    return Response("Let's go it worked! Date has been saved")

@api_view(['PUT'])
def update_assignment(request):
    body_uni = request.body.decode('utf-8')
    body = json.loads(body_uni)

    assType = AssignmentTypeSerializer(AssignmentType.objects.get(pk=body['assTypeId'])).data
    ass = Assignment.objects.get(pk=assType['assignment_set'][body['assIndex']])
    
    ass.due_date = body['newData']['due_date']
    ass.grade = body['newData']['grade']

    if(int(body['newData']['grade'] != 0)):
        ass.completed = True

    ass.save()
    return Response("Saved")
