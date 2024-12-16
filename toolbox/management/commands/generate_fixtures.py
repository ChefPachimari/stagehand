# your_app/management/commands/generate_fixtures.py
import json
from django.core.management.base import BaseCommand
from toolbox.models import Numbers
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Generate fixture data for Numbers model'

    def handle(self, *args, **kwargs):
        # Generate new data
        data = []
        for i in range(1, 101):
            data.append({
                "model": "toolbox.numbers",
                "pk": i,
                "fields": {
                    "number": i,
                    "request_ct": 0
                }
            })

        # Write data to a JSON file
        fixtures_dir = os.path.join(settings.BASE_DIR, 'toolbox', 'fixtures')
        os.makedirs(fixtures_dir, exist_ok=True)
        file_path = os.path.join(fixtures_dir, 'numbers_fixture.json')

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

        self.stdout.write(self.style.SUCCESS('Successfully generated fixture data to numbers_fixture.json'))