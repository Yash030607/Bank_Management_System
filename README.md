# Bank_Management_System
This is a bank managment system.
I am using the csv module, random module, datetime module and the time module
The user can create an account and login
On logging in, the user can check their balance, make a deposit and a withdrawl
I have built in safegaurds to make sure creation of unique account number using the random module
I also check whether the mobile number entered is 10 digits or not
While logging in, the syytem checks whether the account exists in the database and whether the password matches
While making deposit or withdrawl, the system ensures that negative amount is not entered
On withdraw, it also makes sure that the withdrawl amunt is not greater than the balance
I am saving all the transactions in a csv file along with the date. To save the date I have used the datetime module
