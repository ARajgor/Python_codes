t=input("Enter Current Time (in HH:MM format): ").split(':')

if int(t[0])>24 or int(t[1])>60:
    print("Please enter valid time..!!!!")
else:
    print(f"Thanks! It is now {t[1]} minutes after {t[0]} o'clock....")
