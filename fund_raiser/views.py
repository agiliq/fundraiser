from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from books.models import Book, Beneficiary
from fund_raiser.models import Campaign
from fund_raiser.forms import CampaignForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def pbadmin_index(request):
    books = Book.objects.all()
    return render_to_response('pbadmin_index.html', {"books": books})


def approve(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user:
        user.beneficiary.approved = True
        user.beneficiary.save()
        return HttpResponseRedirect(reverse('unapproved'))
    return render_to_response('unapproved_users.html')


def campaigns(request):
    return render_to_response('campaigns.html', context_instance=RequestContext(request))

@login_required
def create_a_campaign(request):
    form = CampaignForm()
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            beneficiary =  Beneficiary.objects.get(beneficiary_user=request.user)
            cam_obj = Campaign.objects.create(beneficiary=beneficiary,
                                     campaign_name=request.POST['campaign_name'],
                                     target_amount=request.POST['target_amount'],
                                     cause=request.POST['cause'])
            if request.POST.getlist('books'):
                for m2m in request.POST.getlist('books'):
                    cam_obj.books.add(m2m)
            return HttpResponseRedirect(reverse('list_of_campaigns'))

    return render_to_response('create_a_campaign.html', {'form':form, 'errors':dict(form.errors.viewitems())}, context_instance=RequestContext(request))
