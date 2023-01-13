
# Let us now briefly look at the techniques to size the memory.

# 1 GB of memory reserved for Operating System
# 1 GB each for every 4 GB of RAM after the initial 4 GB, up to 16 GB of RAM
# 1 GB each for every 8 GB in more than 16 GB of RAM


total_memory = int(input("What is the total memory of the server in GB? "))

operating_sys_memory = 0
sql_server_memory = 0
if total_memory <= 4:
    operating_sys_memory = 1
    sql_server_memory = total_memory - operating_sys_memory
    print(f"As per best practice recommendation the reserved memory for the Operating system should be : {operating_sys_memory} GB")
    print(f"As per best practice recommendation the reserved memory for the SQL Server should be: {sql_server_memory} GB")
elif total_memory > 4 and total_memory <= 16:
    operating_sys_memory = 1
    addition = (total_memory - 4) // 4
    operating_sys_memory += addition
    sql_server_memory = total_memory - operating_sys_memory
    print(f"As per best practice recommendation the reserved memory for the Operating system is: {operating_sys_memory} GB")
    print(f"As per best practice recommendation the reserved memory for the SQL Server should be: {sql_server_memory} GB")
elif total_memory > 16:
    operating_sys_memory = 4
    addition = (total_memory - 16) // 8
    operating_sys_memory += addition
    sql_server_memory = total_memory - operating_sys_memory
    print(f"As per best practice recommendation the reserved memory for the Operating system is: {operating_sys_memory} GB")
    print(f"As per best practice recommendation the reserved memory for the SQL Server should be: {sql_server_memory} GB")
else:
    print("Please enter positive value")
