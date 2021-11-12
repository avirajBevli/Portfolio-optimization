from django.shortcuts import render
from .models import Tweet
from .utilities_sentiment import calculate_delta_sentiment
from .utilities_portfolio_optimization import calculate_portfolio

from asset.models import Asset

# Create your views here.

def index(request):
    return render(request, "tweet/index.html", {'message': "Click here to calculate sentiments."})


def sentiment_result(request):
    context = {
    	#'delta_sentiment': calculate_delta_sentiment(),
    }
    return render(request, "tweet/sentiment_result.html", context)


def input_portfolio(request):
    #print(request.POST)
    print("___________________________HIII_____________________")
    all_assets = Asset.objects.all()
    print("=======================All assets: ", all_assets)
    context = {
    	#'portfolio_wts': calculate_portfolio(), # this will be used in the view for result_portfolio 
        'assets':all_assets,
    }
    return render(request, "tweet/input_portfolio.html", context)


def result_portfolio(request):
    data = request.POST.getlist('data')
    #print("#########################", data, "######################")
    portfolio, exp_return, exp_risk = calculate_portfolio(data)
    context = {
        'portfolio': portfolio,
        'exp_return': exp_return,
        'exp_risk': exp_risk,   
    }
    return render(request, "tweet/result_portfolio.html", context)
