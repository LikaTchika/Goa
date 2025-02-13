

def simple_calculator(num1, num2, operation):
    if operation == "დამატება":
        return num1 + num2
    elif operation == "გამოკლება":
        return num1 - num2
    elif operation == "გამრავლება":
        return num1 * num2
    elif operation == "გაყოფა":
        if num2 == 0:
            return "შეცდომა: ნულზე გაყოფა შეუძლებელია"
        else:
            return num1 / num2
    else:
        return "არასწორი ოპერაცია"

# Example calls
print(simple_calculator(10, 5, "დამატება"))  # 15
print(simple_calculator(10, 5, "გაყოფა"))   # 2.0
print(simple_calculator(10, 0, "გაყოფა"))   # შეცდომა: ნულზე გაყოფა შეუძლებელია

def personal_info(name, surname, age, country, city, hobby):
    return f"ჩემი სახელი არის {name} {surname}, მე {age} წლის ვარ, ვცხოვრობ {city}-ში, {country}-ში და ჩემი საყვარელი ჰობი არის {hobby}."

# Example call
print(personal_info("გიორგი", "ბაქრაძე", 25, "საქართველო", "თბილისი", "მუსიკის მომისმენა"))
