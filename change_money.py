import pandas as pd
import streamlit as st

# Load the CSV data
df = pd.read_csv('exchange_with_month_year.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Filter data to start from January 2023
df_filtered = df[(df['Year'] == 2023) & (df['Month'] >= 1)]

# Group by 'Year' and 'Month' and calculate the average rate for each month
monthly_rates = df_filtered.groupby(['Year', 'Month'])['Rate'].mean().reset_index()

# Streamlit web application
st.title("THB to USD แลกเงินเข้าบัตร แล้ว แลกกลับเป็นเงินบาทเดือนที่ใช้")

# User input for the amount of USD to buy each month
usd_to_buy = st.number_input("ใส่เงินที่จะ dca แต่ลลเดือน:", min_value=1, value=200)

# Parameters
months = 10  # Number of months for the simulation

# Scenario 1: DCA USD ทุกเดือน ก่อนเดินทาง แล้วแลกกลับเป็นเงินบาท
usd_accumulated = 0
total_thb_spent_scenario1 = 0
thb_spent_table_scenario1 = []

for i in range(months):
    rate = monthly_rates.loc[i, 'Rate']
    thb_spent = usd_to_buy * rate
    usd_accumulated += usd_to_buy
    total_thb_spent_scenario1 += thb_spent
    thb_spent_table_scenario1.append({'Month': i + 1, 'Rate': rate, 'THB Spent': thb_spent})

# Sell all accumulated USD at the 10th month's rate
final_rate = monthly_rates.loc[months - 1, 'Rate']
thb_received_scenario1 = usd_accumulated * final_rate

# Scenario 2: Lump-sum purchase of USD for 10 months at once at the 10th month's rate
total_usd_to_buy_scenario2 = usd_to_buy * months
thb_spent_scenario2 = total_usd_to_buy_scenario2 * final_rate

# Table for Scenario 1
st.header("Scenario 1 - DCA USD ทุกเดือน ก่อนเดินทาง แล้วแลกกลับเป็นเงินบาท:")
st.write(f"Total THB ที่ใช้ซื้อ USD: {total_thb_spent_scenario1:.2f} THB")
st.write(f"THB ทั้งหมดที่ขายได้จาก USD: {thb_received_scenario1:.2f} THB")
st.write(f"Total USD ที่แลกคืนเดือนตุลา : {usd_accumulated:.2f} USD")
st.subheader("THB ที่ใช้ในการแลก (Scenario 1):")
st.table(pd.DataFrame(thb_spent_table_scenario1))

# Scenario 2 Table: Single purchase in month 10
thb_spent_table_scenario2 = [{'Month': 10, 'Rate': final_rate, 'THB Spent': thb_spent_scenario2}]

st.header("Scenario 2 - ซื้อทีเดียวเดือนตุลา หรือ เงินที่ต้องใช้ในเงินบาท:")
st.write(f"Total THB ที่ใช้ซื้อ USD: {thb_spent_scenario2:.2f} THB")
st.write(f"Total USD ที่ซื้อ: {total_usd_to_buy_scenario2:.2f} USD")
st.write(f"Total USD ที่แลกคืนเดือนตุลา: {total_usd_to_buy_scenario2:.2f} USD")
st.subheader("THB ที่ใช้ฟแลกในเดือนตุลา (Scenario 2):")
st.table(pd.DataFrame(thb_spent_table_scenario2))

# Comparison
st.subheader("เปรียบเทียบ:")
if total_thb_spent_scenario1 < thb_spent_scenario2:
    st.write(f"**Option 1 DCA USD ทุกเดือน ถูกกว่า {thb_spent_scenario2 - total_thb_spent_scenario1:.2f} THB.**")
else:
    st.write(f"**Option 2 ซื้อทีเดียวเดือนตุลาถูกกว่า {total_thb_spent_scenario1 - thb_spent_scenario2:.2f} THB.**")
