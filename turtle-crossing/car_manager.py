from car import Car
import random


class CarManager:
    def __init__(self, num_cars, start_x, screen_height, screen_width, speed):
        self.cars = []
        self.current_speed = speed
        self.start_y_list = []
        self.create_ycor_list(screen_height)

        self.start_x = start_x
        self.screen_height = screen_height
        self.screen_width = screen_width
        for _ in range(num_cars):
            self.add_car()

    def add_car(self):
        car = Car(
            start_speed=self.current_speed,
            start_x=self.start_x,
            start_y=random.choice(self.start_y_list),
        )
        self.cars.append(car)

    def drive_all(self):
        for car in self.cars:
            car.drive()

    def create_ycor_list(self, screen_height):
        top = int(screen_height / 2 - 40)
        bottom = int(-(screen_height / 2) + 70)

        for ycor in range(bottom, top, 30):
            self.start_y_list.append(ycor)

    def speed_up_all(self, factor):
        self.current_speed = self.current_speed * factor
        for car in self.cars:
            car.speed_up(factor=factor)

    def cleanup(self):
        for car in self.cars:
            if car.xcor() < -(self.screen_width / 2) - 20:
                self.cars.remove(car)
                car.hideturtle()
                car.clear()
                car.reset()
                del car

    def reset(self):
        for car in self.cars:
            car.hideturtle()
            car.clear()
            car.reset()
            self.cars.remove(car)
            del car
            self.current_speed = 1

    def did_car_hit(self, x_cor, y_cor, threshold):
        print(f"{x_cor}, {y_cor}, {threshold}")
        print(f"cars length: {len(self.cars)}")

        print(self.cars)
        for car in self.cars:
            print(f"Car {hash(car)}: {car.xcor()}, {car.ycor()} ")
            if car.distance(x_cor, y_cor) < threshold:
                return True

