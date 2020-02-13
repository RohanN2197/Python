class Parent():
    def print_last_name(self):
        print('Robertson')

class Child(Parent):
    def first_name(self):
        print('Buck')

    def print_last_name(self):
        print('OKAY')

buck = Child()
buck.print_last_name()
buck.first_name()
buck.print_last_name()