from django.core.management.base import BaseCommand
from faker import Faker
from django.utils import timezone
from hangarinorg.models import Note, Subtask, Task, Category, Priority


class Command(BaseCommand):
    help = 'Create initial data for testing'

    def handle(self, *args, **kwargs):
        self.create_tasks(10)
        self.create_notes(10)
        self.create_subtasks(10)

    # Create tasks
    def create_tasks(self, count):
        fake = Faker()
        for _ in range(count):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),  # fixed `faker` -> `fake`
                status=fake.random_element(elements=("Pending", "In Progress", "Completed")),
                category=Category.objects.order_by('?').first(),
                priority=Priority.objects.order_by('?').first()
            )
        self.stdout.write(self.style.SUCCESS('Successfully created tasks initial data.'))

    # Create notes
    def create_notes(self, count):
        fake = Faker()
        for _ in range(count):
            Note.objects.create(
                task=Task.objects.order_by('?').first(),
                content=fake.paragraph(nb_sentences=3)
            )
        self.stdout.write(self.style.SUCCESS('Successfully created notes initial data.'))

    # Create subtasks
    def create_subtasks(self, count):  # fixed function name `create_substask` -> `create_subtasks`
        fake = Faker()
        for _ in range(count):
            Subtask.objects.create(
                parent_task=Task.objects.order_by('?').first(),
                title=fake.sentence(nb_words=5),
                status=fake.random_element(elements=("Pending", "In Progress", "Completed"))
            )
        self.stdout.write(self.style.SUCCESS('Successfully created subtasks initial data.'))
