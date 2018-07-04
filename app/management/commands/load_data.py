import json

import datetime
from django.core.management import BaseCommand
from app.models import *

__author__ = 'Thonny Cleuton'


class Command(BaseCommand):

    def handle(self, **options):
        cont = 0
        dump_data = open('app/fixtures/db.json', 'r')
        dados = json.load(dump_data)

        for item in dados['items']:
            try:
                artist = Artist.objects.get_or_create(
                    name=item['album']['artists'][0]['name'],
                    since=datetime.datetime.today(),
                )[0]
                genre = item['album']['genres'][0] if item['album']['genres'] else 'rock'
                label = Label.objects.get_or_create(name=item['album']['label'])
                album = Album.objects.get_or_create(
                    artist=artist,
                    title=item['album']['name'],
                    label=label[0],
                    genre=Genre.objects.get_or_create(name=genre)[0],
                    year=item['album']['release_date'],
                )
                for track in item['album']['tracks']['items']:
                    Track.objects.get_or_create(
                        number=track['track_number'],
                        album=album[0],
                        name=track['name'],
                        length=datetime.timedelta(0, (track['duration_ms']/60)))
            except Exception as e:
                print(e)
