from django.shortcuts import render

# Copy this to create a new view
# def Index(request):
#     params={}
#     return render(request,"projects/index.html",params)

def Index(request):
    
    return render(request,"projects/index.html")