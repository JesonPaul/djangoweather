from django.shortcuts import render

def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=11237&distance=5&API_KEY=92B4B806-F9FE-4866-8B7D-0C130D8EC9AA")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."

	return render (request, 'home.html', {'api': api})

def about(request):
	return render (request, 'about.html', {})
