import streamlit as st
import streamlit.config

from currentaccount import currentaccount
from pages.savings_Account import operations, sumbit
from savingsaccount import balance

if 'account' not in st.session_state:
    st.session_state.account = currentaccount(balance= 100000)
st.set_page_config(page_title="Current Account", layout = "centered")
st.title("Current Account")

balance_placeholder = st.empty()
balance_placeholder.subheader(f"Balance: ${st.session_state.account.balance}")
with st.form("current_account_form"):
    amount = st.number_input("Enter amount",min_value=1000, step=100)
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    sumbit = st.form_submit_button("Sumbit")

    if sumbit:
        try:
            if operations == "Deposit":
                st.session_state.account.deposit(amount)
                st.success(f"Successfuly Depositted ${amount}")
            # add elif statement here for withdraw function
            elif operations == "Withdraw":
                st.session_state.account.withdraw(amount)
                st.success(f"Successfully Withdrew ${amount}!")
            balance_placeholder.subheader(f"Balance: ${st.session_state.account.balance}")
        except ValueError as e:
            st.error(str(e))