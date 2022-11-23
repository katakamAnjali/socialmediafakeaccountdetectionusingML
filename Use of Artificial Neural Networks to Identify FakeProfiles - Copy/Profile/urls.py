from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path("Admin.html", views.Admin, name="Admin"),
	       path("AdminLogin", views.AdminLogin, name="AdminLogin"),
	       path("GenerateModel", views.GenerateModel, name="GenerateModel"),
           path("Gradient", views.Gradient, name="Gradient"),
		   path("Random", views.Random, name="Random"),
	       path("ViewTrain", views.ViewTrain, name="ViewTrain"),
	       path("User.html", views.User, name="User"),
	       path("UserCheck", views.UserCheck, name="UserCheck"),
]
