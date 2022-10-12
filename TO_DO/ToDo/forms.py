from socket import fromshare
from tkinter import Widget
from django import forms

class ToDoForm(forms.Form):
    text = forms.CharField(max_length=40),
    Widget = forms.TextInput()
