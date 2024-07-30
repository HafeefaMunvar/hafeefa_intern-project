from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import os

# Create your views here.
#     return HttpResponse("Tkinter application started.")
    


def runApp(request):
    # path = r'C:\Users\HP\Downloads\Face_recognition_based_attendance_system-master\main.py'
    path = r"Scripts\main.py"
    
    if not os.path.exists(path):
        return HttpResponse(f"Error: File not found at {path}")
    try:
        subprocess.Popen(['python', path])
        return HttpResponse("<h1>Tkinker App Running</h1>")
    except Exception as e:
        return HttpResponse(f"Error: {e}")