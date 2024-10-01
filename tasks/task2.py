from datetime import datetime


def list_user_trained_in_fiscal_year(data, trainings, fiscal_year):
    users_per_training = {}

    for user_completions in data:
        user = user_completions["name"]
        completions = user_completions["completions"]

        for i in range(len(completions)):
            if completions[i]["name"] in trainings and \
                    is_in_fiscal_year(completions[i]["timestamp"], fiscal_year):
                if completions[i]["name"] not in users_per_training:
                    users_per_training[completions[i]["name"]] = []
                users_per_training[completions[i]["name"]].append(user)

    return users_per_training


def is_in_fiscal_year(date_string, fiscal_year):
    fiscal_start = datetime(fiscal_year - 1, 7, 1)
    fiscal_end = datetime(fiscal_year, 6, 30)
    return fiscal_start <= datetime.strptime(date_string, "%m/%d/%Y") <= fiscal_end
