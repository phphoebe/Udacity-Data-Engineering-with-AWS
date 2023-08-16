import pendulum
import logging

from airflow.decorators import dag, task


@dag(
    schedule_interval='@hourly',
    start_date=pendulum.now()
)
def task_dependencies():

    # the hello_world task doesn't accept parameters
    @task()
    def hello_world():
        logging.info("Hello World")

    # the addition task accepts two parameters and adds them together
    # logs the result, and returns it
    @task()
    def addition(first, second):
        logging.info(f"{first} + {second} = {first+second}")
        return first+second

    # the subtraction task accepts two parameters, and subracts the
    # second from the first, then logs and returns the result
    @task()
    def subtraction(first, second):
        logging.info(f"{first -second} = {first-second}")
        return first-second

    # the division task accepts two parameters, and divides the first
    # by the second, logs and returns the result
    @task()
    def division(first, second):
        logging.info(f"{first} / {second} = {int(first/second)}")
        return int(first/second)

# TODO: call the hello world task function

    # hello represents a discrete invocation of hello world
    hello = hello_world()


# TODO: call the addition function with some constants (numbers)

    # two_plus_two represents the invocation of addition with 2 and 2
    two_plus_two = addition(2, 2)


# TODO: call the subtraction function with some constants (numbers)

    # two_from_six represents the invocation of subtraction with 6 and 2
    two_from_six = subtraction(6, 2)


# TODO: call the division function with some constants (numbers)

    # eight_divided_by_two represents the invocation of division with 8 and 2
    eight_divided_by_two = division(8, 2)

# TODO: create the dependency graph for the first three tasks
# TODO: Configure the task dependencies such that the graph looks like the following:
#
#                    ->  addition_task
#                   /                 \
#   hello_world_task                   -> division_task
#                   \                 /
#                    ->subtraction_task

    # hello to run before two_plus_two and two_from_six
    hello >> two_plus_two
    hello >> two_from_six

    # Notice, addition and subtraction can run at the same time

    # two_plus_two to run before eight_divided_by_two
    two_plus_two >> eight_divided_by_two

    # two_from_six to run before eight_divided_by_two
    two_from_six >> eight_divided_by_two

    # Notice division waits for subtraction and addition to run

# TODO: assign the result of the addition function to a variable

    # sum represents the invocation of addition with 5 and 5
    sum = addition(5, 5)


# TODO: assign the result of the subtraction function to a variable

    # difference represents the invocation of subtraction with 6 and 4
    difference = subtraction(6, 4)


# TODO: pass the result of the addition function, and the subtraction functions to the division function

    # sum_divided_by_difference represents the invocation of division with the sum and the difference
    sum_divided_by_difference = division(sum, difference)


# TODO: create the dependency graph for the last three tasks

    # sum to run before sum_divided_by_difference
    sum >> sum_divided_by_difference

    # difference to run before sum_divided_by_difference
    difference >> sum_divided_by_difference


task_dependencies_dag = task_dependencies()
