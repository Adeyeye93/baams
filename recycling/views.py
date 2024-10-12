from django.shortcuts import render, redirect
from .models import TrashRequest, FundRequest
from django.contrib.auth.decorators import login_required
from .forms import TrashRequestForm, FundRequestForm
from django.contrib import messages

def home(req):
    return render(req, 'recycling/index.html')

@login_required
def make_trash_request(request):
    user = request.user
    trash_requests = TrashRequest.objects.filter(user=user)
    fund_requests = FundRequest.objects.filter(user=user)

    # Combine TrashRequest and FundRequest into all_request (for rendering purposes)
    all_requests = list(trash_requests) + list(fund_requests)

    # Calculate total requests by trash type
    total_requests = {
        'Nylon': trash_requests.filter(trash_type='Nylon').count(),
        'Bottle': trash_requests.filter(trash_type='Bottle').count(),
        'Plastic': trash_requests.filter(trash_type='Plastic').count(),
    }

    # Calculate total earned from TrashRequest
    total_earned = sum(trash_request.earned for trash_request in trash_requests if trash_request.earned is not None)


    total_weight = sum(trash_request.weight for trash_request in trash_requests if trash_request.weight is not None)

    # Calculate total withdrawn from FundRequest
    withdrawn_fund = sum(fund_request.amount for fund_request in fund_requests if fund_request.amount is not None)

    # Calculate available funds (total earned minus withdrawn funds)
    available_fund = total_earned - withdrawn_fund

    # Update the user model with the calculated values
    user.total_fund = total_earned
    user.withdrawn_fund = withdrawn_fund
    user.save()
   
    return render(request, 'recycling/dashboard.html', {
        'total_requests': total_requests,
        'total_weight': total_weight,
        'total_earned': total_earned,
        'withdrawn_fund': withdrawn_fund,
        'available_fund': available_fund,
        'all_requests': all_requests,  # Combine TrashRequest and FundRequest
    })

@login_required
def request(request):
    if 'submit_trash_request' in request.POST:
        trash_form = TrashRequestForm(request.POST)
        fund_form = FundRequestForm()

        if trash_form.is_valid():   
            trash_request = trash_form.save(commit=False)
            trash_request.user = request.user
            trash_request.save()
            messages.success(request, "Your waste request as been sent.")
            return redirect('dashboard')
        else:
             messages.error(request, 'There was an error in your form.')

    elif 'submit_fund_request' in request.POST:
        fund_form = FundRequestForm(request.POST)
        trash_form = TrashRequestForm()
        if fund_form.is_valid():
            fund_request = fund_form.save(commit=False)
            fund_request.user = request.user
            fund_request.save()
            messages.success(request, "Your withdrawal request as been sent.")
            return redirect('dashboard')
        else:
             messages.error(request, 'There was an error in your form.')
    else:
        trash_form = TrashRequestForm()
        fund_form = FundRequestForm()

    # Get user and related data
    user = request.user
    trash_requests = TrashRequest.objects.filter(user=user)
    fund_requests = FundRequest.objects.filter(user=user)

    # Combine TrashRequest and FundRequest into all_request (for rendering purposes)
    all_requests = list(trash_requests) + list(fund_requests)

    # Calculate total requests by trash type
    total_requests = {
        'Nylon': trash_requests.filter(trash_type='Nylon').count(),
        'Bottle': trash_requests.filter(trash_type='Bottle').count(),
        'Plastic': trash_requests.filter(trash_type='Plastic').count(),
    }

    # Calculate total earned from TrashRequest
    total_earned = sum(trash_request.earned for trash_request in trash_requests if trash_request.earned is not None)

    total_weight = sum(trash_request.weight for trash_request in trash_requests if trash_request.weight is not None)

    # Calculate total withdrawn from FundRequest
    withdrawn_fund = sum(fund_request.amount for fund_request in fund_requests if fund_request.amount is not None)

    # Calculate available funds (total earned minus withdrawn funds)
    available_fund = total_earned - withdrawn_fund

    # Update the user model with the calculated values
    user.total_fund = total_earned
    user.withdrawn_fund = withdrawn_fund
    user.save()

    # Render the template with all data
    return render(request, 'recycling/request.html', {
        'trash_form': trash_form,
        'fund_form': fund_form,
        'total_weight': total_weight,
        'total_requests': total_requests,
        'total_earned': total_earned,
        'withdrawn_fund': withdrawn_fund,
        'available_fund': available_fund,
        'all_requests': all_requests,  # Combine TrashRequest and FundRequest
    })


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
