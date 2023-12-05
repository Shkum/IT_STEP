'''Завдання 2
Створіть імітаційну модель «Причал морських катерів».
Введіть таку інформацію:
1. Середній час між появою пасажирів на причалі у різний час доби;
2. Середній час між появою катерів на причалі у різний час доби;
3. Тип зупинки катера (кінцева або інша).
Визначіть:
1. Середній час перебування людини на зупинці;
2. Достатній інтервал часу між приходами катерів, коли на зупинці не більше N людей одночасно;
3. Кількість вільних місць у катері є випадковою величиною.
Вибір необхідних структур даних визначте самостійно.'''


import random
import time

class MarinaSimulation:
    def __init__(self):
        self.passenger_arrival_rate = [5, 10, 15, 20, 10, 5, 3, 8, 12, 7, 5, 3]
        self.boat_arrival_rate = [8, 12, 10, 5, 3, 5, 10, 15, 20, 15, 10, 5]
        self.stop_type = random.choice(['end', 'other'])
        self.max_passengers = 20
        self.available_seats = random.randint(5, 15)

    def simulate(self, num_iterations):
        for i in range(num_iterations):
            current_hour = i % 12
            passengers = self.generate_passengers(current_hour)
            boats = self.generate_boats(current_hour)

            # Учет времени ожидания пассажиров и катеров
            waiting_time_passengers = max(0, boats - passengers) * self.boat_arrival_rate[current_hour]
            waiting_time_boats = max(0, passengers - self.available_seats) * self.passenger_arrival_rate[current_hour]
            total_stay_time = waiting_time_passengers + waiting_time_boats

            print(f'\nHour: {current_hour}, Type: {self.stop_type}')
            print(f'Passengers: {passengers}, Boats: {boats}, Available Seats: {self.available_seats}')
            print(f'Total Stay Time: {total_stay_time:.2f} minutes')

            time.sleep(1)

    def generate_passengers(self, current_hour):
        time_between_arrivals = self.passenger_arrival_rate[current_hour]
        return random.expovariate(1 / time_between_arrivals)

    def generate_boats(self, current_hour):
        time_between_arrivals = self.boat_arrival_rate[current_hour]
        return random.expovariate(1 / time_between_arrivals)

# Пример использования
simulation = MarinaSimulation()
simulation.simulate(24)
