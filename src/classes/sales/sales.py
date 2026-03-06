from typing import List, Dict
from pydantic import BaseModel
import pandas
import json
from collections import defaultdict



# Модели Pydantic
class Product(BaseModel):
    id: int
    name: str
    price: float

class Customer(BaseModel):
    id: int
    name: str

class Order(BaseModel):
    id: int
    customer_id: int
    product_ids: List[int]

class SalesAnalyzer:

    def __init__(self, products: List[Product], customers: List[Customer], orders: List[Order]):
        self.products = products
        self.customers = customers
        self.orders = orders




    def analyze(self) -> Dict:
        most_popular_name, most_popular_count = self.get_most_popular_product()
        total_revenue, avg_order = self.get_avg_revenue_info()

        return {
            "popular_product": {"name": most_popular_name, "sales_count": most_popular_count},
            "average_check": avg_order,
            "total_revenue": total_revenue
        }

    def get_avg_revenue_info(self) -> tuple[float | None, float | None]:
        if len(self.orders) == 0:
            return 0, 0

        price_dict = dict()
        for product in self.products:
            price_dict[product['id']] = product['price']

        order_totals = dict()
        for order in self.orders:
            order_sum = 0
            for product_id in order['product_ids']:
                if price_dict.get(product_id) is not None:
                    order_sum += price_dict.get(product_id)
                else:
                    raise KeyError("Ключ не найден")
            order_totals[order['id']] = order_sum

        total_revenue = sum(order_totals.values())
        avg_order = total_revenue / len(order_totals)

        return total_revenue, avg_order


    def get_most_popular_product(self) -> tuple[str | None, int | None]:
        if len(self.orders) == 0:
            return None, 0
        product_sales = dict()

        for order in self.orders:
            for p_id in order['product_ids']:
                product_sales[p_id] = product_sales.get(p_id, 0) + 1



        most_popular_id = max(product_sales, key=product_sales.get)
        most_popular_sales_count = product_sales[most_popular_id]

        product_names = {p['id']: p['name'] for p in self.products}

        return product_names[most_popular_id], most_popular_sales_count



def load_data(products_path: str, customers_path: str, orders_path: str) -> SalesAnalyzer:

    with open(products_path, "r") as f:
        products = json.load(f)

    with open(customers_path, "r") as f:
        customers = json.load(f)
    with open(orders_path, "r") as f:
        orders = json.load(f)
    return SalesAnalyzer(products=products, customers=customers, orders=orders)


def print_results(analysis: Dict):
    print(f"Самый популярный товар: {analysis['popular_product']['name']} ({analysis['popular_product']['sales_count']} продажи) Средний чек покупателя: {analysis['average_check']} Общая выручка: {analysis['total_revenue']}")
    pass

# Пример использования
if __name__ == "__main__":
    print('zalupa')
    analyzer = load_data("/products.json", "/customers.json", "/orders.json")
    analysis = analyzer.analyze()
    print_results(analysis)