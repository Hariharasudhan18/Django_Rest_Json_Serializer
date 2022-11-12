from rest_framework import serializers

from .models import EmployeeModel

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ('employee_id', 'name', 'age', 'position', 'email')