from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Start a new habit",
    "february": "Show kindness daily",
    "march": "Move your body",
    "april": "Learn something new",
    "may": "Help someone out",
    "june": "Go outside more",
    "july": "Try a new hobby",
    "august": "Read every day",
    "september": "Stay organized",
    "october": "Face a fear",
    "november": "Practice gratitude",
    "december": "Reflect and relax",
}

# Create your views here.

def month_list(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months" : months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_month =  months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month" : month.capitalize(),
            "challenge" : challenge_text})
    except:
        return HttpResponseNotFound("<h1>Month Not Supported</h1>")
