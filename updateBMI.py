import json

def printComparison(oldBMI, bmi):
    if (oldBMI != None):
        if oldBMI > bmi:
            print('You decrease your BMI rate')
        elif oldBMI < bmi:
            print('You increase your BMI rate')
        else:
            print('You keep your BMI rate')
    return
    
    
def printResult(bmi):
    if bmi < 18.5:
        print('You are underweight')

    elif bmi > 18.5 and bmi < 24.9:
        print('You are normal')

    elif bmi > 25 and bmi < 29.9:
        print('You are overweight')

    else:
        print('You are obese')
    return

def bmi_calc():
    f = open("data.JSON")
    info = json.load(f)
    f.close()


    oldBMI = None
    name = input('Insert your name: ')

    height = input('Insert your height [Centimeter]: ')
    height = float(height)

    weight = input('Insert your weight [Kilogram]: ')
    weight = float(weight)

    bmi = weight / (height * height)

    new_data = {'name': name,
                'height': height,
                'weight': weight,
                'bmi': bmi
                }

    for i in info:
        if new_data["name"] == i["name"]:
            oldBMI = i["bmi"]
            break
        else:
            info.append(new_data)


    with open("data.JSON", 'w') as f:
        json.dump(info, f)

    printResult(bmi)
        
    printComparison(oldBMI, bmi)
            
    return


     
            
def mainFunc():
    print('Welcome to the BMI system')
    bmi_calc()
    yes_no = input('Do you want to continue?[y/n]: ')
    while yes_no != 'n':
        bmi_calc()
        yes_no = input('Do you want to continue?[y/n]: ')
    return
mainFunc()
  
