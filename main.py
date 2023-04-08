import streamlit as st
import pandas as pd
import random

bi_dict = {
    "team_member": [
        "Neele",
        "Surya",
        "Fernanda",
        "Lilian",
        "Elizaveta",
        "Sushant",
        "Christian",
        "Alina",
        "Nived",
        "Mostafa",
        "Michael",
        "Tomas",
        "Wojciech",
        "Altar",
        "Britta",
        "Carina",
        "Sander",
        "Sabir",
        "Thibaud",
        "Tommy",
    ],
    "team_name": ["Customer Acquisition"] * 5
    + ["Fulfillment"] * 6
    + ["Core/Central"] * 9,
}

bi_df = pd.DataFrame.from_dict(bi_dict)


def filter_df(df: pd.DataFrame, key: str) -> list:
    if key == "All":
        return list(df["team_member"].unique())
    else:
        return list(df[df["team_name"] == key]["team_member"].unique())


st.title("Pick Next Moderator")
team_selection = st.sidebar.radio(
    "Select a team", ["All"] + list(bi_df.team_name.unique())
)

team_member_selection = st.sidebar.multiselect(
    "Select participating team members",
    filter_df(bi_df, team_selection),
    default=filter_df(bi_df, team_selection),
)

if st.button("Roll Next Moderator!"):
    st.header(f"Next Moderator: {random.choice(team_member_selection)}")
    st.balloons()
