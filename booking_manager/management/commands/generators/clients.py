import random

from account.models.client import Client

from .utils import fake

def generate_clients(users):

    clients_count = Client.objects.count()
    clients_to_create = max(0, 80 - clients_count)

    client_statuses = ['new', 'regular', 'vip']

    clients = []

    for i in range(clients_to_create):
        client = Client(
            user=users[i],
            name=fake.name(),
            phone=fake.unique.numerify(text='###########'),
            status=random.choice(client_statuses),
        )

        clients.append(client)

    Client.objects.bulk_create(clients)

    return clients