"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    # Class variable shared across all devices
    device_category = "Smart Appliance"

    def __init__(self, brand, status="Offline"):
        self.brand = brand
        self.status = status

    def describe(self):
        """Returns basic information about the parent object."""
        return f"Brand: {self.brand}, Status: {self.status}, Category: {ParentClass.device_category}"

    def toggle_power(self):
        """Toggles the status of the device with error handling."""
        if self.status == "Online":
            self.status = "Offline"
        else:
            self.status = "Online"
        return f"{self.brand} is now {self.status}."


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    # New class variable specific to the child class
    protocol = "Wi-Fi"

    def __init__(self, brand, status, temperature, schedule_list):
        # Use super().__init__() to initialize parent attributes
        super().__init__(brand, status)
        self.temperature = temperature
        # Nested mutable data structure for copying demonstration
        self.schedule_list = schedule_list

    def set_temperature(self, new_temp):
        """New method to adjust temperature safely."""
        if isinstance(new_temp, (int, float)) and 50 <= new_temp <= 90:
            self.temperature = new_temp
            return f"Temperature set to {self.temperature}°F."
        else:
            raise ValueError("Error: Temperature must be a number between 50 and 90.")

    # Override the describe method from ParentClass
    def describe(self):
        """Overrides parent describe method to include child-specific attributes."""
        base_desc = super().describe()
        return (f"{base_desc} | Protocol: {ChildClass.protocol}, "
                f"Temperature: {self.temperature}°F, Schedule: {self.schedule_list}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two objects of the child class
    thermostat1 = ChildClass("Nest", "Online", 72, ["Monday", "Wednesday"])
    thermostat2 = ChildClass("Ecobee", "Offline", 68, ["Tuesday", "Thursday"])

    # Access class variables through the class itself
    print(f"Accessing via Class (ParentClass.device_category): {ParentClass.device_category}")
    print(f"Accessing via Class (ChildClass.protocol): {ChildClass.protocol}")

    # Access the same class variable through an object
    print(f"Accessing via Object 1 (thermostat1.protocol): {thermostat1.protocol}")

    # Add a new attribute to only one object after creation
    thermostat1.eco_mode = True

    # Display each object's namespace using __dict__
    print(f"\nthermostat1 __dict__: {thermostat1.__dict__}")
    print(f"thermostat2 __dict__: {thermostat2.__dict__}")

    # Display information about the class namespace
    print(f"\nChildClass __dict__ (Class Namespace): {ChildClass.__dict__}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create an original object containing nested mutable data (a list)
    original_thermostat = ChildClass("Honeywell", "Online", 70, [68, 72, 75])

    # Create a shallow copy
    shallow_thermo = copy(original_thermostat)

    # Create a deep copy
    deep_thermo = deepcopy(original_thermostat)

    print("--- Before Modifying Original ---")
    print(f"Original Schedule:       {original_thermostat.schedule_list}")
    print(f"Shallow Copy Schedule:   {shallow_thermo.schedule_list}")
    print(f"Deep Copy Schedule:      {deep_thermo.schedule_list}")

    # Modify the original object's nested data (appending to the list)
    original_thermostat.schedule_list.append(80)

    print("\n--- After Modifying Original (Added 80 to schedule) ---")
    print(f"Original Schedule:       {original_thermostat.schedule_list}")
    print(f"Shallow Copy Schedule:   {shallow_thermo.schedule_list}  <-- (Affected because it shares reference)")
    print(f"Deep Copy Schedule:      {deep_thermo.schedule_list}  <-- (Unaffected because it is fully independent)")

    # Explanation comments:
    # - copy.copy() (Shallow Copy): Copies the outer object container, but nested
    #   mutable objects (like the schedule_list) still reference the exact same memory
    #   address. Changing the original's list alters the shallow copy as well.
    # - copy.deepcopy() (Deep Copy): Recursively duplicates everything, including
    #   all nested mutable structures. The copy is entirely independent of the original.


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n[1] Testing Parent Class:")
    generic_device = ParentClass(brand="GenericBrand", status="Online")
    print(generic_device.describe())
    print(generic_device.toggle_power())

    print("\n[2] Testing Child Class:")
    smart_thermo = ChildClass(brand="Nest Learning", status="Online", temperature=72, schedule_list=[70, 74])
    print(smart_thermo.describe())
    print(smart_thermo.set_temperature(74))

    # Test error handling safeguard
    try:
        smart_thermo.set_temperature(105)
    except ValueError as e:
        print(f"Caught Expected Error: {e}")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()