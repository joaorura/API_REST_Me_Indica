from rest_framework_mongoengine import serializers

from .models import LogicQuestion


class LogicQuestionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = LogicQuestion
        fields = '__all__'
