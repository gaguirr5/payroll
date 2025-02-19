# try except block will allow the user to keep the program from breaking, example if you put a letter in any float(input()), the program will break because it expects a number so it doesn't know what to do
# None can be useful to declare a variable without giving it a real value yet
# \n creates a new line, I use it for spacing
# \t adds a tab, I used this for spacing
# display_running_total is optional, depends if you want to let the user know as they go

# I used while loops at each input because we don't want to let the user continue inputting when they give an invalid input. 

def my_app():
  valuer_error_msg = 'Invalid input. Enter a valid number.' # reuse error message
  
  # get input from user for deductions
  def get_user_deduction(deduction_type, gross_pay, deduction_total):
    return_value = None
    # make sure user gives a valid input 
    while return_value is None:
      try:
        user_input = float(input(f"Enter {deduction_type} Amount: $"))
        if user_input > gross_pay:
          print('Value cannot be higher then gross pay')
        elif user_input < 0:
          print('Value cannot be negative')
        elif (deduction_total + user_input) > gross_pay:
          print('Deductions cannot be higher than Gross Pay')
        else:
          return_value = user_input
          print('\n')
    
      except ValueError: # account for user not using a number
        print(valuer_error_msg)
    return return_value

  def display_running_total(deductions):
    print(f"Deductions so far: ${format(deductions, '.2f')}")

  while True:
    employee_id = None
    gross_pay = None
    deductions = 0.00

    while employee_id is None: # don't leave loop until employee enters valid number
      try:
        employee_id = int(input('Enter Employee ID (0 to exit): '))
        if (employee_id == 0): 
          print('Thank you for playing!')
          return # this will exit the program
      except ValueError:
        print(valuer_error_msg)
      
    while gross_pay is None:
      try: 
        gross_pay = float(input('Please Enter Gross Pay: $'))
        if (gross_pay < 0):
          print("Gross pay can't be negative")
        else:
          print('\n')
          break
      except ValueError:
        print(valuer_error_msg)
        
    st_tax = get_user_deduction('State Taxes', gross_pay, deductions)
    deductions += st_tax
    # display_running_total(deductions)

    fed_tax = get_user_deduction('Federal Taxes', gross_pay, deductions)
    deductions += fed_tax
    # display_running_total(deductions)

    fica_witholdings = get_user_deduction('Fica Witholdings', gross_pay, deductions)
    deductions += fica_witholdings

    print('=============================================')
    print(f"Employee ID:\t\t{employee_id}")
    print(f"Gross pay: \t\t\t${format(gross_pay, '.2f')}")
    print(f"State taxes; \t\t${format(st_tax, '.2f')}")
    print(f"Federal taxes: \t\t${format(fed_tax, '.2f')}")
    print(f"Fica Witholdings: \t${format(fica_witholdings, '.2f')}")
    print(f"Net pay: \t\t\t${format(gross_pay - deductions, '.2f')}")
    print('=============================================\n')


my_app() # run application 