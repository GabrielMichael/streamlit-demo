import streamlit as st
import pandas as pd
import random

BI_DICT = {
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

BI_DF = pd.DataFrame.from_dict(BI_DICT)


def filter_df(df: pd.DataFrame, key: str) -> list:
    if key == "All":
        return df["team_member"].unique().tolist()
    return df[df["team_name"] == key]["team_member"].unique().tolist()


def main():
    st.title("Pick Next Moderator")
    team_selection = st.sidebar.radio(
        "Select a team", ["All"] + BI_DF.team_name.unique().tolist()
    )

    team_member_selection = st.sidebar.multiselect(
        "Select participating team members",
        filter_df(BI_DF, team_selection),
        default=filter_df(BI_DF, team_selection),
    )

    if st.button("Roll Next Moderator!"):
        next_moderator = random.choice(team_member_selection)
        st.header(f"Next Moderator: {next_moderator}")
        st.balloons()


if __name__ == "__main__":
    main()
