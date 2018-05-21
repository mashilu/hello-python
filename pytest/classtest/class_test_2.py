from pytest.classtest.class_test_1 import Car


class Battery:
    """简单模拟电动汽车的电瓶"""

    def __init__(self, battery_size=70):
        self.batter_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.batter_size) + "-kWh battery.")

    def get_miles(self):
        """描述电瓶续航里程"""
        if self.batter_size == 70:
            miles = 240
        elif self.batter_size == 85:
            miles = 270

        message = "This car can go approximately " + str(miles) + " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.batter_size != 85:
            self.batter_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动车特有的属性
        :param make:
        :param model:
        :param year:
        """
        super().__init__(make, model, year)
        self.battery = Battery()


if __name__ == '__main__':
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_miles()

    my_tesla.battery.upgrade_battery()

    my_tesla.battery.describe_battery()
    my_tesla.battery.get_miles()
