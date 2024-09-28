from django.shortcuts import render
import calendar
from datetime import datetime, timedelta
from django.core.cache import cache
import requests
from .config import api_key
from .forms import SearchForm
from django.http import HttpResponse

# Create your views here.


def index(request, year=None, month=None):

    form = SearchForm()
    if not year or not month:
        today = datetime.today()
        year = today.year
        month = today.month

    cache_key = "events"
    events = cache.get(cache_key)

    if not events:
        response = requests.get(
            url="https://rekrutacja.teamwsuws.pl/events/", headers={"api-key": api_key}
        )
        events = response.json()

        for event in events:
            event["start_time"] = datetime.strptime(
                event["start_time"], "%Y-%m-%dT%H:%M:%S"
            )

        cache.set(cache_key, events)

    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)

    return render(
        request,
        "calendar/index.html",
        {
            "events": events,
            "year": year,
            "month": month,
            "prev_month": month - 1 if month > 1 else 12,
            "prev_year": year - 1 if month == 1 else year,
            "next_month": month + 1 if month < 12 else 1,
            "next_year": year + 1 if month == 12 else year,
            "month_days": month_days,
            "month_name": calendar.month_name[month],
            "form": form,
        },
    )


def event(request, event_id):
    cache_key = f"event-{event_id}"
    event = cache.get(cache_key)
    if not event:
        response = requests.get(
            url=f"https://rekrutacja.teamwsuws.pl/events/{event_id}/",
            headers={"api-key": api_key},
        )
        event = response.json()
        cache.set(cache_key, event)
    event["start_time"] = datetime.strptime(event["start_time"], "%Y-%m-%dT%H:%M:%S")
    event["end_time"] = event["start_time"] + timedelta(hours=event["duration"])

    return render(request, "calendar/event.html", {"event": event})


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        search = None
        if form.is_valid():
            search = form.cleaned_data["search"]
            response = requests.get(
                url=f"https://rekrutacja.teamwsuws.pl/events/filter/?tag={search}",
                headers={"api-key": api_key},
            )
            events = response.json()
            return render(
                request,
                "calendar/search.html",
                {
                    "events": events,
                },
            )
    else:
        return HttpResponse("Invalid form")
