def list_completed_trainings(data):
    training_count = {}

    for person in data:
        trainings_completed = set()
        for completion in person["completions"]:
            if completion["name"] not in trainings_completed \
                    and completion["timestamp"] is not None:
                training_count[completion["name"]] = \
                    training_count.get(completion["name"], 0) + 1
                trainings_completed.add(completion["name"])

    return training_count
