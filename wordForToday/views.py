from django.shortcuts import render
# import requests 
import random


def fetchData(request):
    # api_url = 'https://bible-api.com/john+3:16'
    # Make a GET request to the API
    # response = requests.get(api_url)
    # Parse the JSON response
    # verse_data = response.json()
    # Extract the verse text
    # verse_text = verse_data['text']
    # return render(request, 'api.html', {'verse_text': verse_text})

    bible_verses = [
        {"scripture": "John 3:16", "text": "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life."},
        {"scripture": "Matthew 6:33", "text": "But seek first his kingdom and his righteousness, and all these things will be given to you as well."},
        {"scripture": "Philippians 4:13", "text": "I can do all this through him who gives me strength."},
        # Add more verses as needed
    ]
    
    random_verse = random.choice(bible_verses)
    
    return render(request, 'api.html', {'random_verse': random_verse})

    
    
  




  


 

