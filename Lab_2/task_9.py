salary = 5000
spend = 6000
months = 10
increase = 0.03

need_money = 0

while months > 0:
    need_money = need_money + spend - salary
    spend = spend * (1 + increase)
    months = months - 1
    if months == 0:
        print(round(need_money))


