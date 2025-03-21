from abc import ABC, abstractmethod
from decimal import Decimal

from paradex_py.common.order import OrderSide


class BaseExchange(ABC):
    _client = None

    buy_orders_list: list[(Decimal, Decimal)] = []
    sell_orders_list: list[(Decimal, Decimal)] = []

    open_orders: list[dict] = []
    open_positions: list[dict] = []

    mark_price: Decimal | None = None

    balance: Decimal | None = None

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def init_data_streams(self) -> None:
        pass

    @abstractmethod
    def modify_limit_order(self, order_id: str, order_side: OrderSide, order_size: Decimal, price: Decimal,
                           is_reduce: bool = False) -> dict | None:
        pass

    @abstractmethod
    def open_limit_order(self, order_side: OrderSide, order_size: Decimal, price: Decimal,
                         is_reduce: bool = False) -> dict | None:
        pass

    @abstractmethod
    def open_market_order(self, order_side: OrderSide, order_size: Decimal, is_reduce: bool = False):
        pass

    @abstractmethod
    def cancel_all_orders(self) -> None:
        pass

    @abstractmethod
    def close_all_positions(self) -> None:
        pass

    @abstractmethod
    async def critical_close_all(self) -> None:
        pass
