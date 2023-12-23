from db.models import CinemaHall


from typing import List


def get_cinema_halls() -> List[CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> None:

    CinemaHall.objects.create(
        name=hall_name,
        hall_rows=hall_rows,
        hall_seats_in_row=hall_seats_in_row)