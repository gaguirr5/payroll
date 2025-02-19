# try except block will allow the user to keep the program from breaking, example if you put a letter in any float(input()), the program will break because it expects a number so it doesn't know what to do
# None can be useful to declare a variable without giving it a real value yet
# \n creates a new line, I use it for spacing
# \t adds a tab, I used this for spacing
# display_running_total is optional, depends if you want to let the user know as they go

# I used while loops at each input because we don't want to let the user continue inputting when they give an invalid input. 


def my_app():
    value_error_msg = 'Invalid input. Enter a valid number.'
    totals = {
          "updated": False,
          "gross_pay": 0.00,
          "st_tax": 0.00, 
          "fed_tax": 0.00,
          "fica_withholdings": 0.00,
          "deductions": 0.00
      }

  # Get user deductions
    def get_user_deduction(deduction_type, gross_pay, deduction_total):
      return_value = None
      while return_value is None:
          try:
              user_input = float(input(f"Enter {deduction_type} Amount: $"))
              if user_input > gross_pay:
                  print('Value cannot be higher than Gross Pay')
              elif user_input < 0:
                  print('Value cannot be negative')
              elif (deduction_total + user_input) > gross_pay:
                  print('Deductions cannot be higher than Gross Pay')
              else:
                  return_value = user_input
                  print('\n')
          except ValueError:
              print(value_error_msg)
      return return_value

    def payroll_report(totals):
      print('=============================================')
      print(f"Total Gross Pay: \t\t\t${format(totals['gross_pay'], '.2f')}")
      print(f"Total State Taxes: \t\t\t${format(totals['st_tax'], '.2f')}")
      print(f"Total Federal Taxes: \t\t${format(totals['fed_tax'], '.2f')}")
      print(f"Total FICA Withholdings: \t${format(totals['fica_withholdings'], '.2f')}")
      print(f"Total Net Pay: \t\t\t\t${format(totals['gross_pay'] - totals['deductions'], '.2f')}")
      print('=============================================\n')

    while True:
      employee_id = None
      deductions = 0.00

      while employee_id is None:
          try:
              employee_id = int(input('Enter Employee ID (0 to exit): '))
              if employee_id == 0:
                  if totals["updated"]:
                      payroll_report(totals)
                  print('Thank you for using the payroll system!')
                  return  # Exit program
          except ValueError:
              print(value_error_msg)

      gross_pay = None
      while gross_pay is None:
          try:
              gross_pay = float(input('Please Enter Gross Pay: $'))
              if gross_pay < 0:
                  print("Gross Pay can't be negative")
              else:
                  print('\n')
                  break
          except ValueError:
              print(value_error_msg)

      st_tax = get_user_deduction('State Taxes', gross_pay, deductions)
      deductions += st_tax

      fed_tax = get_user_deduction('Federal Taxes', gross_pay, deductions)
      deductions += fed_tax

      fica_withholdings = get_user_deduction('FICA Withholdings', gross_pay, deductions)
      deductions += fica_withholdings

      # Update totals
      totals["gross_pay"] += gross_pay
      totals["st_tax"] += st_tax
      totals["fed_tax"] += fed_tax
      totals["fica_withholdings"] += fica_withholdings
      totals["deductions"] += (st_tax + fed_tax + fica_withholdings)

      if not totals["updated"]:
          totals["updated"] = True


# Run application
my_app()
