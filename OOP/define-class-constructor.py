# define class constructor

class PhonePlan:
    # FIXME add constructor

    def print_plan(self):
        print('Mins:', self.num_mins, end=' ')
        print('Messages:', self.num_messages)

    def __init__(self, num_mins = 0, num_messages = 0):
        self.num_mins = num_mins
        self.num_messages= num_messages

my_plan = PhonePlan(200, 300)
dads_plan = PhonePlan()

print('My plan...', end=' ')
my_plan.print_plan()

print('Dad\'s plan...', end=' ')
dads_plan.print_plan()