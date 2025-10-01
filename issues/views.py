from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from datetime import date, timedelta
from dateutil import parser

from .models import ISSUE
from .forms import OpenISSUE,UpdateISSUE,EditISSUE

import operator

@login_required
def issues(request):
    today = date.today()
    first = today.replace(day=1)
    to = first - timedelta(days=1)
    fromdate = to.replace(day=1)
    todate = today
    
    if request.method == 'POST': 
        fromdate = parser.parse(request.POST.get('fromdate'))
        todate = parser.parse(request.POST.get('todate'))

    #Issues
    qs =ISSUE.objects.filter(date__gte=fromdate, date__lte=todate).order_by('issue','-date').distinct('issue')
    check_date =ISSUE.objects.filter(date__gte=fromdate, date__lte=todate).order_by('issue','date').distinct('issue')
    
    sorted_qs = sorted(qs, key=operator.attrgetter('machine')) 
    sorted_date = sorted(check_date, key=operator.attrgetter('machine')) 

    issue_days =[]
    date_opens = []
    for a in sorted_date :
        date_open = a.date
        today = date.today()
        issue_day = today - date_open
        issue_days.append(issue_day.days)
        date_opens.append(date_open)
    issue = zip(sorted_qs,date_opens,issue_days)

    context = {'fromdate':fromdate , 'todate':todate, 'issue':issue }
    return render(request, 'issues/issues.html',context)

@login_required
def member_issue(request,member):

    issues = ISSUE.objects.filter(executor=member).order_by('issue','-registered_at').distinct('issue') 
    context = {'issues': issues }
    return render(request, 'issues/member_issue.html', context)

@login_required
def open_issue(request):

    if request.method == 'POST':
        form = OpenISSUE(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.executor = request.user
            print (request.user)
            issue.status = 'open'
            issue.save()
            return HttpResponseRedirect(reverse('member_issue',kwargs={'member':request.user})) 
    else:
        form = OpenISSUE()
    
    context = {'form': form}
    return render(request, 'issues/open_issue.html', context)

@login_required
def update_issue(request,issue):
 
    f_issue = ISSUE.objects.filter(issue=issue).order_by('date')
    last = ISSUE.objects.filter(issue=issue).last()

    try:
        last.date = date.today()

    except:
        last = ISSUE.objects.filter(issue=issue).last()

    if request.method == 'POST': 
        form = UpdateISSUE(request.POST)
        if form.is_valid():

            update_issue = form.save(commit=False)
            update_issue.issue = last.issue
            update_issue.problem = last.problem
            update_issue.customer = last.customer
            update_issue.serial_no = last.serial_no
            update_issue.machine = last.machine
            update_issue.model = last.model
            update_issue.executor = request.user
            update_issue.save()
            return HttpResponseRedirect(reverse('update_issue',kwargs={'issue':update_issue.issue}))
    else:
        form = UpdateISSUE(instance=last)
        context = {'last': last }
    
    context = {'form': form ,'issues': f_issue,'last': last }
    return render(request, 'issues/update_issue.html', context)

@login_required
def edit_issue(request, id):
    try:
        myissue = ISSUE.objects.get(id=id)
    except ISSUE.DoesNotExist:
        myissue = None    
    issue = myissue.issue
    context = {'myissue': myissue}
    if request.method == 'POST': 
        form = EditISSUE(request.POST,instance=myissue)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(reverse('update_issue',kwargs={'issue':issue}))
    else:
        form = EditISSUE(instance=myissue)
    context = {'form': form}
    return render(request, 'issues/edit_issue.html', context)

@login_required
def delete_issue(request, id):
    issue = ISSUE.objects.get(id=id) 
    issue.delete()
   # issue = issue.issue
    return HttpResponseRedirect(reverse('update_issue',kwargs={'issue':issue.issue}))

@login_required
def issue(request,issue):
    q_issue = ISSUE.objects.filter(issue=issue).order_by('date')
    context = {'q_issue': q_issue, 'issue': issue }
    return render(request, 'issues/issue.html', context)