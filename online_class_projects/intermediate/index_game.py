import streamlit as st

def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

# Initialize the list
fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']

# Streamlit Interface
st.title('List Practice Game')

# Display the current list
st.write(f"Current list: {fruit_lst}")

# Option to choose the operation
operation = st.selectbox(
    "Choose an operation",
    ["Access an element", "Modify an element", "Slice the list", "Add an element", "Get the length", "Print the list", "Quit"]
)

# Operation Logic
if operation == "Access an element":
    index = st.number_input("Enter index to access:", min_value=0, max_value=len(fruit_lst)-1, step=1)
    st.write(f"Accessed element: {access_element(fruit_lst, index)}")

elif operation == "Modify an element":
    index = st.number_input("Enter index to modify:", min_value=0, max_value=len(fruit_lst)-1, step=1)
    new_value = st.text_input("Enter new value:")
    if new_value:
        st.write(f"Updated list: {modify_element(fruit_lst, index, new_value)}")

elif operation == "Slice the list":
    start = st.number_input("Enter start index:", min_value=0, max_value=len(fruit_lst)-1, step=1)
    end = st.number_input("Enter end index:", min_value=start, max_value=len(fruit_lst), step=1)
    st.write(f"Sliced list: {slice_list(fruit_lst, start, end)}")

elif operation == "Add an element":
    new_item = st.text_input("Enter a fruit to add:")
    if new_item:
        fruit_lst.append(new_item)
        st.write(f"Updated list: {fruit_lst}")

elif operation == "Get the length":
    st.write(f"The length of the list is: {len(fruit_lst)}")

elif operation == "Print the list":
    st.write(f"Current list: {fruit_lst}")

elif operation == "Quit":
    st.write("Thanks for playing!")
