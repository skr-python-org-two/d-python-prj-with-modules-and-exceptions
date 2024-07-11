from datetime import date , time , datetime


def main():
    print("Today date is ::: " , date.today())
    p = date.today()
    print("Today year is ::: " , p.year)
    print("Today month is ::: " , p.month)
    print("Today day is ::: " , p.day)

    # date in string format
    p_str = date.isoformat(p)
    print(p_str , type(p_str))

    my_date = date(1996, 12, 11)
    print(my_date)



if __name__ == "__main__":
    main()

