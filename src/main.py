from data_loader import load_training_data


if __name__ == '__main__':
    data = load_training_data("data/trainings.txt")
    print(data)
