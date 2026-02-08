import streamlit as st
import random

st.title("Rock Paper Scissors Game")
st.write("Select one option")

choices = ["rock", "paper", "scissors"]

# Layout: 3 columns
col1, col2, col3 = st.columns(3)

user_choice = None

with col1:
    st.image("images/rock.png", width=120)
    if st.button("Rock"):
        user_choice = "rock"

with col2:
    st.image("images/paper.png", width=120)
    if st.button("Paper"):
        user_choice = "paper"

with col3:
    st.image("images/scissors.png", width=120)
    if st.button("Scissors"):
        user_choice = "scissors"

# Game logic
if user_choice:
    computer_choice = random.choice(choices)

    st.write(f"🧠 Computer chose: **{computer_choice}**")
    st.write(f"🧑 You chose: **{user_choice}**")

    if user_choice == computer_choice:
        st.success("It's a Draw 😐")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        st.success("🎉 Yay! You Win!")
        st.balloons()

    else:
        st.error("😢 You Lose! Try Again")