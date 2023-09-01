from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView
from django.views.generic.edit import CreateView

from .models import Link, Profile


# Create your views here.
# view route for home page
class IndexView(ListView):
    model = Link
    template_name = "link_profiles/index.html"
    context_object_name = "links"
    # it would expect a default name for the html file format(modelname_list.html)
    # my default template name should be (link_list.html)


# view route for creating a link
class CreateLinkView(CreateView):
    model = Link
    fields = "__all__"
    template_name = "link_profiles/create-link.html"
    success_url = reverse_lazy("home")
    # it would expect a default name for the html file format(modelname_form.html)
    # my default template name should be (link_form.html)


# view route for updating or editing an existing link
class UpdateLinkView(UpdateView):
    model = Link
    fields = ["name", "url"]
    template_name = "link_profiles/create-link.html"
    success_url = reverse_lazy("home")
    # it shares the same form html with the CreateView
    # it would expect a default name for the html file format(modelname_form.html)
    # my default template name should be (link_form.html)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        has_object = False
        if context["object"]:
            has_object = True
        # print(has_object)
        context["has_object"] = has_object
        return context


# view route for deleting a link
class DeleteLinkView(DeleteView):
    model = Link
    success_url = reverse_lazy("home")
    # form to submit the delete item
    # expects a name of model_confirm_delete.html
    # in my case its link_confirm_delete.html


# view route for profile page
def profile(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    # query for the associated links of the said profile
    links = profile.links.all()

    return render(
        request,
        "link_profiles/profile.html",
        {
            "profile": profile,
            "links": links,
        },
    )
