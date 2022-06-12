from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request,'index.html')

def some_function(request):
    if request.method == "GET":
        print(request.GET)
    if request.method == "POST":
        print(request.POST)

def re(request):
    if request.method == "POST":
        val_from_field_one = request.POST['name']
        val_from_field_two = request.POST['location']
        val_from_field_three = request.POST['Fave']
        val_from_field_four = request.POST['commm']
        context = {
            "name": val_from_field_one,
            "location": val_from_field_two,
            "Fave":val_from_field_three,
            "commm":val_from_field_four
        }
    return render(request,'index2.html',context)