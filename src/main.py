
SUBJECTS = ['URDU','ENGLISH','MATHS','PHYSICS','ISLAMIYAT','AL-QURAN','COMPUTER']

def print_subjects(subjects):
    for subject in subjects:
        print(subject)

print_subjects(SUBJECTS)

studing = True
count = 0
req_time = "10 mins"
while studing:
    print("\n" + SUBJECTS[count])
    syllabus = input(f"Enter the syllabus of {SUBJECTS[count]} : ")

    if syllabus == "none":
        count += 1
        if count == len(SUBJECTS):
            print("You have completed all subjects for now")
            break
        continue

# THINK HOW MUCH TIME WE GIVE TO DESIRED SUBJECT

    print(f"You have {req_time}")

# WAIT FOR USER TO SAY IS IT IS COMPLETED OR NOT
    iscompleted = False
    while iscompleted := True:
        prompt = input("")
        if prompt == "done" or prompt == "comp":
            count += 1
            iscompleted = False
            break
        elif prompt == "later":
            print(f"DO THAT NOW")
        else:
            print(f"Continue {SUBJECTS[count]}")

# ADDS THE BREAK AFTER TOO MUCH SYLLABUS

