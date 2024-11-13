profit = [15, 27, 10, 100, 150]
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadline = [2, 3, 3, 3, 4]

# Zip and sort jobs by profit in descending order
profitNJobs = list(zip(profit, jobs, deadline))
profitNJobs = sorted(profitNJobs, key=lambda x: x[0], reverse=True)

# Determine maximum deadline to size the slots and result arrays appropriately
max_deadline = max(deadline)
slot = [0] * (max_deadline + 1)  # Index 0 is unused for simplicity
ans = ['null'] * (max_deadline + 1)

profit = 0

# Schedule each job based on the sorted profit list
for job in profitNJobs:
    # Check backwards from the job's deadline to find an available slot
    for j in range(job[2], 0, -1):
        if slot[j] == 0:  # If slot is free
            ans[j] = job[1]
            profit += job[0]
            slot[j] = 1
            break

# Filter out unused slots (null values)
scheduled_jobs = [job for job in ans if job != 'null']

print("Jobs scheduled:", scheduled_jobs)
print("Maximum Profit:", profit)
