from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This commands help to insert category data"

    def handle(self, *args: Any, **options: Any):
        #delete existing categories
        Category.objects.all().delete()

        categories = ['Sports', 'Science', 'Technology', 'Environment', 'Art']
        
        for category in categories:
            Category.objects.create(name = category)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))