from rest_framework import serializers
from .models import User, AssignmentType, Class, Assignment

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email', 'class_set', 'assignment_set']

class ClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = Class
		fields = ['grade', 'name', 'user', 'assignmenttype_set']

class AssignmentTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = AssignmentType
		fields = ['weight', 'klass', 'name', 'number_of_assignments', 'assignment_set']

class AssignmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Assignment
		fields = ['grade', 'due_date', 'assignmentType', 'completed', 'user', 'ass_number']