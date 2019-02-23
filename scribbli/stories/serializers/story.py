from rest_framework.serializers import ModelSerializer

from scribbli.stories.models import Story


class StorySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'
