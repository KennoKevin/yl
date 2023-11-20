import random

user_action = input("Vali kivi, paber või käärid: ")

possible_actions = ["kivi", "paber", "käärid"]
computer_action = random.choice(possible_actions)

print(f"\nSina valisid {user_action}, arvuti valis {computer_action}.\n")

if user_action == computer_action:
    print(f"Mõlemad valisid {user_action}. Viik")
elif user_action == "kivi":
    if computer_action == "käärid":
        print("Kivi võidab käärid! Sina võitsid")
    else:
        print("Paber katab kivi! Sina kaotasid")
elif user_action == "paber":
    if computer_action == "kivi":
        print("Paber katab kivi! Sina võitsid")
    else:
        print("Käärid lõikavad paberi! Sa kaotasid")
elif user_action == "käärid":
    if computer_action == "paber":
        print("Käärid lõikavad paberit! Sina võitsid")
    else:
        print("Kivi lõhkus käärid! Sina kaotasid")