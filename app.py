import streamlit as st
import pandas as pd
from database import get_balance, add_expense , init_db , get_all_expenses ,set_balance

# CSS Injection
st.markdown("""
    <style>
    /* Sirf us input par apply karo jiska label "Category" ho */
    div[data-baseweb="input"] input {
        text-transform: capitalize;
    }
    </style>
""", unsafe_allow_html=True)


# App ka basic setup
st.set_page_config(page_title="Aura Finance", layout="centered")
init_db()

st.title("💰 Aura Finance Tracker")

# Sidebar mein options
menu = st.sidebar.selectbox("Navigation", ["Dashboard", "Add Expense", "View History"])

if menu == "Dashboard":
    st.subheader("Current Balance")
    balance = get_balance()
    st.metric("Total Balance", f"₹{balance:.2f}")

    # Manual Update Section
    with st.expander("Update Balance Manually"):
        new_val = st.number_input("Enter New Total Balance", min_value=0.0)
        if st.button("Update"):
            set_balance(new_val)
            st.rerun() # Page refresh karne ke liye taaki naya balance dikhe

elif menu == "Add Expense":
    st.subheader("Add a New Expense")
    amt = st.number_input("Amount (₹)", min_value=0.0)
    cat = st.text_input("Category (e.g., Food, Travel)")
    
    if st.button("Save Expense"):
        add_expense(amt, cat)
        st.success(f"Expense of ₹{amt:.2f} added successfully!")

elif menu == "View History":
    st.subheader("Your Expense History")
    expenses = get_all_expenses()
    
    if expenses:
        df = pd.DataFrame(expenses, columns=["ID", "Amount", "Category", "Date"])
        
        # Format the 'Amount' column to 2 decimal places
        df['Amount'] = df['Amount'].map('{:.2f}'.format)
        
        st.table(df)
    else:
        st.write("No expenses found yet!")