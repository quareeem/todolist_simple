from datetime import datetime
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import TodoModel
import pytz


class TodoSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    due_date = serializers.DateTimeField(format="%d.%m.%Y - %H:%M:%S")
    is_overdue = serializers.SerializerMethodField()

    def get_is_overdue(self, instance):
        tz = pytz.timezone('UTC')
        if instance.due_date > datetime.now(tz=tz):
            return False
        return True

    class Meta:
        model = TodoModel
        fields = ('user', 'id', 'title', 'description', 'due_date', 'is_completed', 'is_overdue')
