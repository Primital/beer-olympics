from django.shortcuts import render
from django.views.generic.base import TemplateView


class GamesView(TemplateView):
    template_name = "games.html"
    #  queryset = PlayerMatch.objects.select_related(
    #          'player_one',
    #          'player_two'
    #      ).order_by("-match_date")

    # def get_queryset(self):
    #     return self.queryset

    # def get_context_data(self, **kwargs):
    #     qs = self.get_queryset()
    #     context = super().get_context_data(**kwargs)

    #     context['matches'] = qs[:50]
    #     context["match_header_text"] = "Latest matches"
    #     return context
