from functools import reduce

with open("2020/survey.txt", "r") as groups:
    groups = groups.read().split("\n\n")
total_answers = []
for group in groups:
    shared_answers = set(group.split()[0])
    for person in group.split():
        shared_answers = shared_answers.intersection(set(person))
    total_answers.append(len(shared_answers))
total_answers = reduce(lambda a, b: a + b, total_answers)
print(total_answers)
