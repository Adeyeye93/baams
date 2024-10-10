from django.shortcuts import render, redirect
from .models import TrashRequest
from django.contrib.auth.decorators import login_required
from .forms import TrashRequestForm, FundRequestForm

def home(req):
    return render(req, 'recycling/index.html')

@login_required
def make_trash_request(request):
    user = request.user
    trash_requests = TrashRequest.objects.filter(user=user)
    all_trash = TrashRequest.objects.all()
    total_requests = {
        'Nylon': trash_requests.filter(trash_type='Nylon').count(),
        'Bottle': trash_requests.filter(trash_type='Bottle').count(),
        'Plastic': trash_requests.filter(trash_type='Plastic').count(),
    }
    total_points = sum(trash_request.points for trash_request in trash_requests if trash_request.points is not None)
    total_weight = sum(trash_request.weight for trash_request in trash_requests if trash_request.weight is not None)
    fund = sum(trash_request.total_fund for trash_request in trash_requests if trash_request.total_fund is not None)
    withdrawn = sum(trash_request.withdrawn_fund for trash_request in trash_requests if trash_request.withdrawn_fund is not None)
    total_fund = fund - withdrawn

    return render(request, 'recycling/dashboard.html', {'total_requests': total_requests, "total_points": total_points, 'total_weight': total_weight, "all_trash": trash_requests, "withdrawn": withdrawn, "total_fund": total_fund, "fund": fund})

@login_required
def request(request):
    if request.method == 'POST':
        if 'submit_trash_request' in request.POST:
            trash_form = TrashRequestForm(request.POST)
            fund_form = FundRequestForm() 

            if trash_form.is_valid():
                trash_request = trash_form.save(commit=False)
                trash_request.user = request.user
                trash_request.save()
                return redirect('dashboard')

        elif 'submit_fund_request' in request.POST:
            fund_form = FundRequestForm(request.POST)
            trash_form = TrashRequestForm() 
            if fund_form.is_valid():
                fund_request = fund_form.save(commit=False)
                fund_request.user = request.user
                fund_request.save()
                return redirect('dashboard')
    else:
        trash_form = TrashRequestForm()
        fund_form = FundRequestForm()

    user = request.user
    trash_requests = TrashRequest.objects.filter(user=user)
    all_trash = TrashRequest.objects.all()
    total_requests = {
        'Nylon': trash_requests.filter(trash_type='Nylon').count(),
        'Bottle': trash_requests.filter(trash_type='Bottle').count(),
        'Plastic': trash_requests.filter(trash_type='Plastic').count(),
    }
    total_points = sum(trash_request.points for trash_request in trash_requests if trash_request.points is not None)
    total_weight = sum(trash_request.weight for trash_request in trash_requests if trash_request.weight is not None)
    fund = sum(trash_request.total_fund for trash_request in trash_requests if trash_request.total_fund is not None)
    withdrawn = sum(trash_request.withdrawn_fund for trash_request in trash_requests if trash_request.withdrawn_fund is not None)
    total_fund = fund - withdrawn

    return render(request, 'recycling/request.html', {'trash_form': trash_form,
        'fund_form': fund_form, 'total_requests': total_requests, "total_points": total_points, 'total_weight': total_weight, "all_trash": trash_requests, "withdrawn": withdrawn, "total_fund": total_fund, "fund": fund})

def impact(req):
    
    return render(req, 'recycling/blog_list.html')


def about(req):
   
    return render(req, 'recycling/about.html')

def media(req):
   
    return render(req, 'recycling/product.html')

def faq(req):
    
    return render(req, 'recycling/contact.html')

# views.py


def user_dashboard(request):
    if request.user.is_authenticated:
        trash_requests = TrashRequest.objects.all()
        return render(request, 'recycling/dash.html', {'trash_requests': trash_requests})
    else:
        return redirect('Recycles')
