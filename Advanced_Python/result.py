def check_result(marks):
    if marks>=40:

      return "Congralution you are pass"

    else:
      return "fail !Better LUCK next time"

marks=int(input("Enter mark:"))
result=check_result(marks)
print(result)


