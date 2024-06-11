class Package:
    def __init__(self, package_id, destination):
        self.package_id = package_id
        self.destination = destination


class Driver:
    def __init__(self, name):
        self.name = name
        self.packages = []

    def add_package(self, package):
        if len(self.packages) < 5:
            self.packages.append(package)
        else:
            print(f"Driver {self.name} cannot take more packages today.")


class DeliverySystem:
    def __init__(self):
        self.drivers = {}

    def add_driver(self, driver_name):
        if driver_name not in self.drivers:
            self.drivers[driver_name] = Driver(driver_name)

    def assign_package(self, driver_name, package):
        if driver_name in self.drivers:
            self.drivers[driver_name].add_package(package)
        else:
            print(f"Driver {driver_name} not found.")

    def print_driver_packages(self):
        for driver in self.drivers.values():
            print(f"Driver: {driver.name}")
            for package in driver.packages:
                print(
                    f"  Package ID: {package.package_id}, Destination: {package.destination}"
                )


def main():
    system = DeliverySystem()

    # Adding drivers
    system.add_driver("Alice")
    system.add_driver("Bob")

    # Creating packages
    package1 = Package(1, "123 Main St")
    package2 = Package(2, "456 Elm St")
    package3 = Package(3, "789 Oak St")
    package4 = Package(4, "101 Maple St")
    package5 = Package(5, "202 Pine St")
    package6 = Package(6, "303 Birch St")  # This package should not be assigned
    package7 = Package(7, "404 Cedar St")  # This package should not be assigned
    package8 = Package(8, "505 Walnut St")  # This package should not be assigned

    # Assigning packages to drivers
    system.assign_package("Alice", package1)
    system.assign_package("Alice", package2)
    system.assign_package("Alice", package3)
    system.assign_package("Alice", package4)
    system.assign_package("Alice", package5)
    system.assign_package("Alice", package6)  # This should trigger a warning
    system.assign_package("Alice", package7)  # This should trigger a warning
    system.assign_package("Alice", package8)  # This should trigger a warning

    system.print_driver_packages()


if __name__ == "__main__":
    main()
