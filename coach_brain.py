def detect_problem(question):
    q = question.lower()

    if q in ["hi", "hello", "hey", "yo"]:
        return "greeting"

    if any(word in q for word in ["offer", "what am i selling", "what do i offer"]):
        return "offer"

    if any(word in q for word in ["message", "text", "dm", "say", "talk"]):
        return "message"

    if any(word in q for word in ["say no", "say np", "nope", "reject", "rejection", "not interested", "no thanks"]):
        return "rejection"

    if any(word in q for word in ["client", "customer", "first yes", "one yes"]):
        return "first_customer"

    if any(word in q for word in ["business", "buss", "long term", "full time"]):
        return "business"

    if any(word in q for word in ["price", "charge", "cost"]):
        return "pricing"

    if any(word in q for word in ["confused", "confuse", "stuck", "idk", "don't know"]):
        return "confused"

    return "general"


def get_offer_examples(idea_name):
    if "Tutoring" in idea_name or "Homework" in idea_name:
        return {
            "simple": "Homework help — $10 for 30 minutes.",
            "better": "I help younger students understand homework and get better grades with short tutoring sessions.",
            "people": "students, parents, younger kids, family friends, teachers"
        }

    if "Cleaning" in idea_name:
        return {
            "simple": "Small cleaning job — $20 this weekend.",
            "better": "I help people clean rooms, cars, garages, or small spaces for a cheap first price.",
            "people": "neighbors, parents, family friends, local people"
        }

    if "Video" in idea_name:
        return {
            "simple": "Short video edit — $10 per clip.",
            "better": "I help athletes, creators, and small businesses turn raw videos into short posts.",
            "people": "athletes, creators, small businesses, barbers, coaches"
        }

    if "Sports" in idea_name:
        return {
            "simple": "Beginner sports lesson — $10 for 30 minutes.",
            "better": "I help beginner athletes improve basic skills with short training sessions.",
            "people": "parents, younger athletes, coaches, teammates"
        }

    return {
        "simple": "Small local service — $10-$20.",
        "better": "I help people with simple tasks so they save time.",
        "people": "family, neighbors, friends, local people"
    }


def coach_response(question, idea_name, history):
    problem = detect_problem(question)
    examples = get_offer_examples(idea_name)

    if problem == "greeting":
        return f"""
Hey 👋 I’m here.

You picked **{idea_name}**.

Right now we’re trying to turn that into your first real money.

Tell me what you want help with:
- making the offer
- sending the message
- handling people saying no
- finding your first customer
- turning it into a business
"""

    if problem == "offer":
        return f"""
Good. Let’s build your offer.

Use this formula:

**I help [person] get [result] by doing [service].**

For **{idea_name}**, your offer can be:

"{examples['better']}"

Simple version:

"{examples['simple']}"

Now your next move:
Pick ONE specific thing you will offer first.

Do not offer everything.
Start small so people understand it fast.

What do you want your first offer to be?
"""

    if problem == "message":
        return f"""
Here is a simple message you can send:

"Hey, I’m trying to make my first $100 by doing {idea_name.lower()}. I’m starting cheap so I can build proof. Do you know anyone who might need help?"

If you want it more direct:

"Hey, I’m offering {examples['simple']} Do you know anyone who would want to try it?"

Send it to:
{examples['people']}

Your mission:
Send it to 3 people first.

If they say yes, I’ll help you with what to say next.
"""

    if problem == "rejection":
        return f"""
That is normal. People saying no does NOT mean the idea is bad.

Usually one of these is happening:

1. The offer is too vague  
Make it specific.

2. The person does not need it  
Ask someone closer to the problem.

3. The price feels risky  
Make the first try cheap.

4. You stopped too early  
Most people need more than one ask.

Try this follow-up:

"No worries. I’m just trying to get my first few customers and build proof. If you know anyone who might need {idea_name.lower()}, send them my way."

Your goal is not for everybody to say yes.

Your goal is:
**5 asks → 1 maybe → 1 yes**

Now tell me:
Did they say no, or did they just not reply?
"""

    if problem == "first_customer":
        return f"""
To get your first customer for **{idea_name}**, start with warm people.

Do not start with random strangers.

Start with:
{examples['people']}

Step-by-step:

1. Pick 5 people.
2. Send the simple message.
3. Offer a cheap first try.
4. Follow up tomorrow.
5. If someone says maybe, make it easy.

Say:

"I can do the first one cheap so you can see if it helps."

Your next move:
Name 3 people you could ask.
"""

    if problem == "business":
        return f"""
To turn **{idea_name}** into a business, you need repeat customers.

Here is the path:

1. Get one paying customer.
2. Do a good job.
3. Ask them to come back weekly.
4. Ask for a referral.
5. Make a package.

Example package:
- one-time: $10-$20
- weekly: $40-$80/month
- small group or bundle: higher price

But do not jump too far yet.

Business starts with proof.

Your next move:
Get one person to try your offer once.
Then ask: "Do you want to do this weekly?"
"""

    if problem == "pricing":
        return f"""
For **{idea_name}**, start cheap.

Beginner pricing:

- First try: $10-$20
- After proof: $25-$40
- Repeat package: $50-$100/month
- Group/bundle: more later

Do not worry about charging high yet.

Your first goal is:
proof, confidence, and one happy customer.
"""

    if problem == "confused":
        return f"""
No problem. Let’s slow it down.

You only need to do 3 things:

1. Pick one simple offer  
Example: "{examples['simple']}"

2. Ask 3 people  
Start with people who know you.

3. Try to get one yes  
Not ten. Just one.

That is it.

What part feels confusing:
the offer, the message, or who to ask?
"""

    return f"""
I got you.

For **{idea_name}**, the next step depends on what you are stuck on.

Pick one:
- "help me make an offer"
- "help me write the message"
- "what if they say no"
- "how do I find customers"
- "how do I make this a business"

Ask me one of those and I’ll walk you through it.
"""


def ask_ai(question, idea_name, history):
    return coach_response(question, idea_name, history)
