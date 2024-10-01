from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def find_people_with_expiring_trainings(data, reference_date):
    users_expiring_training = {}
    reference_date = datetime.strptime(reference_date, "%m/%d/%Y").date()
    expiring_soon_threshold = reference_date + relativedelta(months=+1)

    for user_completions in data:
        user = user_completions["name"]
        latest_trainings = {}

        for completion in user_completions["completions"]:
            if completion["expires"] is not None:
                completion_date = datetime.strptime(completion["timestamp"], "%m/%d/%Y").date()
                expiration_date = datetime.strptime(completion["expires"], "%m/%d/%Y").date()

                if completion["name"] not in latest_trainings \
                        or completion_date > latest_trainings[completion["name"]]["completion_date"]:
                    latest_trainings[completion["name"]] = {
                        "completion_date": completion_date,
                        "expiration_date": expiration_date
                    }
        expiring_trainings = []
        for training_name, training_info in latest_trainings.items():
            if reference_date > training_info["expiration_date"]:
                expiring_trainings.append({"name": training_name, "status": "Expired"})
            elif reference_date <= training_info["expiration_date"] <= expiring_soon_threshold:
                expiring_trainings.append({"name": training_name, "status": "Expiring Soon"})

        if expiring_trainings:
            users_expiring_training[user] = expiring_trainings

    return users_expiring_training
