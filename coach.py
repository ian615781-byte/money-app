def coach_answer(question, idea_name):
    q = question.lower()

    if "what do i say" in q or "message" in q or "text" in q:
        return (
            "Send this:\n\n"
            "'Hey, I’m starting a small service to help people with "
            f"{idea_name.lower()}. I’m trying to earn my first $100. "
            "Would you or someone you know need help this week?'"
        )

    if "price" in q or "charge" in q:
        return (
            "Start cheap so people say yes. Try $10-$25 for your first job/session. "
            "After you get proof and confidence, raise the price."
        )

    if "customer" in q or "find people" in q:
        return (
            "Start with people who already trust you: family, neighbors, parents, coaches, "
            "friends, local groups, or people who post online. Do not start with strangers first."
        )

    if "scared" in q or "nervous" in q:
        return (
            "That is normal. Your first goal is not to be perfect. Your first goal is to ask. "
            "Send 3 messages today. Even if nobody buys, you practiced."
        )

    if "no one" in q or "nobody" in q:
        return (
            "If nobody replies, change your offer. Make it clearer, cheaper, and easier to say yes to. "
            "Example: 'I can do one small job this week for $10.'"
        )

    if "full time" in q or "job" in q or "business" in q:
        return (
            "To turn this into a full-time job, you need repeat customers. "
            "First get 1 customer, then 3 repeat customers, then raise prices, then create packages."
        )

    return (
        "Here is the next best move: send your offer to 5 people today, track who replies, "
        "and follow up tomorrow. Making money starts with asking."
    )
