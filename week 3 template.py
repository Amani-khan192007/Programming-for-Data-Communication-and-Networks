"""
RECORD CHECK  -  my version
===========================

Name  : Amani Khan
Lane  :IT
Date  :7/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

#Threshold
def status_of(percent):
    '''Return the status based on the percentage.'''
    if percent >= 100:
        return 'OVER LIMIT'
    elif percent >= 90:
        return 'WARNING'
    else:
        return 'OK'
label = input("Enter hostname or IP: ")
value = float(input("Enter value: "))
limit = float(input("Enter limit: "))

difference = value - limit
percent = (value / limit) * 100
status = status_of(percent)

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"Value: {value}")
print(f"Limit: {limit}")
print(f"Status: {status}")
print("=" * 34)
#typical
def status_of(percent):
    '''Return the status based on the percentage.'''
    if percent >= 100:
        return 'OVER LIMIT'
    elif percent >= 90:
        return 'WARNING'
    else:
        return 'OK'

def check(value, limit):
    '''Return the difference and percentage.'''
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent

label = input('Enter hostname or IP: ')
value = float(input('Enter value: '))
limit = float(input('Enter limit: '))

difference, percent = check(value, limit)
status = status_of(percent)

print()
print('=' * 34)
print(f"RECORD CHECK  -  {label}")
print('=' * 34)
print(f"Value:      {value:10.2f}")
print(f"Limit:      {limit:10.2f}")
print(f"Difference: {difference:10.2f}")
print(f"Percent:    {percent:10.2f}")
print(f"Status:     {status:>10}")
print('=' * 34)