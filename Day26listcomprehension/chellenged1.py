sen = "What is the Airspeed Velocity of an Unladen Swallow"
new_list = sen.split() # splits each work in a sentence

new_dict = {key:len(key) for key in new_list}
print(new_dict) 

