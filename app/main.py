from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: str,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []
    cleaner_instance = Cleaner(cleaner)
    for data in customers:
        customer = Customer(data["name"], data["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_instances, cleaner_instance)
