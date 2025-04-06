import streamlit as st 
from libs import Jomblo, Member

st.title("Jomblo Management System")

if "jomblo" not in st.session_state:
    st.session_state.jomblo = Jomblo("Jomblo Membership")

page = st.sidebar.selectbox("Menu", ["Add Member", "Manage Membership", "View Members"])

if page == "Add Member":
    st.write("### Add Member")
    name = st.text_input("Name")
    button = st.button("Add Member")
    
    if button:
        new_member = Member(name)
        st.session_state.jomblo.register_member(new_member)
        # st.success(f"Member {name} added successfully")
        st.rerun()
    
elif page == "Manage Membership":
    st.write("### Manage Membership")
    
    for index, member in enumerate(st.session_state.jomblo.members):
        status = "Single / Jomblo" if member.is_active else "In Relationship"
        st.write(f"{member.name} - {status}")
        deactivate_btn = st.button("In Relationship", key=f"deactivate_{index}")
        
        if deactivate_btn:
            member.deactivate()
            st.rerun()
            
elif page == "View Members":
    if not st.session_state.jomblo.members:
        st.write("No current single / jomblo members")
    else:
        active_members = st.session_state.jomblo.get_active_members()
        for member in active_members:
            st.write(member.name)
    
print(st.session_state.jomblo.members)