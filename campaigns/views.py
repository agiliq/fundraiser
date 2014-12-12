import decimal

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Q

from people.models import Person
from campaigns.models import (
    Campaign,
    Category,
    Reward,
    FundDistribution,
    TeamMember
)
from campaigns.forms import CampaignForm


def get_extra_data(post):
    fdd = [k for k in post.keys() if k.startswith('fund-dist-d')]
    fda = [k for k in post.keys() if k.startswith('fund-dist-a')]
    fdd.sort()
    fda.sort()
    tup_fd = [(post[fdd[i]],
               post[fda[i]]) for i in range(len(fda))]
    rew = [k for k in post.keys() if k.startswith('reward')]
    rew.sort()
    tup_rew = [post[rew[i]] for i in range(len(rew))]
    name = [k for k in post.keys() if k.startswith('name')]
    role = [k for k in post.keys() if k.startswith('role')]
    short_desc = [k for k in post.keys()
                  if k.startswith('short-bio')]
    fb_url = [k for k in post.keys() if k.startswith('fb')]
    name.sort()
    role.sort()
    short_desc.sort()
    fb_url.sort()
    tup_tm = [(post[name[i]],
               post[role[i]],
               post[short_desc[i]],
               post[fb_url[i]])
              for i in range(len(name))]
    return (tup_fd, tup_rew, tup_tm)


@login_required
def create_a_campaign(request):
    form = CampaignForm()
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        extra_data = get_extra_data(request.POST)
        tup_fd = extra_data[0]
        tup_rew = extra_data[1]
        tup_tm = extra_data[2]
        if form.is_valid():
            person = Person.objects.get(user=request.user)
            cam_obj = form.save(commit=False)
            cam_obj.person = person
            cam_obj.save()
            for each in tup_rew:
                if each:
                    reward = Reward(title=each)
                    reward.save()
                    cam_obj.rewards.add(reward)
            for each in tup_fd:
                if each[0] and each[1]:
                    fd = FundDistribution(usage=each[0], allocation=each[1])
                    fd.save()
                    cam_obj.fund_distribution.add(fd)
            for each in tup_tm:
                if each[0] and each[1] and each[2] and each[3]:
                    tm = TeamMember(name=each[0],
                                    role=each[1],
                                    short_description=each[2],
                                    fb_url=each[3],
                                    campaign=cam_obj)
                    tm.save()

            return HttpResponseRedirect(
                reverse('campaigns:list_of_campaigns'))
        else:
            form = CampaignForm()

    return render_to_response('campaigns/create_a_campaign.html',
                              {'form': form,
                               'errors': dict(form.errors.viewitems())},
                              context_instance=RequestContext(request))


class CampaignDetail(generic.DetailView):
    model = Campaign
    template_name = 'campaigns/campaign_detail.html'
    context_object_name = 'campaign'


class CampaignsListView(generic.ListView):
    template_name = 'campaigns/campaigns.html'
    context_object_name = 'campaign_list'
    paginate_by = 10

    def get_queryset(self):
        return Campaign.objects.filter(is_approved=True)

    def get_context_data(self, **kwargs):
        search_results = None
        if self.request.GET:
            search_results = Campaign.objects.filter(
                Q(campaign_name__icontains=self.request.GET['q']))
        context = super(CampaignsListView, self).get_context_data(**kwargs)
        context['search_results'] = search_results
        return context


class CampaignUpdate(generic.UpdateView):
    model = Campaign
    template_name_suffix = '_update_form'
    form_class = CampaignForm

    def get_success_url(self):
        return reverse("campaigns:campaign_detail", args=[self.object.slug])

    def post(self, request, *args, **kwargs):
        form = CampaignForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            print get_extra_data(form.data)
        return super(CampaignUpdate, self).post(request, *args, **kwargs)


class MyCampaigns(generic.ListView):
    template_name = 'campaigns/my_campaigns.html'
    context_object_name = 'my_campaigns_list'
    paginate_by = 10

    def get_queryset(self):
        return Campaign.objects.filter(
            person__id__exact=self.kwargs['user_id'])

    def get_context_data(self, **kwargs):
        search_results = None
        if self.request.GET:
            search_results = Campaign.objects.filter(
                Q(campaign_name__icontains=self.request.GET['q']))
        context = super(MyCampaigns, self).get_context_data(**kwargs)
        context['search_results'] = search_results
        return context


def testpay(request, campaign_id):

    if request.method == 'POST':
        campaign = get_object_or_404(Campaign, id=campaign_id)
        if campaign:
            campaign.donation += decimal.Decimal(request.POST['donation'])
            campaign.save()
            return render(request, 'campaigns/campaign_detail.html',
                          {'donation': 'success', 'campaign': campaign})
    return render(request, 'campaigns/donate.html',
                  {'campaign_id': campaign_id})


class CategoryListView(generic.ListView):
    template_name = 'campaigns/categories.html'
    context_object_name = 'categories'
    paginate_by = 10

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        search_results = None
        if self.request.GET:
            search_results = Category.objects.filter(
                Q(name__icontains=self.request.GET['q']))
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['search_results'] = search_results
        return context


class CategoryDetail(generic.DetailView):
    model = Category
    template_name = 'campaigns/category_detail.html'
    context_object_name = 'category'
