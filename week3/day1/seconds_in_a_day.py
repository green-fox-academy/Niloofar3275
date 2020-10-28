current_hours = 14;
current_minutes = 34;
current_seconds = 42;

seconds_of_a_day= 24 * 3600
x=seconds_of_a_day

seconds_of_current_minutes= current_minutes * 60
y=seconds_of_current_minutes

seconds_of_current_hours= current_hours * 3600
z=seconds_of_current_hours

k=current_seconds

seconds_of_the_current_time= y + z + k

m=seconds_of_the_current_time

Answer=x-m
print("The remaining seconds from a day is:", Answer)



# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables