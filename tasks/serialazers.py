from rest_framework import serializers

from tasks.models import Task


class TaskListSerialazer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["id", "user", "title", "text", "status", "isImportant", "created", "start", "end", "categories"]


class TaskDetailSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskCreateSerialazer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    text = serializers.StringRelatedField(required=False)
    start = serializers.DateTimeField(
        required=False,
        input_formats=["%d.%m.%Y %H:%M", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"],
    )
    end = serializers.DateTimeField(
        required=False,
        input_formats=["%d.%m.%Y %H:%M", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d", ""],
    )

    class Meta:
        model = Task
        exclude = []
