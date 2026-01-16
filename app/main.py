class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str) \
            -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> int:
        clean_mark_change = 0
        if car.clean_mark < self.clean_power:
            clean_mark_change = self.clean_power - car.clean_mark
            car.clean_mark = self.clean_power
        return clean_mark_change

    def serve_cars(self, cars: Car) -> float:
        income = 0.0
        if len(cars):
            for car in cars:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            return round((self.clean_power - car.clean_mark)
                         * car.comfort_class
                         * self.average_rating
                         / self.distance_from_city_center,
                         1)
        else:
            return 0.0

    def rate_service(self, rating: int) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings
                                     + rating)
                                    / (self.count_of_ratings + 1),
                                    1)
        self.count_of_ratings += 1
