import streamlit as st
from questions import get_profile
from ideas import generate_ideas
from tracker import show_tracker
from course import get_course
from places import get_places

CASH_APP_LINK = "https://cash.app/$iangriffin18"

st.set_page_config(page_title="First $100 Mission", page_icon="💸", layout="wide")

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
.locked {
    padding: 20px;
    border-radius: 16px;
    background: #fff7e6;
    border: 1px solid #ffd27a;
}
</style>
""", unsafe_allow_html=True)

if "profile" not in st.session_state:
    st.session_state.profile = None

if "ideas" not in st.session_state:
    st.session_state.ideas = None

if "selected_idea" not in st.session_state:
    st.session_state.selected_idea = None

if "paid" not in st.session_state:
    st.session_state.paid = False

if st.session_state.profile is None:
    st.markdown('<div class="big-title">Make your first $100.</div>', unsafe_allow_html=True)

    st.write("""
This is not motivation.

This is a system.

You will:
- Get a real way to make money based on YOU
- Get exact steps to follow
- Get scripts to get your first customer
- Start this week

If you follow this, you can make money.
""")

    st.warning("If you don’t take action, nothing changes.")

    profile = get_profile(st)

    if st.button("Start My $100 Mission", use_container_width=True):
        if len(profile["skills"]) == 0:
            st.warning("Pick at least one skill")
        else:
            st.session_state.profile = profile
            st.session_state.ideas = generate_ideas(profile)
            st.rerun()

elif st.session_state.selected_idea is None:
    st.header("Pick your path")

    for idea in st.session_state.ideas:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader(idea["name"])
        st.write(idea["why"])
        st.write("Start cost:", idea["cost"])
        st.write("Goal:", idea["first_goal"])

        if st.button(f"Start {idea['name']}", key=idea["name"], use_container_width=True):
            st.session_state.selected_idea = idea
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

else:
    idea = st.session_state.selected_idea
    course = get_course(idea["name"])

    st.header(idea["name"])

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Daily Plan", "Scripts 🔒", "Tracker 🔒"])

    with tab1:
        st.subheader("What you’re doing")
        st.write(idea["explanation"])

        st.subheader("Where to get customers")
        for p in get_places(idea["name"]):
            st.write("- " + p)

    with tab2:
        for d in course["days"]:
            st.subheader(f"Day {d['day']}: {d['goal']}")
            st.write(d["lesson"])
            st.success(d["action"])

    with tab3:
        st.markdown("""
<div class="locked">
<h3>🔒 Scripts Locked</h3>
<p>Unlock exact copy-paste messages to send customers.</p>
<p><b>Price:</b> $5 one-time</p>
</div>
""", unsafe_allow_html=True)

        st.link_button("Pay $5 with Cash App", CASH_APP_LINK, use_container_width=True)

        st.info("After paying, send proof of payment to $iangriffin18. Then you can be given access to the full version.")

    with tab4:
        st.markdown("""
<div class="locked">
<h3>🔒 Tracker Locked</h3>
<p>Unlock the progress tracker, money tracker, streaks, and levels.</p>
<p><b>Price:</b> $5 one-time</p>
</div>
""", unsafe_allow_html=True)

        st.link_button("Pay $5 with Cash App", CASH_APP_LINK, use_container_width=True)

        st.info("After paying, send proof of payment to $iangriffin18. Then you can be given access to the full version.")
