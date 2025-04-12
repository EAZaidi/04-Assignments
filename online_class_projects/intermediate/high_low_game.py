import streamlit as st
import random

# Constants
NUM_ROUNDS = 5

# Initialize session state variables
if "round" not in st.session_state:
    st.session_state.round = 1
    st.session_state.your_score = 0
    st.session_state.game_over = False
    st.session_state.your_num = random.randint(1, 100)
    st.session_state.computer_num = random.randint(1, 100)

# Game Header
st.title("🎮 High-Low Game")
st.write("Welcome to the High-Low Game! Try to guess if your number is **higher** or **lower** than the computer's.")

# Show round info
st.subheader(f"Round {st.session_state.round} of {NUM_ROUNDS}")
st.write(f"**Your number:** {st.session_state.your_num}")

# Game Logic
if not st.session_state.game_over:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📈 Higher"):
            guess = "higher"
            is_correct = st.session_state.your_num > st.session_state.computer_num
            st.session_state.round += 1
            st.session_state.your_score += int(is_correct)

    with col2:
        if st.button("📉 Lower"):
            guess = "lower"
            is_correct = st.session_state.your_num < st.session_state.computer_num
            st.session_state.round += 1
            st.session_state.your_score += int(is_correct)

    if "guess" in locals():  # Checks if a guess was made
        if is_correct:
            st.success(f"✅ You were right! The computer's number was **{st.session_state.computer_num}**")
        else:
            st.error(f"❌ Incorrect! The computer's number was **{st.session_state.computer_num}**")

        # Generate new numbers for the next round
        if st.session_state.round <= NUM_ROUNDS:
            st.session_state.your_num = random.randint(1, 100)
            st.session_state.computer_num = random.randint(1, 100)
        else:
            st.session_state.game_over = True

# Final Score and Restart Option
if st.session_state.game_over:
    st.subheader(f"🎉 Game Over! Your Final Score: {st.session_state.your_score}/{NUM_ROUNDS}")

    if st.session_state.your_score == NUM_ROUNDS:
        st.success("🏆 Wow! You played **perfectly!**")
    elif st.session_state.your_score >= NUM_ROUNDS // 2:
        st.info("👏 Good job, you played really well!")
    else:
        st.warning("🤔 Better luck next time!")

    if st.button("🔄 Play Again"):
        st.session_state.round = 1
        st.session_state.your_score = 0
        st.session_state.game_over = False
        st.session_state.your_num = random.randint(1, 100)
        st.session_state.computer_num = random.randint(1, 100)
        st.rerun()
