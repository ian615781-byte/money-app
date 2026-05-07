def get_daily_schedule(idea_name, day):
    schedules = {
        1: [
            ("10:00 AM", "Pick the exact service you will offer."),
            ("11:00 AM", "Write your simple offer in one sentence."),
            ("1:00 PM", "Make a list of 10 people you can ask."),
            ("4:00 PM", "Send your first 3 messages."),
            ("7:00 PM", "Write down who replied and who did not."),
        ],
        2: [
            ("10:00 AM", "Improve your offer so it sounds clear and simple."),
            ("12:00 PM", "Send your offer to 5 more people."),
            ("3:00 PM", "Follow up with anyone who replied."),
            ("6:00 PM", "Set a price for your first job or session."),
            ("8:00 PM", "Plan tomorrow’s outreach."),
        ],
        3: [
            ("10:00 AM", "Message 5 new people."),
            ("1:00 PM", "Post your offer on social media or send it to a group chat."),
            ("4:00 PM", "Follow up with people who did not answer."),
            ("6:00 PM", "Try to book one real customer."),
            ("8:00 PM", "Write down what worked and what didn’t."),
        ],
        4: [
            ("10:00 AM", "Prepare for your first job/session."),
            ("12:00 PM", "Practice what you will say."),
            ("3:00 PM", "Do the job/session or schedule it."),
            ("6:00 PM", "Ask for feedback."),
            ("8:00 PM", "Ask if they want help again."),
        ],
        5: [
            ("10:00 AM", "Use your proof or experience from yesterday."),
            ("12:00 PM", "Message 10 more people."),
            ("3:00 PM", "Offer a simple deal for first-time customers."),
            ("6:00 PM", "Try to book another job/session."),
            ("8:00 PM", "Track your money and progress."),
        ],
        6: [
            ("10:00 AM", "Ask past customers for referrals."),
            ("12:00 PM", "Post or send proof of your work if allowed."),
            ("3:00 PM", "Follow up with warm leads."),
            ("6:00 PM", "Create a weekly offer."),
            ("8:00 PM", "Plan how to repeat this next week."),
        ],
        7: [
            ("10:00 AM", "Review your whole week."),
            ("12:00 PM", "Count money made and steps completed."),
            ("3:00 PM", "Decide what offer worked best."),
            ("6:00 PM", "Set next goal: $100, $250, or 5 customers."),
            ("8:00 PM", "Make your next 7-day plan."),
        ],
    }

    return schedules.get(day, schedules[1])
