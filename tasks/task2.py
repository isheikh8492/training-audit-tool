from datetime import datetime


def list_user_trained_in_fiscal_year(data, trainings, fiscal_year):
    users_per_training = {t: [] for t in trainings}

    for user_completions in data:
        user = user_completions["name"]
        latest_trainings = {}

        for completion in user_completions["completions"]:
            if completion["name"] in trainings:
                timestamp = datetime.strptime(completion["timestamp"], "%m/%d/%Y")
                if completion["name"] not in latest_trainings \
                        or timestamp > latest_trainings[completion["name"]]:
                    latest_trainings[completion["name"]] = timestamp

        for training_name, timestamp in latest_trainings.items():
            if is_in_fiscal_year(timestamp, fiscal_year):
                users_per_training[training_name].append(user)

    return users_per_training


def is_in_fiscal_year(date, fiscal_year):
    fiscal_start = datetime(fiscal_year - 1, 7, 1)
    fiscal_end = datetime(fiscal_year, 6, 30)
    return fiscal_start <= date <= fiscal_end
