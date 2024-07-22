from django.shortcuts import render,get_object_or_404,redirect
from BibleReviewApp.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
  searchTerm = request.GET.get('searchTerm')
  if searchTerm:
    characters = BibleCharacter.objects.filter(character__icontains=searchTerm)
  else:
    characters = BibleCharacter.objects.all()   
  return render(request, 'home.html', {'searchTerm':searchTerm,'characters':characters})
  

def detail(request,bible_id):
  bible = get_object_or_404(BibleCharacter,pk=bible_id)
  reviews = Review.objects.filter(character = bible)
  return render(request,'detail.html',{'bible':bible,'reviews':reviews})

@login_required
def createReview(request,bible_id):
  bible = get_object_or_404(BibleCharacter,pk=bible_id)
  if request.method == 'GET':
    return render(request,'createreview.html',{'form':ReviewForm(),'bible':bible})
  else:
    try:
      form = ReviewForm(request.POST)
      newReview = form.save(commit=False)
      newReview.user = request.user
      newReview.character = bible
      newReview.save()
      return redirect('detail',newReview.character.id)
    except ValueError:
      return render(request,'createreview.html',{'form':ReviewForm(),'error':'bad data passed'})
      
@login_required
def updateReview(request,review_id):
  review = get_object_or_404(Review,pk=review_id,user=request.user)
  if request.method == 'GET':
    form = ReviewForm(instance=review)
    return render(request,'updatereview.html',{'review':review,'form':form})
  else:
    try:
      form = ReviewForm(request.POST,instance=review)
      form.save()
      return redirect('detail',review.character.id)
    except ValueError:
      return render(request,'updatereview.html',{'review':review})
 
@login_required   
def deleteReview(request,review_id):
  review = get_object_or_404(Review,pk=review_id,user=request.user)
  if request.method == 'POST':
    review.delete()
    messages.info(request,f'Review: {review.text} deleted successfully')
    return redirect('detail')
  return render(request,'delete.html',{'obj':review})
    
  
         
  
  








#  Sign up for newsletter section 

# def signup(request):
#   name = request.GET.get('name')
#   email = request.GET.get('email')
#   return render(request,'signup.html', {'email':email, 'name':name})
  
