def strategy_t():
    # 描述符作拦截器
    class StrategyValidator:
        def __init__(self):
            self.func = None

        def __set__(self, instance, value):
            if value(instance) < 0:
                raise ValueError("折扣金额不能小于0")

            self.func = value

        def __get__(self, instance, owner):
            return self.func

    class Order:
        strategy = StrategyValidator()

        def __init__(self, price, strategy):
            self.price = price
            self.strategy = strategy

        def apply_discount(self):
            return self.strategy(self)

    def discount_1(order: Order):
        return order.price * 0.1 - 5

    def discount_2(order: Order):
        return order.price * 0.2 - 5

    o = Order(40, discount_2)
    print(o.apply_discount())

    o = Order(40, discount_1)
    print(o.apply_discount())


if __name__ == '__main__':
    strategy_t()
