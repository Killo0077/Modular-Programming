

def load_apps(filename):
    app_names = []
    downloads = []
    costs = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            app_names.append(parts[0])
            downloads.append(int(parts[1]))
            costs.append(float(parts[2]))

    return app_names, downloads, costs





def print_revenue(app_names, downloads, costs):
    total = 0

    print("\nApp Revenue")
    print("-" * 15)

    for i in range(len(app_names)):
        revenue = downloads[i] * costs[i]
        total += revenue
        print(f"{app_names[i]:<15}$  {revenue:.2f}")

    print("-"*15)
    print(f"Total: 4 {total:.2f}")


def get_apps_in_range(app_names, downloads, low, hight):
    result = []

    for i in range(len(app_names)):
        if low <= downloads[i] <= hight:
            result.append(app_names[i])

    return result




names, downloads, costs = load_apps("apps.txt")
print_revenue(names, downloads,costs)

apps = get_apps_in_range(names, downloads, 100,350)
print("\nApps with downloads between 100 and 350: ")
for app in apps:
    print(app)



