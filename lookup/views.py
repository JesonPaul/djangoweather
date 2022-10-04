from django.shortcuts import render

def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=11237&distance=5&API_KEY=92B4B806-F9FE-4866-8B7D-0C130D8EC9AA")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."

	if api[0]['Category']['Name'] == "Good":
		category_description = "(0 -50) Air quality is considered satisfactory, and air pollution poses little or no risk"
		category_color = "good"

	elif api[0]['Category']['Name'] == "Moderate": 
		category_description = "(51 -100) If you are unusually sensitive to ozone, consider reducing your activity level or shorten the amount of time you are active outdoors."
		category_color = "moderate"

	elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
		category_description = "(101 -150) Although general public is not likely to be affected at thi AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas person with heart and lung disease are at greater risk from the presence of particles in air."
		category_color = "Unhealthy for Sensitive Groups"

	elif api[0]['Category']['Name'] == "Unhealthy":
		category_description = "(151 -200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
		category_color = "unhealthy"

	elif api[0]['Category']['Name'] == "Very unhealthy":
		category_description = "(201 -300) Health Alert: everyone may experience more serious health effects."
		category_color = "veryunhealthy"

	elif api[0]['Category']['Name'] == "Hazardous":
		category_description = "(301 -500) Health warnings of emergency conditions. The entire population is more likely to be affected. "
		category_color = "hazardous"


	return render (request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

def about(request):
	return render (request, 'about.html', {})
