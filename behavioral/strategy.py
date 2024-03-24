from __future__ import annotations

from abc import ABC, abstractmethod


class Navigator:
    def __init__(self, strategy: RouteStrategy) -> None:
        self._route_strategy = strategy

    @property
    def route_strategy(self) -> RouteStrategy:
        return self._route_strategy

    @route_strategy.setter
    def route_strategy(self, strategy: RouteStrategy) -> None:
        self._route_strategy = strategy

    def show_route(self, departure_point: float, destination_point: float) -> None:
        route = self._route_strategy.build_route(departure_point, destination_point)
        print(route)


class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, departure_point: float, destination_point: float) -> str:
        pass


class RoadStrategy(RouteStrategy):
    def build_route(self, departure_point: float, destination_point: float) -> str:
        return f"Поезжайте из точки {departure_point} в точку {destination_point}"


class WalkingStrategy(RouteStrategy):
    def build_route(self, departure_point: float, destination_point: float) -> str:
        return f"Идите из точки {departure_point} в точку {destination_point}"


if __name__ == "__main__":
    navigator = Navigator(RoadStrategy())

    departure_point = float(input("Введите точку отправления: "))
    destination_point = float(input("Введите точку назначения: "))

    navigator.show_route(departure_point, destination_point)
    navigator.route_strategy = WalkingStrategy()
    navigator.show_route(departure_point, destination_point)
