from django import forms
from todolist.models import TaskList

class TaskForm(forms.ModelForm):

    class Meta:
        model = TaskList
        fields = ['task', 'done']