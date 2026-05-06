def get_profile(st):
    st.header("Tell us about you")

    age = st.selectbox(
        "Age range",
        ["Under 13", "13-15", "16-18", "18+"],
    )

    skills = st.multiselect(
        "What skills do you already have?",
        [
            "Sports",
            "Cleaning",
            "Yard work",
            "Babysitting",
            "Tutoring",
            "Social media",
            "Gaming",
            "Cooking",
            "Drawing/design",
            "Fixing things",
            "Talking to people",
            "Selling",
        ],
    )

    time = st.selectbox(
        "How much time can you work each week?",
        ["1-3 hours", "4-7 hours", "8-15 hours", "15+ hours"],
    )

    money = st.selectbox(
        "How much money can you start with?",
        ["$0", "$1-$20", "$21-$50", "$50+"],
    )

    goal = st.selectbox(
        "What is your first money goal?",
        ["Make $25", "Make $50", "Make $100", "Make $250"],
    )

    comfort = st.selectbox(
        "Are you comfortable talking to people?",
        ["Yes", "A little", "No"],
    )

    location_type = st.selectbox(
        "Do you want online or in-person ideas?",
        ["Either", "Online", "In-person"],
    )

    transportation = st.selectbox(
        "Do you have transportation?",
        ["Yes", "Sometimes", "No"],
    )

    fast_or_long = st.selectbox(
        "What do you want more?",
        ["Fast cash", "Long-term business", "Both"],
    )

    if age != "18+":
        st.info("If you are under 18, ask a parent or guardian before meeting customers, accepting payments, or doing in-person work.")

    return {
        "age": age,
        "skills": skills,
        "time": time,
        "money": money,
        "goal": goal,
        "comfort": comfort,
        "location_type": location_type,
        "transportation": transportation,
        "fast_or_long": fast_or_long,
    }
