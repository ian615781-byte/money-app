import streamlit as st
from questions import get_profile
from ideas import generate_ideas
from course import get_course
from places import get_places
from daily_schedule import get_daily_schedule
from ai_coach import ask_ai

CASH_APP_LINK = "https://cash.app/$iangriffin18"

st.set_page_config(page_title="7 Day $100 Challenge", page_icon="💸", layout="wide")

# ---------- STATE ----------
if "profile" not in st.session_state:
    st.session_state.profile = None
if "ideas" not in st.session_state:
    st.session_state.ideas = None
if "selected_idea" not in st.session_state:
    st.session_state.selected_idea = None
if "current_day" not in st.session_state:
    st.session_state.current_day = 1
if "money_made" not in st.session_state:
    st.session_state.money_made = 0
if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = []
if "coach_chat" not in st.session_state:
    st.session_state.coach_chat = []

st.title("🔥 HustlePath")
st.error("Most people stay broke because they don’t know what to do. This tells you exactly what to do starting today.")
st.success("Real examples:\n- Made $30 in 2 days doing yard work\n- Got first client from Instagram DMs\n- Turned 1 job into repeat customers")
st.warning("You have 7 days to make your first $100. Follow the plan exactly.")

# ---------- START ----------
if st.session_state.profile is None:
    st.header("Start Here")

    profile = get_profile(st)

    if st.button("Build My $100 Plan", use_container_width=True):
        if len(profile["skills"]) == 0:
            st.warning("Pick at least one skill.")
        else:
            st.session_state.profile = profile
            st.session_state.ideas = generate_ideas(profile)
            st.rerun()

# ---------- PICK IDEA ----------
elif st.session_state.selected_idea is None:
    st.header("Choose Your Money Path")

    for idea in st.session_state.ideas:
        with st.container(border=True):
            st.subheader(idea["name"])
            st.write(f"**Why this fits:** {idea['why']}")
            st.write(f"**Starting cost:** {idea['cost']}")
            st.write(f"**First goal:** {idea['first_goal']}")

            if st.button(f"Start {idea['name']}", key=idea["name"], use_container_width=True):
                st.session_state.selected_idea = idea
                st.rerun()

# ---------- MAIN APP ----------
else:
    idea = st.session_state.selected_idea
    course = get_course(idea["name"])

    completed = len(st.session_state.completed_tasks)
    total = 35

    st.header(idea["name"])
    st.progress(min(completed / total, 1.0))
    st.write(f"Mission progress: {completed}/{total} tasks completed")
    st.write(f"Money made: **${st.session_state.money_made}** / $100")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Overview",
        "Today’s Plan",
        "Ask Coach",
        "Premium Scripts 🔒",
        "Tracker"
    ])

    with tab1:
        st.subheader("What you are doing")
        st.write(idea["explanation"])

        st.subheader("Why this can work")
        st.write(idea["why"])

        st.subheader("Where to find customers")
        for place in get_places(idea["name"]):
            st.write("- " + place)

        st.subheader("How this can become full-time")
        for step in idea["full_time_path"]:
            st.write("- " + step)

    with tab2:
        st.subheader(f"Day {st.session_state.current_day}: Full Daily Plan")

        day_data = course["days"][st.session_state.current_day - 1]

        st.write("### Main Goal")
        st.success(day_data["goal"])

        st.write("### Why this matters")
        st.info("This step matters because money comes from action. Every message, offer, and follow-up gives you proof.")

        st.write("### Main Lesson")
        st.write(day_data["lesson"])

        st.write("### Main Action")
        st.success(day_data["action"])

        st.write("### Schedule for today")
        schedule = get_daily_schedule(idea["name"], st.session_state.current_day)

        for time, task in schedule:
            key = f"day_{st.session_state.current_day}_{time}_{task}"
            checked = st.checkbox(f"{time} — {task}", key=key)

            if checked and key not in st.session_state.completed_tasks:
                st.session_state.completed_tasks.append(key)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Previous Day", use_container_width=True):
                if st.session_state.current_day > 1:
                    st.session_state.current_day -= 1
                    st.rerun()

        with col2:
            if st.button("Next Day", use_container_width=True):
                if st.session_state.current_day < 7:
                    st.session_state.current_day += 1
                    st.rerun()

    with tab3:
        st.subheader("💬 Money Coach Chat")
        st.caption("Ask about clients, prices, messages, online business, or turning this into a real business.")

        if len(st.session_state.coach_chat) == 0:
            with st.chat_message("assistant"):
                st.write(
                    f"Hey 👋 I’m your coach for **{idea['name']}**. "
                    "Ask me what you’re stuck on, and I’ll help you take the next step."
                )

        for chat in st.session_state.coach_chat:
            with st.chat_message("user"):
                st.write(chat["question"])

            with st.chat_message("assistant"):
                st.write(chat["answer"])

        question = st.chat_input("Ask your money coach...")

        if question:
            answer = ask_ai(
                question,
                idea["name"],
                st.session_state.coach_chat
            )

            st.session_state.coach_chat.append({
                "question": question,
                "answer": answer
            })

            st.rerun()

        if st.button("Clear Chat", key="clear_chat_button"):
            st.session_state.coach_chat = []
            st.rerun()

    with tab4:
        st.subheader("Premium Scripts")
        st.warning("Premium scripts are locked.")

        st.write("""
Premium gives you:
- exact messages to send customers
- follow-up messages
- pricing scripts
- what to say when someone says no

Price: $5 one-time.
""")

        st.link_button("Pay $5 with Cash App", CASH_APP_LINK, use_container_width=True)

        st.info("After paying, send proof of payment to $iangriffin18. Access is manual for now.")

    with tab5:
        st.subheader("Money Tracker")

        money = st.number_input("Add money made", min_value=0, step=1)

        if st.button("Add Money", use_container_width=True):
            st.session_state.money_made += money
            st.rerun()

        st.write(f"Total money made: ${st.session_state.money_made}")

        if st.session_state.money_made >= 25:
            st.success("Level 1: You made your first $25.")
        else:
            st.info("Level 1 goal: Make your first $25.")

        if st.session_state.money_made >= 50:
            st.success("Level 2: You are halfway to $100.")
        else:
            st.info("Level 2 goal: Reach $50.")

        if st.session_state.money_made >= 100:
            st.success("Level 3: You hit your first $100.")
        else:
            st.info("Level 3 goal: Reach $100.")

        if st.button("Reset App"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
