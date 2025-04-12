import streamlit as st

# Gravitational constants as percentages of Earth gravity
GRAVITY_FACTORS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    st.title("🌌 Planetary Weight Calculator")

    st.markdown("""
    Enter your weight on Earth, select a planet from the list, and we'll tell you what you would weigh there!
    """)

    earth_weight = st.number_input("Enter your weight on Earth (kg):", min_value=0.0, step=0.1)

    planet = st.selectbox("Choose a planet:", list(GRAVITY_FACTORS.keys()))

    if st.button("Calculate"):
        planetary_weight = earth_weight * GRAVITY_FACTORS[planet]
        st.success(f"Your weight on **{planet}** would be **{round(planetary_weight, 2)} kg**")

if __name__ == "__main__":
    main()
