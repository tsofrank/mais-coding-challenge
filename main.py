import csv
import matplotlib.pyplot as plt
import numpy as np

# declare lists to store values
car = []
credit_card = []
debt_consolidation = []
home_improvement = []
house = []
major_purchase = []
medical = []
moving = []
other = []
small_business = []
vacation = []
wedding = []


def calc_avg(list):  # this function is used to calculate the average avg_rate for all purposes
    avg = 0
    for item in list:
        avg += float(item)
    avg /= len(list)
    return avg


def results_table():    # this function prints a table of purposes and avg_rate
    title_purpose = "Purpose"
    title_rate = "Avg_Rate"
    print("%-25s %s" % (title_purpose, title_rate))
    print("%-25s %.3f" % ("car", car_avg))
    print("%-25s %.3f" % ("credit_card", credit_avg))
    print("%-25s %.3f" % ("debt_consolidation", debt_avg))
    print("%-25s %.3f" % ("home_improvement", home_avg))
    print("%-25s %.3f" % ("house", house_avg))
    print("%-25s %.3f" % ("major_purchase", purchase_avg))
    print("%-25s %.3f" % ("medical", medical_avg))
    print("%-25s %.3f" % ("moving", moving_avg))
    print("%-25s %.3f" % ("other", other_avg))
    print("%-25s %.3f" % ("small_business", biz_avg))
    print("%-25s %.3f" % ("vacation", vacation_avg))
    print("%-25s %.3f" % ("wedding", wedding_avg))


def plot_graph():   # this function plots the bar chart
    purpose = ["car", "credit_card", "debt_consolidation", "home_improvement", "house", "major_purchase", "medical",
               "moving", "other", "small_business", "vacation", "wedding"]
    avg_rate = [car_avg, credit_avg, debt_avg, home_avg, house_avg, purchase_avg, medical_avg, moving_avg, other_avg,
                biz_avg, vacation_avg, wedding_avg]
    ypos = np.arange(len(purpose))

    plt.xticks(ypos, purpose, rotation = 45)
    plt.xlabel("Purpose")
    plt.ylabel("Average Rate")
    plt.title("Average Rate of Different Financial Purposes")
    plt.bar(ypos, avg_rate)
    plt.show()


with open('data.csv', 'r') as csv_file:  # read the file and store different purposes into respective lists
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # skip the titles

    for line in csv_reader:
        if line[16] == "car":
            car.append(line[5])
        elif line[16] == "credit_card":
            credit_card.append(line[5])
        elif line[16] == "debt_consolidation":
            debt_consolidation.append(line[5])
        elif line[16] == "home_improvement":
            home_improvement.append(line[5])
        elif line[16] == "house":
            house.append(line[5])
        elif line[16] == "major_purchase":
            major_purchase.append(line[5])
        elif line[16] == "medical":
            medical.append(line[5])
        elif line[16] == "moving":
            moving.append(line[5])
        elif line[16] == "other":
            other.append(line[5])
        elif line[16] == "small_business":
            small_business.append(line[5])
        elif line[16] == "vacation":
            vacation.append(line[5])
        else:
            wedding.append(line[5])

# calculate average_rates of various purposes
car_avg = calc_avg(car)
credit_avg = calc_avg(credit_card)
debt_avg = calc_avg(debt_consolidation)
home_avg = calc_avg(home_improvement)
house_avg = calc_avg(house)
purchase_avg = calc_avg(major_purchase)
medical_avg = calc_avg(medical)
moving_avg = calc_avg(moving)
other_avg = calc_avg(other)
biz_avg = calc_avg(small_business)
vacation_avg = calc_avg(vacation)
wedding_avg = calc_avg(wedding)

plot_graph()
results_table()









