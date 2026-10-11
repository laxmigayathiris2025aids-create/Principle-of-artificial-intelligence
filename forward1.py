
print("MEDICAL EXPERT SYSTEM")
print("BACKWARD CHAINING")
print()

patient = input("Enter Patient Name: ")

fever = input("Does the patient have Fever? (yes/no): ").lower()
cough = input("Does the patient have Cough? (yes/no): ").lower()
rash = input("Does the patient have Rash? (yes/no): ").lower()


def diagnose(goal):
    if goal == "Flu":
        return fever == "yes" and cough == "yes"

    elif goal == "Skin Disease":
        return rash == "yes"

    elif goal == "Viral Infection":
        return diagnose("Flu")

    return False


print("\nDiagnosis Results:")

if diagnose("Flu"):
    print(patient, "has Flu")
    print("Medication should be prescribed.")
elif diagnose("Skin Disease"):
    print(patient, "may have a Skin Disease")
    print("Medical consultation is recommended.")
else:
    print("Medical condition cannot be predicted.")

