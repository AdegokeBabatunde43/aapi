from rest_framework import serializers
from todos.models import Todos

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = "__all__"