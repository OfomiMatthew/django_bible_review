from django.shortcuts import render
import requests 
import random


def fetchData(request):
    url = "https://beta.ourmanna.com/api/v1/get/?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        verse = data['verse']['details']['text']
        reference = data['verse']['details']['reference']
        version = data['verse']['details']['version']
        context = {'verse':verse,'reference':reference,'version':version}
        
    else:
        context = {'error': 'Failed to retrieve the verse of the day.'}
    return render(request, 'verse.html', context)
        
        
    
    

    
    
  




  


 

