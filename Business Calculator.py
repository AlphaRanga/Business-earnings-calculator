from gekko import GEKKO
m = GEKKO()
x = m.Var()
y = m.Var()
c = m.Var()
h = m.Var()



total_cost_make = float (input("How much does it cost to manufacture and sell the product per unit (excluding cost of workers): "))
print("")

sell_cost = float (input("How Much would you sell your product for: "))
print("")

product_cost = (sell_cost - total_cost_make)

worker_cost_hr = float (input("What is your workers/worker hourly rate (0 if no worker): "))
print("")
worker_hours = float (input("How many hours per week does your worker/workers work: "))
print("")
workers_amount = float (input("How many workers/worker do you have: "))
print("")

product_sell_day = float (input("How many products do you sell in a day: "))

daily_earn = (product_sell_day * product_cost)

daily_earn_str = str(daily_earn)
print("")

print("")

weeks_year = float (input("How many weeks do you sell you product in a year: "))
print("")

weeks_year_worker = float (input("How many weeks does your worker/workers work in a year: "))

print("")
print("")
print("**************************************")


print("Your daily earning is $" + daily_earn_str)
print("")
yearly_earn = (daily_earn * 5 * weeks_year)

worker_week_cost = (worker_cost_hr * worker_hours)
workers_cost = (worker_week_cost * weeks_year_worker * workers_amount)

weeks_year_str = str(yearly_earn)

print("You earn $" + weeks_year_str + " in a year")
print("")

print("You will pay your workers", workers_cost, "$ in a year")

print("Please Wait...")
m.Equation (yearly_earn*x==1000000)
m.solve(disp=False)
print("")
print("It will take", x.value, "years to earn 1 Million dollars")
print("And...")

m.Equation (yearly_earn*y==10000000)
m.solve(disp=False)
print("It will take", y.value, "years to earn 10 million dollars")
print("And...")

m.Equation (yearly_earn*c==5000000)
m.solve(disp=False)
print("It will take", c.value, "years to earn 5 million dollars")
print("And...")

m.Equation (yearly_earn*h==100000)
m.solve(disp=False)
print("It will take", h.value, "years to earn 100k dollars")
print("And...")

profit_margin = (product_cost / total_cost_make * 100)
print("Your profit margin is ", profit_margin, "%")

workers_cost_tax10 = ((workers_cost / 100) * 10)
workers_cost_tax8 = ((workers_cost / 100) * 8)
workers_cost_tax4 = ((workers_cost / 100) * 4)
workers_cost_tax3 = ((workers_cost / 100) * 3)

print("")
print("If the majority of your workers choose 10% kiwi saver fund you could contribute about ", workers_cost_tax10, "$ to their kiwi saver fund")
print("")
print("If the majority of your workers choose 8% kiwi saver fund you could contribute about ", workers_cost_tax8, "$ to their kiwi saver fund")
print("")
print("If the majority of your workers choose 4% kiwi saver fund you could contribute about ", workers_cost_tax4, "$ to their kiwi saver fund")
print("")
print("If the majority of your workers choose 3% kiwi saver fund you could contribute about ", workers_cost_tax3, "$ to their kiwi saver fund")

total = (workers_cost + (((total_cost_make * product_sell_day) * 5) * weeks_year_worker))

print("")
print("**************************************************")
print("Yout Total estimated yearly cost is: ", total, "$ + your kiwi saver fund payment")
print("")
print("And your earnings are " + weeks_year_str + "$")
revenue = (total + yearly_earn)
print("")
print("Your company turns over", revenue, "$ in revenue per year")
print("")

invest = (revenue / 100 * 20)

if yearly_earn > total or yearly_earn > 3000000:
    print("")
    print("you have enough money to start manufacturing a diffrent product because")
    print("your personal earnings are greater that the cost to run the company")
    print("I recomend you invest ", invest, "$ share into your company")
    print("this will give you about 20% of shares in your company")


if yearly_earn < 50000:
    print("")
    print("I recomend you review your budget and earnings as your yearly income is ")
    print("bellow 50k ")


if worker_cost_hr < 17.50:
    print("")
    print("you are under paying your workers the legal amount")
    print("your workers recieve", worker_cost_hr, "this is below legal")

print("")
print("Nice!")


done = input("press enter if your done")








