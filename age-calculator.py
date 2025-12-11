import streamlit as st
import datetime

st.title("Age Calculator")

# Date range
min_date = datetime.date(1900, 1, 1)
max_date = datetime.date.today()

st.subheader("Welcome here!!")

# Input DOB
dob = st.date_input("Enter your Date of Birth", min_value=min_date, max_value=max_date)

# Today's date
today = datetime.date.today()

if dob:
    # Calculate age
    age_years = today.year - dob.year
    age_months = today.month - dob.month
    age_days = today.day - dob.day

    # Adjust negative values
    if age_days < 0:
        age_months -= 1
        # Days in previous month
        previous_month = today.month - 1 or 12
        previous_year = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = (datetime.date(previous_year, previous_month % 12 + 1, 1) -
                              datetime.date(previous_year, previous_month, 1)).days
        age_days += days_in_prev_month

    if age_months < 0:
        age_years -= 1
        age_months += 12
# Button
cal = st.button("Calculate Age")

if cal:
    st.write("#### Your Age Is:")
    st.write(f"{age_years} years, {age_months} months, {age_days} days")
    st.success("Age calculated successfully!")

































# st.title("🎯 Age Calculator")

# # Date input for user date of birth
# min_date = datetime.date(2000, 1, 1)
# max_date = datetime.date(2100, 12, 31)
# default_date = datetime.date.today()
# dob = st.date_input("Enter your date of birth:", value=default_date, min_value=min_date, max_value=max_date, key=None)

# # Calculate age button
# if st.button("Calculate Age"):
#     today = datetime.date.today()

#     if dob > today:
#         st.error("❌ Date of birth cannot be in the future!")
#     else:
#         age_years = today.year - dob.year
#         age_months = today.month - dob.month
#         age_days = today.day - dob.day

#         # Adjust if current month/day is smaller than dob
#         if age_days < 0:
#             age_months -= 1
#             age_days += 30
#         if age_months < 0:
#             age_years -= 1
#             age_months += 12

#         st.success(f"🎉 Your Age is:  \n **{age_years} years, {age_months} months, {age_days} days**")

# st.write("---")
# st.write("Enter your DOB above and click the button to calculate your age 😉")




