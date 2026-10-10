
from flask import Flask, render_template, request

app = Flask(__name__)

EMAILS = [
    {
        "title": "Urgent Account Verification",
        "sender": "security@example-training.test",
        "verdict": "Suspicious",
        "message": (
            "Your account requires immediate verification. "
            "Review the message carefully before taking action."
        ),
        "warning": (
            "Urgent language and requests to verify an account can "
            "be warning signs. Check the sender and use the official "
            "website instead of links in unexpected messages."
        ),
    },
    {
        "title": "Unexpected Prize Notification",
        "sender": "rewards@example-training.test",
        "verdict": "Suspicious",
        "message": (
            "This fictional message claims that you have won a prize "
            "and asks you to provide information to claim it."
        ),
        "warning": (
            "Unexpected prizes, requests for personal information, "
            "and pressure to act quickly should be treated cautiously."
        ),
    },
    {
        "title": "Routine Course Announcement",
        "sender": "courses@example-training.test",
        "verdict": "Review Normally",
        "message": (
            "Your course dashboard has a new announcement. "
            "Open your usual course portal to read it."
        ),
        "warning": (
            "A routine-looking message can still be spoofed. Verify "
            "the sender and visit your known course portal directly."
        ),
    },
]

QUESTIONS = [
    {
        "question": "What should you do with an unexpected email asking for your password?",
        "options": [
            "Reply with your password",
            "Verify through the official website or support channel",
            "Forward it to all your friends",
            "Trust it if the logo looks real",
        ],
        "answer": 1,
        "explanation": (
            "Never share your password by email. Visit the official "
            "website directly or contact the organization through a "
            "known, trusted channel."
        ),
    },
    {
        "question": "Which can be a warning sign of phishing?",
        "options": [
            "Unexpected urgency",
            "A request for sensitive information",
            "An unfamiliar or misleading sender address",
            "All of the above",
        ],
        "answer": 3,
        "explanation": (
            "Urgency, sensitive-information requests, and suspicious "
            "sender details can all indicate phishing."
        ),
    },
    {
        "question": "What is the safest way to open your bank website?",
        "options": [
            "Use a link in an unexpected email",
            "Click any shortened link",
            "Type its known address or use its official app",
            "Use a link sent by an unknown person",
        ],
        "answer": 2,
        "explanation": (
            "Use a known website address or the official app rather "
            "than following unexpected links."
        ),
    },
    {
        "question": "An email looks professional and has a familiar logo. Is it automatically safe?",
        "options": [
            "Yes, logos prove it is genuine",
            "Yes, professional grammar proves it",
            "No, verify the sender and request independently",
            "Yes, if it includes your first name",
        ],
        "answer": 2,
        "explanation": (
            "Logos, names, and polished wording can be copied. "
            "Check the sender and verify unusual requests independently."
        ),
    },
    {
        "question": "What should you do if you suspect a phishing email?",
        "options": [
            "Report it using your organization's approved process",
            "Reply to ask whether it is genuine",
            "Share its link publicly",
            "Enter fake personal information to test it",
        ],
        "answer": 0,
        "explanation": (
            "Use your organization's reporting process or report it "
            "to the relevant service provider. Do not interact with "
            "suspicious links or attachments."
        ),
    },
]


def calculate_result(form_data):
    answers = []
    score = 0

    for index, question in enumerate(QUESTIONS):
        selected_value = form_data.get(f"q{index}", "")
        selected = None

        if selected_value.isdigit():
            candidate = int(selected_value)
            if 0 <= candidate < len(question["options"]):
                selected = candidate

        correct = selected == question["answer"]

        if correct:
            score += 1

        answers.append(
            {
                "question": question["question"],
                "selected": selected,
                "selected_text": (
                    question["options"][selected]
                    if selected is not None
                    else "Not answered"
                ),
                "correct": correct,
                "correct_answer": question["options"][question["answer"]],
                "explanation": question["explanation"],
            }
        )

    total = len(QUESTIONS)
    percentage = round((score / total) * 100) if total else 0

    return {
        "score": score,
        "total": total,
        "percentage": percentage,
        "answers": answers,
    }


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        result = calculate_result(request.form)

    return render_template(
        "index.html",
        emails=EMAILS,
        questions=QUESTIONS,
        result=result,
    )


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(debug=True)
