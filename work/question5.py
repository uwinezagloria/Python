"""Use the if condition to implement the following solution (you can use Boolean or any type of 
variable)"""
print("Fixing  Bulb Lamp")
print("Fixing Bulb Lamp")

lamp_work = True        # Lamp is working
lamp_plugged_in = False
bulb_burned_out = True

if lamp_work:
    print("Lamp is working fine!")
else:
    if not lamp_plugged_in:
        print("Plug in lamp")
    elif bulb_burned_out:
        print("Repair Bulb")
    else:
        print("Replace Bulb")
