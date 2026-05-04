def generate_ideas(profile):
    skills = profile["skills"]
    comfort = profile["comfort"]
    location_type = profile["location_type"]
    transportation = profile["transportation"]
    fast_or_long = profile["fast_or_long"]

    ideas = []

    def add(name, why, cost, first_goal, explanation, steps, full_time_path, score):
        ideas.append({
            "name": name,
            "why": why,
            "cost": cost,
            "first_goal": first_goal,
            "explanation": explanation,
            "steps": steps,
            "full_time_path": full_time_path,
            "score": score,
        })

    if "Sports" in skills and location_type != "Online":
        score = 70
        if comfort in ["Yes", "A little"]:
            score += 10
        if transportation != "No":
            score += 10
        if fast_or_long in ["Long-term business", "Both"]:
            score += 10

        add(
            "Beginner Sports Lessons",
            "You already understand sports, and parents often pay for beginner help if it feels safe and simple.",
            "$0-$10",
            "$100",
            "You teach younger beginners one simple skill at a time. You do not need to be famous. You need to be clear, reliable, and helpful.",
            [
                "Pick one beginner skill you can teach.",
                "Write a simple offer.",
                "Ask coaches, parents, neighbors, or family friends.",
                "Offer a short first session.",
                "Teach one skill, not everything.",
                "Ask for feedback.",
                "Offer weekly lessons.",
            ],
            [
                "Get 1 student.",
                "Build to 3 weekly students.",
                "Raise price after proof.",
                "Start group lessons.",
                "Post training clips.",
                "Build a coaching brand.",
            ],
            score,
        )

    if "Cleaning" in skills and location_type != "Online":
        score = 65
        if transportation != "No":
            score += 15
        if fast_or_long in ["Fast cash", "Both"]:
            score += 10

        add(
            "Quick Cleaning Service",
            "Cleaning is direct: people understand it fast and may pay quickly.",
            "$0-$20",
            "$100",
            "You help with simple cleaning jobs like cars, garages, rooms, trash pickup, or organizing. Your first goal is proof and repeat customers.",
            [
                "Choose one simple cleaning service.",
                "Write one clear offer.",
                "Ask 10 people.",
                "Do one small job well.",
                "Take proof if allowed.",
                "Ask for a review.",
                "Offer repeat help.",
            ],
            [
                "Do 1 job.",
                "Get repeat customers.",
                "Create packages.",
                "Raise prices.",
                "Get helpers.",
                "Turn it into a local service business.",
            ],
            score,
        )

    if "Yard work" in skills and location_type != "Online":
        score = 65
        if transportation != "No":
            score += 15
        if fast_or_long in ["Fast cash", "Both"]:
            score += 10

        add(
            "Yard Help",
            "Yard work is local, simple, and people often need help fast.",
            "$0-$20",
            "$100",
            "You offer simple outdoor help like leaf cleanup, trash pickup, watering, or basic yard work.",
            [
                "Pick one yard service.",
                "Make a simple price.",
                "Ask neighbors or family friends.",
                "Do one job well.",
                "Take before/after photos if allowed.",
                "Ask if they need weekly help.",
                "Track money made.",
            ],
            [
                "Start with small jobs.",
                "Build repeat weekly customers.",
                "Bundle services.",
                "Raise prices.",
                "Hire help.",
                "Turn into a local yard service.",
            ],
            score,
        )

    if "Social media" in skills and location_type != "In-person":
        score = 75
        if fast_or_long in ["Long-term business", "Both"]:
            score += 15
        if comfort == "No":
            score += 5

        add(
            "Short Video Editing Help",
            "This works online and can grow into monthly clients.",
            "$0",
            "$100",
            "You help athletes, small businesses, or creators turn raw clips into short social media posts.",
            [
                "Choose who you want to help.",
                "Make 2 sample edits.",
                "Message 10 people.",
                "Offer one cheap first edit.",
                "Deliver quickly.",
                "Create a price list.",
                "Ask for weekly work.",
            ],
            [
                "Build a portfolio.",
                "Get 3 clients.",
                "Offer monthly packages.",
                "Raise prices.",
                "Outsource editing.",
                "Turn it into a small media agency.",
            ],
            score,
        )

    if "Tutoring" in skills:
        score = 70
        if comfort in ["Yes", "A little"]:
            score += 10
        if location_type != "In-person":
            score += 5

        add(
            "Homework Help / Tutoring",
            "If you understand one subject, you can help younger students and build trust with parents.",
            "$0",
            "$50",
            "You offer simple 30-minute help sessions in one subject. The key is being patient and prepared.",
            [
                "Pick one subject.",
                "Make a simple offer.",
                "Ask parents or students.",
                "Prepare 3 practice problems.",
                "Do a short first session.",
                "Ask what they need next.",
                "Offer weekly help.",
            ],
            [
                "Start with 1 student.",
                "Get weekly sessions.",
                "Raise price.",
                "Create worksheets.",
                "Offer group sessions.",
                "Turn it into tutoring business.",
            ],
            score,
        )

    if "Drawing/design" in skills and location_type != "In-person":
        score = 68
        if fast_or_long in ["Long-term business", "Both"]:
            score += 10

        add(
            "Simple Logo / Flyer Design",
            "People need basic designs for small businesses, teams, and events.",
            "$0",
            "$100",
            "You create simple flyers, profile pictures, logos, or social posts using free design tools.",
            [
                "Make 3 sample designs.",
                "Choose a simple service.",
                "Message 10 small pages or teams.",
                "Offer one cheap design.",
                "Deliver a clean file.",
                "Ask to use it as proof.",
                "Create a price list.",
            ],
            [
                "Build a portfolio.",
                "Sell small designs.",
                "Make bundles.",
                "Raise prices.",
                "Offer monthly design help.",
                "Turn it into a design service.",
            ],
            score,
        )

    if len(ideas) == 0:
        add(
            "Local Errand Helper",
            "This works even if you do not have a special skill yet.",
            "$0",
            "$50",
            "You help people with simple tasks like carrying things, organizing, cleaning, or errands. The key is being safe, reliable, and clear.",
            [
                "Pick one simple task.",
                "Write one clear offer.",
                "Ask 10 trusted people.",
                "Do one small job.",
                "Track money made.",
                "Ask for repeat work.",
                "Raise your goal.",
            ],
            [
                "Start with small jobs.",
                "Find repeat customers.",
                "Pick the best service.",
                "Make flyers or posts.",
                "Raise prices.",
                "Turn it into a local service business.",
            ],
            50,
        )

    ideas = sorted(ideas, key=lambda x: x["score"], reverse=True)
    return ideas[:3]
