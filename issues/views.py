from django.shortcuts import render

def issues(request):

    return render(request, 'issues/issues.html')
