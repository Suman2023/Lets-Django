from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from .models import Note


#  we are using this to make our objects that returns from the table to json compatible
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'  # we can do like [ 'id' 'title' blah blah] but __all__ takes all the fields