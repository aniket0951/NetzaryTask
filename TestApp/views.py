from django.shortcuts import render, redirect
from django.http import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.contrib import messages

# Create your views here.
def OpenForm(request):
    return render(request, 'testform.html')


def GrandTotal(request):
    startdate = request.POST.get('startdate')
    enddate = request.POST.get('enddate')
    principal = request.POST.get('principal')
    interest = request.POST.get('interest')

    if principal <= '5000':
        interest = 3
    if principal > '5001':
        interest = 2

    start_date = datetime.strptime(startdate, "%Y-%m-%d")
    end_date = datetime.strptime(enddate, "%Y-%m-%d")

    year = numOfYear(end_date, start_date)
    month = numOfMonths(end_date, start_date)
    day = numOfDays(end_date, start_date)

    prinRate = Interest100sPrin(int(principal), int(interest))
    int_per_month = InterestPerMonth(prinRate, int(month))
    for_day = InterestForDays(prinRate, int(day))
    total_interest = int_per_month + for_day

    grandT = float(int(principal) + total_interest)
    grandT = round(grandT,2)

    messages.success(request, f"Grand total is : {grandT}")
    return HttpResponse(f"Grand total is : {grandT}")


def Interest100sPrin(principal, interest):
    prin = int((principal / 100) * interest)
    return prin


def InterestPerMonth(prinRate, month):
    int_per_month = int(prinRate * month)
    return int_per_month


def InterestForDays(month_rate, days):
    for_day = float((month_rate / 30) * days)
    for_day = round(for_day, 2)
    return for_day


def numOfDays(date2, date1):
    num_days = relativedelta(date2, date1).days
    return num_days


def numOfMonths(date2, date1):
    numMounth = relativedelta(date2, date1).months
    return numMounth


def numOfYear(date2, date1):
    numYear = relativedelta(date2, date1).years
    return numYear
