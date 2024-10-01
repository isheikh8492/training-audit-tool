from datetime import datetime


def list_user_trained_in_fiscal_year(data, trainings, fiscal_year):
    users_per_training = {}

    for user_completions in data:
        user = user_completions["name"]
        completions = user_completions["completions"]

        for i in range(len(completions)):
            if completions[i]["name"] in trainings:
                if is_in_fiscal_year(completions[i]["timestamp"], fiscal_year):
                    if completions[i]["name"] not in users_per_training:
                        users_per_training[completions[i]["name"]] = []
                    users_per_training[completions[i]["name"]].append(user)

    return users_per_training


def is_in_fiscal_year(date_string, fiscal_year):
    first_date = datetime.strptime(f"7/1/{fiscal_year - 1}", "%m/%d/%Y").date()
    end_date = datetime.strptime(f"6/30/{fiscal_year}", "%m/%d/%Y").date()
    timestamp_date = datetime.strptime(date_string, "%m/%d/%Y").date()
    return first_date <= timestamp_date <= end_date
