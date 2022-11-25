from dataclasses import field
import imp
from pyexpat import model
from django.forms import ModelForm
from .models import Room



# all data dispkay in this from database
class RoomForm(ModelForm):
    class Meta:
        model =Room
        fields = '__all__'