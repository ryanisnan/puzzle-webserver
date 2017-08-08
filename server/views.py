from .models import Puzzle
from django.core.views.generic import View
from django.http import HttpResponse
from django.utils.timezone import now


class LatestPuzzleAPIView(View):
    def get(self, request, *args, **kwargs):
        latest_puzzle = Puzzle.objects.all().exclude(released_at__gte=now()).order_by('-released_at').first()
        return HttpResponse(latest_puzzle.puzzle)
