def init_tracker(st):
    if "money_made" not in st.session_state:
        st.session_state.money_made = 0

    if "completed_steps" not in st.session_state:
        st.session_state.completed_steps = []

    if "streak" not in st.session_state:
        st.session_state.streak = 0

    if "mission_completed_today" not in st.session_state:
        st.session_state.mission_completed_today = False


def show_tracker(st, selected_idea):
    init_tracker(st)

    st.header("🔥 Mission Tracker")

    goal_amount = 100
    progress = min(st.session_state.money_made / goal_amount, 1.0)

    st.subheader("Money Progress")
    st.progress(progress)
    st.write(f"${st.session_state.money_made} / ${goal_amount}")

    money = st.number_input("Add money made", min_value=0, step=1)

    if st.button("Add Money", use_container_width=True):
        st.session_state.money_made += money
        st.success(f"Total money made: ${st.session_state.money_made}")

    st.divider()

    st.subheader("🔥 Daily Streak")

    if st.button("Mark today's mission complete", use_container_width=True):
        if not st.session_state.mission_completed_today:
            st.session_state.streak += 1
            st.session_state.mission_completed_today = True
            st.success("Mission completed. Streak increased.")
        else:
            st.info("You already completed today's mission.")

    st.write(f"Current streak: 🔥 {st.session_state.streak} days")

    st.divider()

    st.subheader("7-Day Mission Checklist")

    for step in selected_idea["steps"]:
        checked = st.checkbox(step, key=step)

        if checked and step not in st.session_state.completed_steps:
            st.session_state.completed_steps.append(step)

    st.write(f"Steps completed: {len(st.session_state.completed_steps)}/{len(selected_idea['steps'])}")

    st.divider()

    st.subheader("Levels")

    if st.session_state.money_made >= 25:
        st.success("Level 1 Complete: You made your first $25.")
    else:
        st.info("Level 1: Make your first $25.")

    if st.session_state.money_made >= 50:
        st.success("Level 2 Complete: You are halfway to $100.")
    else:
        st.info("Level 2: Reach $50.")

    if st.session_state.money_made >= 100:
        st.success("Level 3 Complete: You hit your first $100.")
    else:
        st.info("Level 3: Reach $100.")
