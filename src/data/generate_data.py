import random
import string
import numpy as np
from datetime import date, timedelta

### dates ###
date_day = np.random.randint(1, 29, 2000)
date_month = np.random.randint(1, 13, 2000)
order_start_date_year = np.random.randint(2040, 2045, 2000)
registration_date_year = np.random.randint(2039, 2045, 2000)
acquisition_date_year = np.random.randint(2035, 2040, 2000)
birth_date_year = np.random.randint(1930, 2021, 2000)


### person info ###
first_name_options = ['John', 'Maria', 'Jane', 'Lucas', 'Willian', 'Elizabeth', 'Roxanne', 'Louis',
                     'Richard', 'Miles', 'Michael', 'Ann', 'Rose', 'Christian', 'Rosalind', 'Jennifer']
last_names_options = ['Johnson', 'Smith', 'Phillips', 'Robertson', 'Winters', 'Summers', 'Washington',
                     'Owen', 'Montana', 'Robinson', 'Roswell', 'Jones', 'Lee', 'Silva', 'Ying', 'Ming']

email_number_options = np.random.randint(0, 10000, 10000)
email_options = ['@gnail.con', '@yay.con', '@liver.con', '@neutron.con', '@outspook.con']


### models ###
model_brand_options = ['Leopard', 'Ferrero', 'Lambeginning', 'Porch', 'Fort', 'Nissun']
model_name_options = []
model_name_options.append(['XJR-15', 'XJ220', 'C-X75'])
model_name_options.append(['SF-90', 'Testarossa', 'F-40'])
model_name_options.append(['Veneno', 'Countach', 'Aventador'])
model_name_options.append(['911', 'Panamera', 'Cayenne'])
model_name_options.append(['GT-40', 'Mustang', 'GT'])
model_name_options.append(['Skyline', 'R92CP', 'GT-R Nismo'])

model_brand_indices = np.random.randint(0, 6, 50)
model_brands = [model_brand_options[i] for i in model_brand_indices]
model_names = [random.choice(model_name_options[i]) for i in model_brand_indices]

operating_system_options = ['Doors', 'Minix', 'OrangeOS', 'Andromeda', 'OS/3']
operating_systems = np.random.choice(operating_system_options, 50)

cpu_options = ['Fallen 7', 'Fallen 9', 'Helium', 'Encore i9', 'Encore i11', 'N1', 'Xenon']
cpus = np.random.choice(cpu_options, 50)

memory_options = ['64 GB', '96 GB', '128 GB', '256 GB']
memories = np.random.choice(memory_options, 50)

generation_options = ['1', '2', '3', '4']
generations = np.random.choice(generation_options, 50)

service_options = ['Cleaner', 'Guard', 'Driver', 'Babysitter', 'Gardener', 'Cook']
services = np.random.choice(service_options, 50)

file_strings = []
for i in range(50):
    file_strings.append("INSERT INTO relational.models(model_brand, model_name, operating_system, "
                        + "cpu, memory, generation, service_category) VALUES (\'"
                        + model_brands[i] + "\', \'" + model_names[i] + "\', \'" + operating_systems[i] + "\', \'"
                        + cpus[i] + "\', \'" + memories[i] + "\', " + generations[i] + ", \'" + services[i] + "\');")
np.savetxt("2.InsertModels.sql", file_strings, fmt='%s')


### robots ###
model_ids = np.random.randint(1, 51, 900)

register_plates = []
while(True):
    for i in range(900):    
        register_plates.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=7)))
    if len(register_plates) == len(set(register_plates)):
        break

acquisition_dates = []
for i in range(900):
    acquisition_dates.append("".join(str(random.choice(date_day)).zfill(2) + "/" + str(random.choice(date_month)).zfill(2)
                                    + "/" + str(random.choice(acquisition_date_year))))

daily_rate_options = ['9.90', '14.90', '19.90', '24.90', '29.90', '39.90', '49.90', '59.90', '79.90', '99.90']
daily_rates = np.random.choice(daily_rate_options, 900)

robot_status_options = ['Available', 'Not available', 'Rented']
robot_statuses = np.random.choice(robot_status_options, 900)

file_strings = []
for i in range(900):
    file_strings.append("INSERT INTO relational.robots(model_id, register_plate, acquisition_date, daily_rate, status) VALUES ("
                        + str(model_ids[i]) + ", \'" + register_plates[i] + "\', \'" + acquisition_dates[i] + "\', "
                        + daily_rates[i] + ", \'" + robot_statuses[i] + "\');")
np.savetxt("3.InsertRobots.sql", file_strings, fmt='%s')


### customers ###
customer_emails = []
while(True):
    for i in range(2000):
        customer_emails.append("".join(random.choice(first_name_options).lower() + "_" + random.choice(last_names_options).lower())
                    + str(email_number_options[i]) + random.choice(email_options))
    if len(customer_emails) == len(set(customer_emails)):
        break
    else:
        customer_emails = []

customer_names = []
for i in range(2000):
    curr_customer_name = customer_emails[i].split("_")
    curr_customer_last_name = curr_customer_name[1].split("@")
    curr_customer_last_name = curr_customer_last_name[0].rstrip("0123456789")
    
    customer_names.append("".join(curr_customer_name[0].capitalize() + " " + curr_customer_last_name.capitalize()))

dates_of_births = []
for i in range(2000):
    dates_of_births.append("".join(str(random.choice(date_day)).zfill(2) + "/" + str(random.choice(date_month)).zfill(2)
                           + "/" + str(random.choice(birth_date_year))))

sex_options = ['Male', 'Female', 'Not informed']
sexes = np.random.choice(sex_options, 2000)

phone_numbers = []
for i in range(2000):
    phone_numbers.append(''.join(random.choices(string.digits, k=7)))

state_options = ['Rio Grande', 'San Andreas', 'Liberty', 'Vice', 'Calgary', 'Alberto', 'Cayman',
                 'Green Cape', 'Saimon', 'Holland']
city_options = []
city_options.append(['Silverado', 'Los Santos', 'Gamenon', 'Nebraska', 'America'])
city_options.append(['San Fierro', 'Las Venturas', 'Red City', 'Flint City', 'Tierra Robada'])
city_options.append(['Liberty City', 'Ranger', 'Los Alamos', 'Franka', 'Green River'])
city_options.append(['Bone City', 'Whetstone', 'Eldorado', 'Sparta', 'Troy'])
city_options.append(['Morales', 'Mape Town', 'Rivendell', 'Hobbiton', 'Middleton'])
city_options.append(['Rosewood', 'Charming', 'Hawkins', 'Smallville', 'Gotham'])
city_options.append(['Metropolis', 'Bedrock', 'New Vegas', 'Hogsmeade', 'Castle Rock'])
city_options.append(['Atlantis', 'Arkham', 'Emerald City', 'Minas Morgul', 'Rapture'])
city_options.append(['Cloud City', 'Wonderland', 'Springfield', 'Bethos', 'Calydon'])
city_options.append(['Basin City', 'Zion', 'Mos Eisley', 'New Tokyo', 'Night City'])

state_indices = np.random.randint(0, 10, 2000)
states = [state_options[i] for i in state_indices]
cities = [random.choice(city_options[i]) for i in state_indices]

road_options = ['Street', 'Avenue', 'Boulevard', 'Road']
addresses = []
for i in range(2000):
    addresses.append("".join(random.choice(road_options) + " " + random.choice(first_name_options)
                             + " " + random.choice(last_names_options) + " " + str(np.random.randint(100, 10001))))

dates_of_registrations = []
for i in range(2000):
    dates_of_registrations.append("".join(str(random.choice(date_day)).zfill(2) + "/" + str(random.choice(date_month)).zfill(2)
                                          + "/" + str(random.choice(registration_date_year))))

customer_status_options = ['Active', 'Inactive']
customer_statuses = np.random.choice(customer_status_options, 2000)

file_strings = []
for i in range(2000):
    file_strings.append("INSERT INTO relational.customers(email, name, date_of_birth, sex, phone_number, state_province, city, "
                        + "address, date_of_registration, status) VALUES (\'"
                        + customer_emails[i] + "\', \'" + customer_names[i] + "\', \'" + dates_of_births[i] + "\', \'"
                        + sexes[i] + "\', \'" + phone_numbers[i] + "\', \'" + states[i] + "\', \'" + cities[i] + "\', \'"
                        + addresses[i] + "\', \'" + dates_of_registrations[i] + "\', \'" + customer_statuses[i] + "\');")
np.savetxt("4.InsertCustomers.sql", file_strings, fmt='%s')


### salespersons ###
salesperson_emails = []
while(True):
    for i in range(2000):
        salesperson_emails.append("".join(random.choice(first_name_options).lower() + "_" + random.choice(last_names_options).lower())
                    + str(email_number_options[i]) + random.choice(email_options))
    if len(salesperson_emails) == len(set(salesperson_emails)):
        break
    else:
        salesperson_emails = []

salesperson_names = []
for i in range(2000):
    curr_salesperson_name = salesperson_emails[i].split("_")
    curr_salesperson_last_name = curr_salesperson_name[1].split("@")
    curr_salesperson_last_name = curr_salesperson_last_name[0].rstrip('0123456789')

    salesperson_names.append("".join(curr_salesperson_name[0].capitalize() + " " + curr_salesperson_last_name.capitalize()))

branch_options = ['Diamond', 'Sapphire', 'Emerald', 'Ruby', 'Quartz', 'Amethyst', 'Amber']
branches = np.random.choice(branch_options, 100)

salesperson_status_options = ['Active', 'Inactive']
salesperson_statuses = np.random.choice(salesperson_status_options, 100)

file_strings = []
for i in range(100):
    file_strings.append("INSERT INTO relational.salespersons(email, name, branch, status) VALUES (\'"
                        + salesperson_emails[i] + "\', \'" + salesperson_names[i] + "\', \'"
                        + branches[i] + "\', \'" + salesperson_statuses[i] + "\');")
np.savetxt("5.InsertSalespersons.sql", file_strings, fmt='%s')


### orders ###
robot_ids = np.random.randint(1, 901, 4000)

customer_ids = np.random.randint(1, 2001, 4000)

salesperson_ids = np.random.randint(1, 101, 4000)

orders_start_dates = []
for i in range(4000):
    orders_start_dates.append("".join(str(random.choice(date_day)).zfill(2) + "/" + str(random.choice(date_month)).zfill(2)
                                      + "/" + str(random.choice(order_start_date_year))))
orders_start_dates_datetime = [date(int(x[2]), int(x[1]), int(x[0])) for x in (y.split('/') for y in orders_start_dates)]

orders_end_dates_datetime = [x + timedelta(days=np.random.randint(1, 30)) for x in orders_start_dates_datetime]
orders_end_dates = [dt.strftime("%d/%m/%Y") for dt in orders_end_dates_datetime]
orders_end_dates_indexes = list(np.random.randint(0, 4000, 500))
np.array(orders_end_dates)[orders_end_dates_indexes] = 'NULL'

discount_percentage_options = [0.0, 0.01, 0.02, 0.05, 0.10]
discount_percentages = np.random.choice(discount_percentage_options, 4000)

total_prices = ['NULL'] * 4000
discounts = ['NULL'] * 4000
discounted_total_prices = ['NULL'] * 4000
for i in range(4000):
    if orders_end_dates[i] != 'NULL':
        robot_daily_rate = float(daily_rates[robot_ids[i] - 1])
        total_prices[i] = (orders_end_dates_datetime[i] - orders_start_dates_datetime[i]).days * robot_daily_rate
        discounts[i] = discount_percentages[i] * total_prices[i]
        discounted_total_prices[i] = total_prices[i] - discounts[i]

file_strings = []
for i in range(4000):
    file_strings.append("INSERT INTO relational.orders(robot_id, customer_id, salesperson_id, order_start_date, "
                        + "order_end_date, total_price, discount_percentage, discount, discounted_total_price) VALUES ("
                        + str(robot_ids[i]) + ", " + str(customer_ids[i]) + ", " + str(salesperson_ids[i]) + ", \'"
                        + orders_start_dates[i] + "\', " + (("\'" + orders_end_dates[i] + "\'") if orders_end_dates[i] != 'NULL' else 'NULL')
                        + ", " + str(round(total_prices[i], 2)) + ", " + str(round(discount_percentages[i], 2)) + ", "
                        + str(round(discounts[i], 2)) + ", " + str(round(discounted_total_prices[i], 2)) + ");")
np.savetxt("6.InsertOrders.sql", file_strings, fmt='%s')