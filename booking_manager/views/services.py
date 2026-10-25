from django.shortcuts import render

def services(request):
    services = [
        {"id": 1, "name": "Haircut", "duration": 60, "price": 30, "category": "Hair"},
        {"id": 2, "name": "Beard Trim", "duration": 30, "price": 15, "category": "Hair"},
        {"id": 3, "name": "Manicure", "duration": 45, "price": 25, "category": "Nails"},
        {"id": 4, "name": "Massage", "duration": 90, "price": 50, "category": "Wellness"},
        {"id": 5, "name": "Consultation", "duration": 30, "price": 20, "category": "Other"}
    ]

    return render(request,'services.html',context={'services':services})