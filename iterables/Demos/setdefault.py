grades = {
    "English": 97,
    "Math": 93,
    "Art": 74,
    "Music": 86
}

grades.setdefault("Art", 87) # Art key exists. No change.
print("Art grade:", grades["Art"])

grades.setdefault("Gym", 97) # Gym key is new. Added and set.
print("Gym grade:", grades["Gym"])