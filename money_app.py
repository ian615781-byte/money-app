import streamlit as st
from questions import get_profile
from ideas import generate_ideas
from tracker import show_tracker
from course import get_course
from places import get_places

CASH_APP_LINK = "https://cash.app/$iangriffin18"

st.set_page_config(page_title="First $100 Mission", page_icon="💸", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.big-title {
    font-size: 48px;
    font-weight: 900;
}
.subtitle {
    font-size: 20px;
    color: #555;
}
.card {
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #eee;
    background: #fff;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "profile" not in st.session_state:
    st.session_state.profile = None

if "ideas" not in st.session_state:
    st.session_state.ideas = None

if "selected_idea" not in st.session_state:
    st.session_state.selected_idea = None

if "paid" not in st.session_state:
    st.session_state.paid = False

# ---------------- LANDING ----------------
if st.session_state.profile is None:

    st.markdown('<div class="big-title">Make your first $100.</div>', unsafe_allow_html=True)

    st.markdown("""
This is not motivation.

This is a system.

You will:
- Get a real way to make money based on YOU
- Get exact steps to follow
- Get scripts to get your first customer
- Start this week

If you follow this, you can make money.
""")

    st.markdown("""
### 💥 Real Examples

- Made $30 in 2 days doing yard work  
- Got first client from Instagram DMs  
- Turned 1 job into 3 repeat customers  

This works if you actually do it.
""")

    st.warning("If you don’t take action, nothing changes.")

    profile = get_profile(st)

    if st.button("Start My $100 Mission"):
        if len(profile["skills"]) == 0:
            st.warning("Pick at least one skill")
        else:
            st.session_state.profile = profile
            st.session_state.ideas = generate_ideas(profile)
            st.rerun()

# ---------------- PICK IDEA ----------------
elif st.session_state.selected_idea is None:

    st.header("Pick your path")

    for idea in st.session_state.ideas:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader(idea["name"])
        st.write(idea["why"])
        st.write("Start cost:", idea["cost"])
        st.write("Goal:", idea["first_goal"])

        if st.button(f"Start {idea['name']}", key=idea["name"]):
            st.session_state.selected_idea = idea
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- MAIN ----------------
else:
    idea = st.session_state.selected_idea
    course = get_course(idea["name"])

    st.header(idea["name"])

    st.markdown("""
### 🧠 Your Mission

Follow the steps.
Take action.
Make money.

This only works if you do the work.
""")

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Daily Plan", "Scripts", "Tracker"])

    # -------- OVERVIEW --------
    with tab1:
        st.subheader("What you’re doing")
        st.write(idea["explanation"])

        st.subheader("Where to get customers")
        for p in get_places(idea["name"]):
            st.write("- " + p)

    # -------- DAILY PLAN --------
    with tab2:
        for d in course["days"]:
            st.subheader(f"Day {d['day']}")
            st.write(d["lesson"])
            st.success(d["action"])

    # -------- SCRIPTS --------
    with tab3:
        if not st.session_state.paid:
            st.markdown("""
### 🔓 Unlock Full System

Get:
- Exact messages to send
- Real scripts that get customers
- The fastest way to make your first $100

One-time: $5
""")

            st.link_button("Pay $5", CASH_APP_LINK)

            if st.button("I Paid - Unlock"):
                st.session_state.paid = True
                st.rerun()

        else:
            for d in course["days"]:
                st.write(d["script"])

    # -------- TRACKER --------
    with tab4:
        if not st.session_state.paid:
            st.markdown("Unlock tracker after payment")
            st.link_button("Pay $5", CASH_APP_LINK)

            if st.button("I Paid - Unlock Tracker"):
                st.session_state.paid = True
                st.rerun()

        else:
            show_tracker(st, idea)
