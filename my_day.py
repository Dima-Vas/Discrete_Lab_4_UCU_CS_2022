"""
Productivity is the key to success in everything, and studying is not an exception.
But none of us are machines - our productivity is based on many of the factors.
This simple program will show the correlation between the life conditions and productivity.
And represent my day of course :)
"""
from numpy import random
# from time import sleep

class MyDay():
    """
    A class representing one of my days studying at UCU
    """
    def __init__(self, factors):
        
        # setting current stance of the system
        self.sleeping()

        self.factors = factors
        self.productiveness_coefficient = 1
        self.time_passed = 0
        self.hours_studied = 0
        self.stopped = False

    # initializing stances

    def sleeping(self):
        self.current_stance = "sleep"

    def eating(self):
        self.current_stance = "eat"

    def studying(self):
        self.current_stance = "study"

    def gym(self):
        self.current_stance = "gym"

    def relaxing(self):
        self.current_stance = "relax"


    def __str__(self) -> str:
        return f"My current stance is {self.current_stance}."
    
    def build_day(self, time = "06:00"):
        """
        The main function of this class
        """
        if self.current_stance == "sleep":
            if int(time.split(":")[0]) < 23 :
                if random.randint(0, 3):
                    self.eating()
                    if int(time.split(":")[0]) < 7: 
                        print(f"It's {time} now. What a new day!") 
                        self.productiveness_coefficient += 0.1
                    else :
                        print("Oh, I overslept!")
                        self.productiveness_coefficient -= 0.1
                else :
                    print("Zzzzzz....")
            else : 
                return
            time = str((int(time.split(":")[0]) + 1) % 24) + ":00"
            self.time_passed += 1

        elif self.current_stance == "eat":
            print(f"It's {time} now. A tasty meal.")
            if "coffee" in self.factors and self.time_passed < 16:
                print("I also have a coffee)")
                self.productiveness_coefficient += 0.1
                if "sleepy" in self.factors:
                    self.factors.remove("sleepy")
            if "exams" in self.factors or "deadlines" in self.factors or \
                "goodmood" in self.factors:
                self.studying()
            else:
                self.gym()
            time = str((int(time.split(":")[0]) + 1) % 24) + ":00"
            self.time_passed += 1
        
        elif self.current_stance == "gym":
            print(f"It's {time} now. And I'm gonna work out to max! >:-)")
            if "sleepy" in self.factors:
                self.factors.remove("sleepy")
            if "goodmood" not in self.factors:
                self.factors.append("goodmood")
            self.relaxing()
            time = str((int(time.split(":")[0]) + 1) % 24) + ":00"
            self.time_passed += 1
        
        elif self.current_stance == "relax":
            print(f"It's {time} now. It's time to chill.")
            if "quarrel" not in self.factors and "goodmood" not in self.factors:
                self.factors.append("goodmood")
                self.productiveness_coefficient += 0.1
            if int(time.split(":")[0]) > 22 :
                self.sleeping()
            self.eating()
            time = str((int(time.split(":")[0]) + 1) % 24) + ":00"
            self.time_passed += 1
        
        elif self.current_stance == "study":
            print(f"It's {time} now. Let's start studying!")
            if "sleepy" in self.factors :
                self.productiveness_coefficient -= 0.2
            elif "deadlines" in self.factors :
                self.productiveness_coefficient += random.randint(-1, 2)/10
            elif "exams" in self.factors :
                self.productiveness_coefficient += random.randint(-1, 2)/10
            elif "goodmood" in self.factors:
                self.productiveness_coefficient += 0.2
            self.hours_studied += 2
            self.relaxing()
            time = str((int(time.split(":")[0]) + 2) % 24) + ":00"
            self.time_passed += 2
        if self.time_passed < 18:
            # sleep(3)
            self.build_day(time)
        else :
            # sleep(3)
            have_done = "a good job!" if self.productiveness_coefficient > 1 else \
                "all I could."
            print(f"It's {time} now. Such a hard day it was. I have studied for \
{self.hours_studied} hours and done {have_done}. \
Now let`s have a nap at all..")


def run_my_day():
    """
    Runner function
    """
    factors = event_generator()
    me = MyDay(factors)
    me.build_day()

def event_generator():
    """
    Returns factors giving an influence to the productivity rate.
    """
    output = list(set(random.choice(["coffee", "sleepy", "deadlines",\
         "exams", "quarrel"], random.randint(1, 5))))
    return output

if __name__ == "__main__":
    run_my_day()
