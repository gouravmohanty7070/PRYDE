from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from .models import ForumComment
from .utils import process_comment
import requests
import random
import openai

openai.api_key = "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"

# Create your views here.
def forumPage(request):
    if request.user.is_authenticated:
        context = {
            "comments": ForumComment.objects.all()
        }
        return render(request, 'forums/forum.html', context=context)
    else:
        return redirect('loginPage')

def addComment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            comment = request.POST['comment']
            if(len(comment)):
                obj = ForumComment(comment=process_comment(comment), user=request.user)
                obj.save()
            return redirect("forumPage")
        else:
            return redirect("forumPage")
    else:
        return redirect('loginPage')
    
def knowMore(request):
    return render(request, 'KnowMore/knowmore.html')

def chatBot(request):
    return render(request, 'chatbot/chatbot.html')

# def videoCall(request):
#     return render(request, 'VideoCall/videocall.html')

def get_chatbot_response(user_input):
    prompt = f"User: {user_input}\nPryde Bot:"

    # Call OpenAI's GPT model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

# Define Django view to handle conversation requests
@csrf_exempt
def conversation(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'chatbot/conversation.html')
    if request.method == 'POST':
        print(request.POST)
        user_input =  request.body.decode('UTF-8')
        # Code to get chatbot response using OpenAI's GPT goes here
        #response = "This is the response from the chatbot.  "+user_input

        response = get_chatbot_response(user_input)

        return JsonResponse({'data': response})
    else:
        return HttpResponse(status=405)

def blogPage(request):
    if request.user.is_authenticated:
        response = requests.get('https://blogsug.azurewebsites.net/suggest_blogs?topic=lgbtq')
        response = random.sample(response.json()['suggestions'], 6)
        context = {
            'articles': response,
        }
        return render(request, 'blogs/blog.html', context=context)
    else:
        return redirect('loginPage')

def youMatter(request):
    if request.user.is_authenticated:
        emotion = None
        movie_url = None
        song_url = None
        if 'emotion' in request.GET:
            emotion = request.GET['emotion']
            song_url = requests.get('https://musicsuggestion.azurewebsites.net/'+emotion).json()[0]['url']
            movie_url = requests.get('https://netflixrecommendation.azurewebsites.net/random_movie?sentiment='+emotion).json()[0]['poster_url']
        context = {
            'emotion': emotion,
            'song_url': song_url,
            'movie_url': movie_url,
        }
        return render(request, 'selfLove/youMatter.html', context=context)
    else:
        return redirect('loginPage')