# Pharmacy Management System - Version 2.0
# Feature: display medicine list, find medicine function, add medicine function

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

def addmed():
  newmed = input("Enter new medicine name : ")
  meds.append(newmed)
  for i in meds:
    print(i)

addmed()
