from django.shortcuts import render,get_object_or_404

from BibleReviewApp.models import BibleCharacter




def home(request):
 
  searchTerm = request.GET.get('searchTerm')
  
  if searchTerm:
    characters = BibleCharacter.objects.filter(character__icontains=searchTerm)
  else:
    characters = BibleCharacter.objects.all()
    
    
    
  return render(request, 'home.html', {'searchTerm':searchTerm,'characters':characters})
  

def detail(request,bible_id):
  bible = get_object_or_404(BibleCharacter,pk=bible_id)
  return render(request,'detail.html',{'bible':bible})
  
  








#  Sign up for newsletter section 

# def signup(request):
#   name = request.GET.get('name')
#   email = request.GET.get('email')
#   return render(request,'signup.html', {'email':email, 'name':name})
  
