import phonenumbers
from phonenumbers import carrier,timezone,geocoder
number=input("enter your number with + : ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
sim_name=carrier.name_for_number(phone,"en")
region=geocoder.description_for_number(phone,"en")
print("time_zone :",time)
print("Sim_name :",sim_name)
print("region :",region)
