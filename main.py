from data_loader import load_training_data
from tasks.task1 import list_completed_trainings

if __name__ == '__main__':
    data = load_training_data("data/trainings.txt")

    # Task 1: List each completed training with a count of how many people have completed that training.
    training_list = list_completed_trainings(data)
    print(training_list)

    # Task 2: List all people that completed that training in the specified fiscal year.
    training = trainings = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]
    fiscal_year = 2024
    # users = list_user_trained_in_fiscal_year(data, training, fiscal_year)