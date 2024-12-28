import streamlit as st
import pandas as pd
import os
PRICING_DATA = {
    "Kitchen Remodeling": {"price": 5000},
    "Bathroom Remodeling": {"price": 4000},
    "Flooring Installation": {"price": 3000},
    "Roofing": {"price": 8000},
    "Painting": {"price": 1500},
    "Electrical Work": {"price": 2000}
}
def save_submission(data):
    try:
        df = pd.DataFrame([data])
        if not os.path.exists("submissions.csv"):
            df.to_csv("submissions.csv", mode="w", header=True, index=False)
        else:
            df.to_csv("submissions.csv", mode="a", header=False, index=False)
    except Exception as e:
        st.error(f"Error saving submission: {e}")
def user_form():
    st.title("Cost Calculator")
    total_cost = 0
    selected_services = []

    st.subheader("Select Services:")
    for service, details in PRICING_DATA.items():
        if st.checkbox(f"{service} - ${details['price']}"):
            total_cost += details['price']
            selected_services.append(service)

    st.subheader(f"Total Cost: ${total_cost}")
    
    if st.button("Submit"):
        if selected_services:
            submission = {
                "Selected Services": ", ".join(selected_services),
                "Total Cost": total_cost
            }
            save_submission(submission)
            st.success("Your submission has been saved!")
        else:
            st.warning("Please select at least one service before submitting.")
def admin_panel():
    st.title("Admin Panel")
    updated_data = {}

    for service, details in PRICING_DATA.items():
        new_price = st.number_input(f"{service} - Current Price: ${details['price']}", value=details['price'])
        updated_data[service] = {"price": new_price}

    if st.button("Save Changes"):
        for service, details in updated_data.items():
            PRICING_DATA[service]["price"] = details["price"]
        st.success("Pricing updated successfully!")
def main():
    st.sidebar.title("Navigation")
    mode = st.sidebar.radio("Select Mode:", ["User Form", "Admin Panel"])

    if mode == "User Form":
        user_form()
    elif mode == "Admin Panel":
        admin_password = st.sidebar.text_input("Admin Password", type="password")
        if admin_password == "admin123": 
            admin_panel()
        else:
            st.sidebar.warning("Enter the correct admin password to access this section.")

if __name__ == "__main__":
    main()
