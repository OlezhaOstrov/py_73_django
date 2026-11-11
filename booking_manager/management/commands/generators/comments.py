import random

from booking_manager.models.comment import Comment
from booking_manager.models.booking import Booking

from .utils import fake

def generate_comments():

    comments_count = Comment.objects.count()
    comments_to_create = max(0, 200 - comments_count)

    bookings_without_comments = list(
        Booking.objects.filter(comment__isnull=True)
    )

    comments = []

    for booking in bookings_without_comments[:comments_to_create]:
        comments.append(
            Comment(
                text=fake.text(),
                is_published=True,
                client=booking.client,
                barber=booking.barber,
                booking=booking,
                rating=random.randint(1, 5),
            )
        )

    Comment.objects.bulk_create(comments)

    return comments