import csv

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
energy_usage = [5.2, 6.8, 4.9, 7.3, 6.1]

total = sum(energy_usage)
average = total / len(energy_usage)
peak = max(energy_usage)
peak_day = days[energy_usage.index(peak)]

print("\nENERGY CONSUMPTION DASHBOARD\n")
print("Day     Energy Used (kWh)")
print("-------------------------")

for day, usage in zip(days, energy_usage):
    print(f"{day:<7} {usage}")

print(f"\nTotal Consumption: {total} kWh")
print(f"Average Usage: {average:.2f} kWh")
print(f"Peak Usage: {peak} kWh ({peak_day})")

with open("energy_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Day", "Energy Used (kWh)"])
    for day, usage in zip(days, energy_usage):
        writer.writerow([day, usage])

print("\nReport saved to energy_report.csv")
