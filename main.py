from data_loader import load_training_data
from tasks.task1 import list_completed_trainings
from tasks.task2 import list_user_trained_in_fiscal_year
from tasks.task3 import find_people_with_expiring_trainings

if __name__ == '__main__':
    data = load_training_data("data/trainings.txt")

    # Task 1: List each completed training with a count of how many people have completed that training.
    training_list = list_completed_trainings(data)
    print(training_list)

    # Task 2: List all people that completed that training in the specified fiscal year.
    training = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]
    fiscal_year = 2024
    users_per_training = list_user_trained_in_fiscal_year(data, training, fiscal_year)
    print(users_per_training)

    # Task 3: Find all people with expired or soon-to-expire trainings
    reference_date = "10/01/2023"
    users_with_expiring_trainings = find_people_with_expiring_trainings(data, reference_date)
    print(users_with_expiring_trainings)