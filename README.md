<h1>Banking Application</h1>

<p>
This is a simple banking application written in Python that allows users to perform various banking operations such as checking transaction history, withdrawing money, depositing money, and transferring money between accounts. Users can sign up for a new account or log in to an existing account.
</p>

<H3>Features</H3>
<p>
<ul>
1.Transaction History: View a history of all transactions performed.
2.Withdraw: Withdraw a specified amount of money from the account.
3.Deposit: Deposit a specified amount of money into the account.
4.Transfer: Transfer a specified amount of money to another account.
5.Quit: Exit the application.
</ul>
</p>

<h3>Requirements</h3>
<p>
Python 3.x
</p>

<h1>How to Use</h1>
<p>
<ul>
1.Clone the repository or download the code file to your local machine.
2. Ensure you have Python 3.x installed on your machine.
</ul>
</p>


<h3>Running the Application</h3>
1.Open a terminal or command prompt.
2.Navigate to the directory where the code file is located.
3.Run the application by executing the command

python banking_app.py

<h3>Application Flow</h3>
1.When you run the application, you will be prompted to either log in or sign up.
2.If you choose to sign up, you will be asked to set a username and a pin.
3.If you choose to log in, you will need to enter your username and pin.
4.Once logged in, you can choose from the following options:
   .Transaction History: View a list of all your past transactions.
   .Withdraw: Withdraw a specific amount of money from your account.
   .Deposit: Deposit a specific amount of money into your account.
   .Transfer: Transfer a specific amount of money to another user's account.
   .Quit: Exit the application.

<h3>Code Structure</h3>
list1: A list that stores tuples of usernames and pins.
dep_amount: A global variable that keeps track of the user's account balance.
history: A list that stores the transaction history.


<h3>Functions</h3>
starter(): Main menu function that provides options for different banking operations.
login(): Function for user login.
signup(): Function for new user signup.
deposit(): Function to deposit money into the account.
withdraw(): Function to withdraw money from the account.
transfer(): Function to transfer money to another account.
transaction_history(): Function to display the transaction history.
logfunc(): Initial function to prompt for login or signup.



<h2>Sample interaction<h2>
LOGIN******SIGNUPlogin or sign up 1/2: 2set a user name: Aliceset a pin: 1234sign up successful at 2024-06-17 12:34:56.789012**********choose the option number**********1. transaction history2. withdraw3. deposit4. transfer5. quitenter your desired service (use digits): 3enter your amount: 100you have 100.0 in your account**********choose the option number**********1. transaction history2. withdraw3. deposit4. transfer5. quit


<h2>
Notes
<h2>

Ensure you enter the correct username and pin when logging in.
When transferring money, make sure the recipient's account exists and you have sufficient balance.
Always choose options using digits as prompted.

<h2>
License
<h2>
This project is open-source and available under the MIT License.
  