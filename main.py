import json
import os
from data_loader import load_training_data
from tasks.task1 import list_completed_trainings
from tasks.task2 import list_user_trained_in_fiscal_year
from tasks.task3 import find_people_with_expiring_trainings


def generate_reports():
    if not os.path.exists('output'):
        os.makedirs('output')

    data = load_training_data("data/trainings.txt")

    # Task 1: List each completed training with a count of how many people have completed that training.
    training_count = list_completed_trainings(data)
    with open('output/output_task_1.json', 'w') as output1_file:
        json.dump(training_count, output1_file, indent=4)

    # Task 2: List all people that completed that training in the specified fiscal year.
    training = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]
    fiscal_year = 2024
    users_per_training = list_user_trained_in_fiscal_year(data, training, fiscal_year)
    with open('output/output_task_2.json', 'w') as output2_file:
        json.dump(users_per_training, output2_file, indent=4)

    # Task 3: Find all people with expired or soon-to-expire trainings
    reference_date = "10/01/2023"
    users_with_expiring_trainings = find_people_with_expiring_trainings(data, reference_date)
    with open('output/output_task_3.json', 'w') as output3_file:
        json.dump(users_per_training, output3_file, indent=4)

    print("Reports have been successfully generated in the 'output' directory.")


if __name__ == '__main__':
    generate_reports()
