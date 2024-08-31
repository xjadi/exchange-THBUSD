# THB to USD Investment Simulation

This project is a Streamlit web application that simulates two investment strategies for buying and selling USD using historical exchange rate data. The goal is to compare the costs and outcomes of these two strategies over a 10-month period.

## Investment Strategies Simulated:

1. **Strategy 1: Buy USD Monthly**  
   In this strategy, you buy a specified amount of USD each month at that month's exchange rate. After 10 months, all accumulated USD is sold using the exchange rate of the 10th month.

2. **Strategy 2: Buy USD in a Lump Sum in Month 10**  
   In this strategy, instead of buying USD monthly, you buy all the USD at once in the 10th month using that month’s exchange rate.

## Features of the App:
- Input the amount of USD to buy each month.
- View a summary of the THB spent and USD bought for each strategy.
- See a detailed table showing the exchange rates and THB spent for each month (in Strategy 1).
- Compare the total THB spent between the two strategies and see which strategy is more cost-effective.

## How to Run the App:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name``

2. **Install the Required Packages:**
You need to have Python installed. Then, install the necessary packages using:

```bash
Copy code
pip install streamlit pandas
```

Run the Streamlit App:
In the project directory, run:

```bash
Copy code
streamlit run app.py


Open the App in Your Browser:
Once the command runs, it will automatically open the app in your default web browser. If it doesn’t open automatically, you can access it at:

##Project Structure:
app.py: The main script that contains the Streamlit app code.
exchange_with_month_year.csv: The dataset used for exchange rates (ensure this file is in the same directory).

##Example Usage:
Enter the amount of USD you want to buy each month (default is 200 USD).
View the total THB spent and USD bought for both strategies.
Analyze the tables showing detailed monthly expenses and exchange rates.
Compare which strategy is more cost-effective based on the total THB spent.

##Data:
The data used for this simulation is contained in the exchange_with_month_year.csv file and represents historical THB to USD exchange rates.