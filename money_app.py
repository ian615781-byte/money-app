import streamlit as st
from questions import get_profile
from ideas import generate_ideas
from course import get_course
from places import get_places
from daily_schedule import get_daily_schedule
from ai_coach import ask_ai

CASH_APP_LINK = "https://cash.app/$iangriffin18"

st.set_page_config(
    page_title="HustlePath",
    page_icon="🔥",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 52px;
    font-weight: 900;
    line-height: 1.05;
}
.sub-title {
    font-size: 20px;
    color: #555;
    margin-bottom: 20px;
}
.hero-card {
    padding: 24px;
    border-radius: 22px;
    background: linear-gradient(135deg, #fff7e6, #ffffff);
    border: 1px solid #f1d18a;
    box-shadow: 0 6px 20px rgba(0,0,0,0.07);
    margin-bottom: 18px;
}
.card {
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #e8e8e8;
    background: white;
    box-shadow: 0 4px 14px rgba(0,0,0,0.05);
    margin-bottom: 16px;
}
.metric-box {
    padding: 16px;
    border-radius: 16px;
    background: #f7f7f7;
    text-align: center;
}
.locked-box {
    padding: 22px;
    border-radius: 18px;
    background: #fff3cd;
    border: 1px solid #ffd36b;
}
@media (max-width: 768px) {
    .main-title {
        font-size: 36px;
    }
    .sub-title {
        font-size: 16px;
    }
}
</style>
""", unsafe_allow_html=True)

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

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("🔥 HustlePath")

    if st.session_state.selected_idea:
        st.write(f"Path: **{st.session_state.selected_idea['name']}**")
        st.write(f"Day: **{st.session_state.current_day}/7**")
        st.write(f"Money: **${st.session_state.money_made}/$100**")
    else:
        st.write("Build your first money plan.")

    st.divider()

    st.write("Free:")
    st.write("✅ quiz")
    st.write("✅ daily plan")
    st.write("✅ coach")
    st.write("✅ tracker")

    st.write("Premium:")
    st.write("🔒 scripts")
    st.write("🔒 follow-ups")
    st.write("🔒 sales help")

    st.divider()

    if st.button("Reset App"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ---------- START ----------
if st.session_state.profile is None:
    left, right = st.columns([1.2, 1])

    with left:
        st.markdown('<div class="main-title">Turn your skills into your first $100.</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="sub-title">HustlePath gives beginners a realistic money path, daily actions, customer ideas, and a coach to help them start.</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="hero-card">
        <h3>🔥 7 Day $100 Challenge</h3>
        <p>Most people stay stuck because they don’t know what to do first. HustlePath gives you the next move.</p>
        <ul>
            <li>Pick your skills</li>
            <li>Get matched with a money path</li>
            <li>Follow a daily plan</li>
            <li>Ask the coach when stuck</li>
            <li>Track your first $100</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        colA, colB, colC = st.columns(3)
        with colA:
            st.markdown('<div class="metric-box"><b>7 Days</b><br>guided plan</div>', unsafe_allow_html=True)
        with colB:
            st.markdown('<div class="metric-box"><b>$100</b><br>first goal</div>', unsafe_allow_html=True)
        with colC:
            st.markdown('<div class="metric-box"><b>Coach</b><br>built in</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.header("Start Here")
        profile = get_profile(st)

        if st.button("Build My HustlePath", use_container_width=True):
            if len(profile["skills"]) == 0:
                st.warning("Pick at least one skill.")
            else:
                st.session_state.profile = profile
                st.session_state.ideas = generate_ideas(profile)
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- PICK IDEA ----------
elif st.session_state.selected_idea is None:
    st.markdown('<div class="main-title">Choose your path.</div>', unsafe_allow_html=True)
    st.write("Pick the one that feels realistic for you to start this week.")

    for idea in st.session_state.ideas:
        with st.container(border=True):
            st.subheader(idea["name"])
            st.write(f"**Match score:** {idea.get('score', 0)}/100")
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
    progress = min(completed / total, 1.0)

    st.markdown(f'<div class="main-title">{idea["name"]}</div>', unsafe_allow_html=True)
    st.write("Your 7-day money mission.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="metric-box"><b>{completed}/{total}</b><br>tasks done</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-box"><b>${st.session_state.money_made}</b><br>made so far</div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-box"><b>Day {st.session_state.current_day}</b><br>current mission</div>', unsafe_allow_html=True)

    st.progress(progress)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Overview",
        "Today",
        "Coach",
        "Premium 🔒",
        "Tracker"
    ])

    with tab1:
        st.subheader("What you are doing")
        st.write(idea["explanation"])

        st.subheader("Why this can work")
        st.write(idea["why"])

        st.subheader("Where to find customers")
        for place in get_places(idea["name"]):
            st.write("✅ " + place)

        st.subheader("How this can become full-time")
        for step in idea["full_time_path"]:
            st.write("→ " + step)

    with tab2:
        day_data = course["days"][st.session_state.current_day - 1]

        st.subheader(f"Day {st.session_state.current_day}: {day_data['goal']}")

        st.info("Money comes from action. Today’s job is to move one step closer to a real customer.")

        st.write("### Lesson")
        st.write(day_data["lesson"])

        st.write("### Main Action")
        st.success(day_data["action"])

        st.write("### Schedule")
        schedule = get_daily_schedule(idea["name"], st.session_state.current_day)

        for time, task in schedule:
            key = f"day_{st.session_state.current_day}_{time}_{task}"
            checked = st.checkbox(f"{time} — {task}", key=key)

            if checked and key not in st.session_state.completed_tasks:
                st.session_state.completed_tasks.append(key)

        colA, colB = st.columns(2)

        with colA:
            if st.button("Previous Day", use_container_width=True):
                if st.session_state.current_day > 1:
                    st.session_state.current_day -= 1
                    st.rerun()

        with colB:
            if st.button("Next Day", use_container_width=True):
                if st.session_state.current_day < 7:
                    st.session_state.current_day += 1
                    st.rerun()

    with tab3:
        st.subheader("💬 Money Coach")
        st.caption("Ask about offers, messages, customers, prices, rejection, or turning this into a business.")

        if len(st.session_state.coach_chat) == 0:
            with st.chat_message("assistant"):
                st.write(f"Hey 👋 I’m your HustlePath coach for **{idea['name']}**. What are you stuck on?")

        for chat in st.session_state.coach_chat:
            with st.chat_message("user"):
                st.write(chat["question"])
            with st.chat_message("assistant"):
                st.write(chat["answer"])

        question = st.chat_input("Ask your coach...")

        if question:
            answer = ask_ai(question, idea["name"], st.session_state.coach_chat)

            st.session_state.coach_chat.append({
                "question": question,
                "answer": answer
            })

            st.rerun()

        if st.button("Clear Chat"):
            st.session_state.coach_chat = []
            st.rerun()

    with tab4:
        st.markdown("""
        <div class="locked-box">
        <h3>🔒 Premium Scripts</h3>
        <p>Unlock exact customer messages, follow-ups, pricing scripts, and what to say when people say no.</p>
        <p><b>Price:</b> $5 one-time</p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button("Pay $5 with Cash App", CASH_APP_LINK, use_container_width=True)

        st.info("After paying, send proof of payment to $iangriffin18. Access is manual for now.")

    with tab5:
        st.subheader("Money Tracker")

        money = st.number_input("Add money made", min_value=0, step=1)

        if st.button("Add Money", use_container_width=True):
            st.session_state.money_made += money
            st.rerun()

        st.write(f"Total money made: ${st.session_state.money_made}")

        if st.session_state.money_made >= 100:
            st.success("🔥 You hit your first $100.")
        elif st.session_state.money_made >= 50:
            st.success("Halfway there. Keep going.")
        elif st.session_state.money_made >= 25:
            st.success("First $25 made. That’s proof.")
        else:
            st.info("Goal 1: make your first $25.")
