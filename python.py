import math
from datetime import date
print('=' * 30)
print('WEEKLY REPORT : \n    Name : LENOX KIBET.')
print('    Date', date.today())
print('=' * 30)

weight_kg = 69
height_m = 1.7
weekly_step = [7800, 9000, 8000, 9887, 10007, 7666, 8965]

protocols = ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"]    
 
#Calculating BMI .1 
def calculate_bmi (weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)
    
def bmi_category(bmi):
    if bmi < 18.5:
        return 'You are underweight person.'
    elif bmi < 25:
        return 'You have normal BMI.'
    elif bmi < 30:
        return 'You are an overweight person.'
    else:
        return 'You are an obese person.'    
        
bmi = calculate_bmi(weight_kg, height_m)     
print(f'Statu on BMI: \n Weight: {weight_kg} Kg. \n Height: {height_m} m.\n Calculated BMI : {bmi}.\n BMI category: {bmi_category(bmi)}')   
print('\n')

#Step goals checker. 2
def weekly_steps_summary(steps_list, goal= 8000):
    days_hit = len([s for s in steps_list if s>= goal])
    avarage =math.floor(sum(steps_list) / len(steps_list))
    best = max(steps_list)
    worst = min(steps_list)
    return { 'days on goal': days_hit,
               'avarage': avarage,
                'best day': best,
                'worst day': worst}
result = weekly_steps_summary (weekly_step)
print (f"Days on goal:  {result['days on goal']} / 7") 
print (f"Avarage:  {result['avarage']}") 
print (f"The best day: {result['best day']} steps.") 
print (f"The worst day:  {result['worst day']} steps.")   
print('\n')

#Calorie estimate. 3
def estimate_calories (steps, calories_per_step = 0.04):
    calories = steps * calories_per_step
    return math.floor(calories)
daily_cal = [estimate_calories(s) for s in weekly_step]   
print ('Estimate calories for the week.')
days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri' ,'Sat', 'Sun']
for day, cals in zip(days , daily_cal):
    print(f'{day}: {cals} Kcal.')
print(f'Total : {sum(daily_cal)} Kcal')    

print('\n')

#
def protocol_summary (protocol_list):
    unique = list(set(protocol_list))
    summary= {}
    for p in unique:
        summary[p] =protocol_list.count (p)
    return summary

result = protocol_summary(protocols)   
print('Protocols break down')  
for protocol, days in result.items():
              print(f'{protocol} : {days} day(s)')
print('\n')
              
print('END OF REPORT.')              
print("=" * 30)              
              

