from contextlib import nullcontext
import random
import string
import numpy as np

### dates ###
date_day = np.random.randint(1, 29, 2000)
date_month = np.random.randint(1, 13, 2000)
order_start_date_year = np.random.randint(2040, 2045, 2000)
registration_date_year = np.random.randint(2039, 2045, 2000)
acquisition_date_year = np.random.randint(2035, 2040, 2000)
birth_date_year = np.random.randint(1930, 2021, 2000)


### models ###
generation_options = ['NULL', '1', '2', '3', '4']
generation = np.random.choice(generation_options, 50)

operating_system_options = ['Doors', 'Minix', 'OrangeOS', 'Andromeda', 'OS/3']
operating_systems = np.random.choice(operating_system_options, 50)

cpu_options = ['ADM', 'Intelligent', 'N1', 'ARMY']
cpus = np.random.choice(cpu_options, 50)

memory_options = ['64 GB', '96 GB', '128 GB', '256 GB']
memories = np.random.choice(memory_options, 50)

service_options = ['Cleaner', 'Guard', 'Driver', 'Babysitter', 'Gardener', 'Cook']
services = np.random.choice(service_options, 50)

file_strings = []
for i in range(50):
    file_strings.append("INSERT INTO relational.models(generation, operating_system, cpu, memory, service_category) VALUES ("
                        + generation[i] + ", \'" + operating_systems[i] + "\', \'" + cpus[i] + "\', \'" + memories[i] + "\', \'" + services[i] + "\');")
np.savetxt("2.InsertModels.sql", file_strings, fmt='%s')


### robots ###
model_ids = np.random.randint(1, 51, 900)

acquisition_dates = []
for i in range(900):
    acquisition_dates.append("".join(str(random.choice(date_day)).zfill(2) + "/" + str(random.choice(date_month)).zfill(2) + "/" + str(random.choice(acquisition_date_year))))

register_plates = []
for i in range(900):    
    register_plates.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=7)))

daily_rate_options = ['9.90', '14.90', '19.90', '24.90', '29.90', '39.90', '49.90', '59.90', '79.90', '99.90']
daily_rates = np.random.choice(daily_rate_options, 900)

robot_status_options = ['Available', 'Not available', 'Rented']
robot_statuses = np.random.choice(robot_status_options, 900)

file_strings = []
for i in range(900):
    file_strings.append("INSERT INTO relational.robots(model_id, acquisition_date, register_plate, daily_rate, status) VALUES ("
                        + str(model_ids[i]) + ", \'" + acquisition_dates[i] + "\', \'" + register_plates[i] + "\', " + daily_rates[i] + ", \'" + robot_statuses[i] + "\');")
np.savetxt("3.InsertRobots.sql", file_strings, fmt='%s')


### customers ###
document_numbers = []
for i in range(2000):
    document_numbers.append(''.join(random.choices(string.digits, k=11)))

first_name_options = ['John', 'Maria', 'Jane', 'Lucas', 'Willian', 'Elizabeth', 'Roxanne', 'Louis']
last_names_options = ['Johnson', 'Smith', 'Phillips', 'Robertson', 'Winters', 'Summers', 'Washington', 'Owen', 'Montana']
customer_names = []
for i in range(2000):
    customer_names.append("".join(random.choice(first_name_options) + " " + random.choice(last_names_options)))

dates_of_births = []
for i in range(2000):
    dates_of_births.append("".join(str(random.choice(date_day)).zfill(2) + "/" + str(random.choice(date_month)).zfill(2)
                           + "/" + str(random.choice(birth_date_year))))

phone_numbers = []
for i in range(2000):
    phone_numbers.append(''.join(random.choices(string.digits, k=7)))

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
    file_strings.append("INSERT INTO relational.customers(document_number, name, date_of_birth, "
                        + "phone_number, address, date_of_registration, status) VALUES (\'"
                        + document_numbers[i] + "\', \'" + customer_names[i] + "\', \'" + dates_of_births[i] + "\', \'"
                        + phone_numbers[i] + "\', \'" + addresses[i] + "\', \'" + dates_of_registrations[i] 
                        + "\', \'" + customer_statuses[i] + "\');")
np.savetxt("4.InsertCustomers.sql", file_strings, fmt='%s')


### salesmen ###
salesman_names = []
for i in range(100):
    salesman_names.append("".join(random.choice(first_name_options) + " " + random.choice(last_names_options)))

branch_options = ['USA', 'Brazil', 'UK', 'Japan', 'China', 'France']
branches = np.random.choice(branch_options, 100)

salesman_status_options = ['Active', 'Inactive']
salesman_statuses = np.random.choice(salesman_status_options, 100)

file_strings = []
for i in range(100):
    file_strings.append("INSERT INTO relational.salesmen(name, branch, status) VALUES (\'"
                        + salesman_names[i] + "\', \'" + branches[i] + "\', \'" + salesman_statuses[i] + "\');")
np.savetxt("5.InsertSalesmen.sql", file_strings, fmt='%s')


### orders ###
robot_ids = np.random.randint(1, 901, 4000)

customer_ids = np.random.randint(1, 2001, 4000)

salesman_ids = np.random.randint(1, 101, 4000)

from datetime import date, timedelta

orders_start_dates = []
for i in range(4000):
    orders_start_dates.append("".join(str(random.choice(date_day)).zfill(2) + "/" + str(random.choice(date_month)).zfill(2) + "/" + str(random.choice(order_start_date_year))))
orders_start_dates_datetime = [date(int(x[2]), int(x[1]), int(x[0])) for x in (y.split('/') for y in orders_start_dates)]

orders_end_dates_datetime = [x + timedelta(days=np.random.randint(1, 30)) for x in orders_start_dates_datetime]
orders_end_dates = [dt.strftime("%d/%m/%Y") for dt in orders_end_dates_datetime]
orders_end_dates_indexes = list(np.random.randint(0, 4000, 500))
np.array(orders_end_dates)[orders_end_dates_indexes] = 'NULL'

total_prices = []
for i in range(4000):
    if orders_end_dates[i] != 'NULL':
        robot_daily_rate = float(daily_rates[robot_ids[i] - 1])
        total_prices.append((orders_end_dates_datetime[i] - orders_start_dates_datetime[i]).days * robot_daily_rate)
    else:
        total_prices[i] = 'NULL'

file_strings = []
for i in range(4000):
    file_strings.append("INSERT INTO relational.orders(robot_id, customer_id, salesman_id, order_start_date, order_end_date, total_price) VALUES ("
                        + str(robot_ids[i]) + ", " + str(customer_ids[i]) + ", " + str(salesman_ids[i]) + ", \'" + orders_start_dates[i] + "\', "
                        + (("\'" + orders_end_dates[i] + "\'") if orders_end_dates[i] != 'NULL' else 'NULL')
                        + ", " + str(round(total_prices[i], 2)) + ");")
np.savetxt("6.InsertOrders.sql", file_strings, fmt='%s')