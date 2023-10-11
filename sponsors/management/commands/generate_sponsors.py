import random

import faker as faker
from django.core.management.base import BaseCommand

from sponsors.models import Sponsor


class Command(BaseCommand):
    help = "Generate sponsors"

    def handle(self, *args, **options):
        fake = faker.Faker()
        sponsors = [
            Sponsor(
                full_name=fake.name,
                phone=fake.phone_number(),
                amount=random.randint(1000000, 10000000),
                payment_type=Sponsor.PaymentType.card,
            )
            for _ in range(1000)
        ]
        sponsors_organizations = [
            Sponsor(
                full_name=fake.name(),
                phone=fake.phone_number(),
                amount=random.randint(1000000, 10000000),
                payment_type=Sponsor.PaymentType.card,
                is_organization=True,
                organization_name=" ".join(fake.text().split(" ")[:2]),
            )
            for _ in range(1000)
        ]
        Sponsor.objects.bulk_create(sponsors)
        Sponsor.objects.bulk_create(sponsors_organizations)
        self.stdout.write(self.style.SUCCESS("Successfully generated sponsors."))
