import streamlit as st

from streamlit import subheader

from savingsaccount import balance, limit
from savingsaccount import Savingsaccount

st.set_page_config(page_title = "SavingsAcct", layout = "centered")
st.header('Savings Account')
st.subheader('Set withdraw limit = 20,000(Twenty Thousand Dollars)')
savings = Savingsaccount(200000)



if 'account' not in st.session_state:
    st.session_state.account = Savingsaccount(balance= 100000)

balance_placeholder = st.empty()
balance_placeholder.subheader(f"Balance: ${st.session_state.account.balance}")


with st.form("savings_form"):
    amount = st.number_input("Enter Amount",min_value=1000, step=100)
    operations = st.selectbox("Deposit or Withdraw", ("Deposit","Withdraw"))
    sumbit = st.form_submit_button("Sumbit")


if sumbit and operations:
       try:
           if amount < limit and operations == "Withdraw":
               with st.spinner('Processing...'):
                st.session_state.account.withdraw(amount)
                savings.withdraw(amount, limit=20000)
                st.success(f"You successfully withdrew ${amount:} from your savings account")
                balance_placeholder.subheader(f"Balance: ${st.session_state.account.balance}")

           elif sumbit and operations == "Deposit":
              with st.spinner("Processing..."):
                st.session_state.account.deposit(amount)
                savings.deposit(amount)
                st.success(f"${amount:} deposited successfully.")
                balance_placeholder.subheader(f"Balance: ${st.session_state.account.balance}")

           else:
                with st.spinner('Processing...'):

                    savings.withdraw(amount, limit=20000)
                    st.success(f"${amount:} exceeds your set withdraw limit")
                    balance_placeholder.subheader(f"Balance: ${st.session_state.account.balance}")

       except ValueError as e:
          st.error(str(e))




