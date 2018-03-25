from django.shortcuts import render

# Create your views here.

from django.views.generic import View

from .models import CourseOrg, CityDict


class OrgView(View):
    """
    课程机构列表
    """
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        all_cities = CityDict.objects.all()
        return render(request, "org-list.html", {
            "all_orgs": all_orgs,
            "all_cities": all_cities,
            "org_nums": org_nums
        })
