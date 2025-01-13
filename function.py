def get_Marks(marks):
    if marks < 0 or marks >100:
        print("Invalid marks")

    elif marks >= 0 and marks < 35:
        print("You failed the exam")

    elif marks >= 35 and marks < 55:
        print("You passed your grade is S ")

    elif marks >= 55 and marks < 65:
        print("You passed your grade is C")

    elif marks >= 65 and marks < 75:
        print("You passed your grade is B")

    elif marks >= 75 and marks < 100:
        print("You passed your grade is A")

get_Marks(65)
