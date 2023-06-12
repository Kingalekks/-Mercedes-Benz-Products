#!/usr/bin/env python
# coding: utf-8

# # Mercedes Benz Maybach GLS 600

# In[60]:


class car:
    def _init_(vehicle):
        vehicle.name = "Mercedes Benz"
        vehicle.model = "Maybach GLS 600 4MATIC"
        vehicle.color = "Black"
        vehicle.seater = "Four-seater, six-star-level comfort"
        vehicle.rims = "23' exclusive Maybach rims"
    
    def talk(vehicle):
        print("This luxury is", "Mercedes Benz")
        print("The model is", "Maybach GLS 600 4MATIC")
        print("Color:", "Black")
        print("With a", "Four-seater, six-star-level comfort")
        print("Rim size: 23' exclusive Maybach rims")
    
    def size(vehicle):
        if "vehicle.rims=23":
            print("This is the order")
        else:
            print("This is not the order")

Obj=car()
Obj.talk()
Obj.size()


# # Mercedes Benz AMG G 63

# In[113]:


class luxury():
    def _init_(benz):
        benz.brand = "Mercedes Benz"
        benz.model = "AMG G 63"
        benz.color = "White"
        benz.engine = "4.0-litre V8 biturbo engine delivering 430 kW (585 PS)"
    
    def ride(benz):
        print("The brand is", "Mercedes Benz")
        print("The model is", "AMG G 63")
        print("Color: White")
        print("The engine is 4.0-litre V8 biturbo engine delivering 430 kW (585 PS)")
    
    def rides(benz):
        if "benz.color=white":
            print("This is the order")
        else:
            print("This is not the order")

obj=luxury()
obj.ride()
obj.rides()  


# # Mercedes Benz C-Class

# In[114]:


class smooth:
    def _init_(sedan):
        sedan.brand = "Mercedes Benz C-Class"
        sedan.color = "White"
    
    def m(sedan):
        print("The Brand name is Mercedes Benz C-Class")
        print("The color available is Black")
    
    def b(sedan):
        if "sedan.color<white":
            print("This is not the right order!")
        else:
            print("This is the right order!")
    
obj=smooth()
obj.m()
obj.b()


# # Mercedes Benz V-Class

# In[115]:


class car:
    def _init_(zoom):
        zoom.brand = "Mercedes Benz V-Class"
        zoom.color = "Navy Blue"
        zoom.fuel_type = "Diesel"
        zoom.cylinder = "4 Cylinders"
    
    def v(zoom):
        print("The Brand is Mercedes Benz V-Class")
        print("The Color is Navy Blue")
        print("The Fuel type is Diesel")
    
    def c(zoom):
        if "zoom.cylinder>4 Cylinders":
            print("This is a wrong order!")
            print("This is the IF statement")
        else:
            print("This is the right order!")

obj=car()
obj.v()
obj.c()


# # Mercedes Benz E-Class

# In[122]:


class car:
    def _init_(drive):
        drive.brand = "Mercedes Benz E-Class"
        drive.color = "Black"
        drive.engine_type = "In-Line 4 Cylinder Petrol Engine"
        drive.transmission = "Automatic"
        drive.drive_type = "RWD"
        drive.max_power = "194.44bhp@5500-6100rpm"
        drive.max_torque = "320Nm@1650-4000rpm"
        drive.cylinders = "4 Cylinders"
    
    def e(drive):
        print("The Brand is Mercedes Benz E-Class")
        print("The Color is Black")
        print("The Engine type is In-Line 4 Cylinder Petrol Engine ")
        print("The Transmission is Automatic")
        print("The Drive type is RWD")
        print("The MaX Torque is 320Nm@1650-4000rpm")
        print("The Max power is 194.44bhp@5500-6100rpm")
        print("The number of cyclinder is 4")
    
    def c(drive):
        if "drive.cylinders=4":
            print("This is the right order!")
            print("This is the IF statement")
        else:
            print("This is a wrong order!")
            print("This is the ELSE statement!")
        
obj=car()
obj.e()
obj.c()     


# # Mercedes-Benz GLA

# In[21]:


class car:
    def _init_(taste):
        taste.brand = "Mercedes-Benz GLA"
        taste.color = "Grey"
        taste.engine_displacement = "1332 cc"
        taste.max_torque = "250Nm@1620–4000rpm"
        taste.max_power = "160.92bhp@5500rpm"
        taste.cylinders = 4
        taste.transmission = "Automatic"
        taste.gear_box = "7G-DCT"
        taste.drive_type = "FWD"
        taste.turbo_charger = "Yes"
        taste.alloy_wheel_size = "18"
        taste.fuel_type = "Petrol"
    
    def drive(taste):
        print("The brand name is Mercedes-Benz GLA")
        print("The available color is Grey")
        print("The engine displpacement is 1332 cc")
        print("This beauty has a Max Torque 250Nm@1620–4000rpm")
        print("Her Max Power is 160.92bhp@5500rpm")
        print("She's got 4 Cylinders")
        print("The transmission is Automatic")
        print("The gear  box is 7G-DCT")
        print("Drive type is FWD")
        print("Turbo Charger? YES")
        print("Her beautiful alloy wheel size is 18")
    
    def beauty(taste):
        if "taste.fuel_type=4":
            print("This is the order!")
            print("This is the IF statement")
        else:
            print("This is not the order!")
            print("This is the ELSE statement")

obj=car()
obj.drive()
obj.beauty()


# # Mercedes-Benz S-Class

# In[24]:


class car:
    def _init_(power):
        power.brand = "Mercedes-Benz S-Class"
        power.color = "Black"
        power.fuel_type = "Petrol/Diesel"
        power.mileage = "13.38 Kmpl"
        power.engine = "2925 - 2999 CC"
        power.transmission = "Automatic"
        power.max_power = "362.07bhp@5500-6100rpm"
        power.steering = "Electric"
        power.seating_capacity = 5
        power.max_torque =  "500Nm@1600-4500rpm"
        power.airbags = "Driver, Passenger, Side Front and Side Rear"
        power.fog_lamps =  "Both"
        power.engine_displacement =  "2999 cc"
        power.gear_shift_indicator = "Yes"
        power.central_locking = "Yes"
        power.child_safety_lock =  "Yes"
        power.abs = "Yes"
        power.power_windows =  "Front and Rear"
        power.emission_norm_compliance = "BS VI"
    
    def drive(power):
        print("The brand is Mercedes-Benz S-Class")
        print("The available color is Black")
        print("We've got Mercedes-Benz S-Class fuel types Petrol; and Diesel")
        print("Mileage is about 13.38 Kmpl")
        print("Engine is 2925 - 2999 CC")
        print("The transmission is Automatic")
        print("It's max power is 362.07bhp@5500-6100rpm")
        print("The steering is Electric")
        print("Having a sitting capacity of 5")
        print("Max Torque is 500Nm@1600-4500rpm")
        print("The Air Bags - Driver, Passenger, Side Front and Side Rear")
        print("Fog Lamps: Both")
        print("The engine displacement is 2999 cc")
        print("Gear Shift Indicator: Yes")
        print("Central Locking: Yes")
        print("Children are safe with child safety lock")
        print("ABS: Yes")
        print("The power windows: Front and Rear")
        print("Emission Norm Compliance: BS VI")
        
    def nice(power):
        if "power.seating_capacity=5":
            print("This is the order!")
            print("This is the IF statement")
        else:
            print("This is not the order!")
            print("This is the ELSE statement")
            
obj=car()
obj.drive()
obj.nice()


# In[ ]:




