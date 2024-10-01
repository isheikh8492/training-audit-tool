from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def find_people_with_expiring_trainings(data, reference_date):
    users_expiring_training = {}
    reference_date = datetime.strptime(reference_date, "%m/%d/%Y").date()
    expiring_soon_threshold = reference_date + relativedelta(months=+1)

    for user_completions in data:
        user = user_completions["name"]
        completions = user_completions["completions"]

        expiring_trainings = []
        for i in range(len(completions)):
            if completions[i]["expires"] is not None:
                expiration_date = datetime.strptime(completions[i]["expires"], "%m/%d/%Y").date()
                if reference_date > expiration_date:
                    expiring_trainings.append(
                        {"name": completions[i]["name"],
                         "status": "Expired"})
                elif reference_date <= expiration_date <= expiring_soon_threshold:
                    expiring_trainings.append(
                        {"name": completions[i]["name"],
                         "status": "Expiring Soon"})

        if expiring_trainings:
            users_expiring_training[user] = expiring_trainings

    return users_expiring_training
