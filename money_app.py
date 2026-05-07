import streamlit as st
from questions import get_profile
from ideas import generate_ideas
from course import get_course
from places import get_places
from daily_schedule import get_daily_schedule
from coach import coach_answer

CASH_APP_LINK = "https://cash.app/$iangriffin18"

st.set_page_config(page_title="7 Day $100 Challenge", page_icon="💸", layout="wide")

if "profile" not in st.session_state:
    st.session_state.profile = None

if "ideas" not in st.session_state:
    st.session_state.ideas = None

if "selected_idea" not in st.session_state:
    st.session_state.selected_idea = None

if "paid" not in st.session_state:
    st.session_state.paid = False

if "current_day" not in st.session_state:
    st.session_state.current_day = 1

if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = []

if "money_made" not in st.session_state:
    st.session_state.money_made = 0

st.title("💸 7 Day $100 Challenge")
st.write("A daily money coach that tells you what to do, when to do it, what to say, and how to get your first customers.")

if st.session_state.profile is None:
    st.header("Start your challenge")
    profile = get_profile(st)

    if st.button("Build My $100 Plan", use_container_width=True):
        if len(profile["skills"]) == 0:
            st.warning("Pick at least one skill.")
        else:
            st.session_state.profile = profile
            st.session_state.ideas = generate_ideas(profile)
            st.rerun()

elif st.session_state.selected_idea is None:
    st.header("Pick your money path")

    for idea in st.session_state.ideas:
        with st.container(border=True):
            st.subheader(idea["name"])
            st.write(f"**Why this fits:** {idea['why']}")
            st.write(f"**Starting cost:** {idea['cost']}")
            st.write(f"**First goal:** {idea['first_goal']}")

            if st.button(f"Start {idea['name']}", key=idea["name"], use_container_width=True):
                st.session_state.selected_idea = idea
                st.rerun()

else:
    idea = st.session_state.selected_idea
    course = get_course(idea["name"])

    st.header(idea["name"])

    completed = len(st.session_state.completed_tasks)
    total = 35
    st.progress(min(completed / total, 1.0))
    st.write(f"Mission progress: {completed}/{total} tasks completed")
    st.write(f"Money made: **${st.session_state.money_made}** / $100")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Overview",
        "Today",
        "Coach Q&A",
        "Scripts 🔒",
        "Tracker"
    ])

    with tab1:
        st.subheader("What you’re doing")
        st.write(idea["explanation"])

        st.subheader("Where to get customers")
        for place in get_places(idea["name"]):
            st.write("- " + place)

        st.subheader("How this can become full-time")
        for step in idea["full_time_path"]:
            st.write("- " + step)

    with tab2:
        st.subheader(f"Day {st.session_state.current_day} Daily Schedule")

        day_data = course["days"][st.session_state.current_day - 1]

        st.write("### Main lesson")
        st.write(day_data["lesson"])

        st.write("### Main goal")
        st.success(day_data["action"])

        st.write("### Your schedule today")

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
        st.subheader("Ask the Money Coach")

        question = st.text_input("Ask a question like: What do I say? How much should I charge? Where do I find customers?")

        if st.button("Ask Coach", use_container_width=True):
            if question.strip() == "":
                st.warning("Type a question first.")
            else:
                answer = coach_answer(question, idea["name"])
                st.info(answer)

    with tab4:
        st.subheader("Copy-Paste Scripts")

        if not st.session_state.paid:
            st.warning("Scripts are locked. Unlock the full system for $5.")
            st.link_button("Pay $5 with Cash App", CASH_APP_LINK, use_container_width=True)
            st.info("After paying, send proof to $iangriffin18 for access.")
        else:
            for d in course["days"]:
                with st.expander(f"Day {d['day']}: {d['goal']}"):
                    st.write(d["script"])

    with tab5:
        st.subheader("Money Tracker")

        money = st.number_input("Add money made", min_value=0, step=1)

        if st.button("Add Money", use_container_width=True):
            st.session_state.money_made += money
            st.rerun()

        st.write(f"Total money made: ${st.session_state.money_made}")

        if st.button("Reset App"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
