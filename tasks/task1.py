from datetime import datetime


def list_completed_trainings(data):
    training_count = {}

    for user_completions in data:
        latest_trainings = {}

        for completion in user_completions["completions"]:
            timestamp = datetime.strptime(completion["timestamp"], "%m/%d/%Y")
            if completion["name"] not in latest_trainings \
                    or timestamp > latest_trainings[completion["name"]]:
                latest_trainings[completion["name"]] = timestamp

        for training in latest_trainings:
            training_count[training] = training_count.get(training, 0) + 1

    return training_count
