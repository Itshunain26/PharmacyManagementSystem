# Pharmacy Management System - Version 1.1
# Feature: display medicine list, find medicine function

meds = ["Paracetamol", "Crocin", "Dolo"]

def printmed():
  for i in meds:
    print(i)
printmed()

def findmed():
  medtofind = input("Enter medicine name: ")
  if medtofind in meds:
    print("In Stock")
  else:
    print("Not Found")

findmed()
