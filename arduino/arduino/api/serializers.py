from rest_framework import serializers
from test_timer.models import Players


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'
        # fields = ('id', 'user_name', 'user_number', 'user_time_start','user_time_end', 'uid', 'rid')