
import unittest

from app import app, QUESTIONS


class PhishAwareTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_homepage_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"PhishAware", response.data)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_all_correct_answers_score_100_percent(self):
        answers = {
            f"q{i}": str(question["answer"])
            for i, question in enumerate(QUESTIONS)
        }

        response = self.client.post("/", data=answers)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"100%", response.data)

    def test_all_wrong_answers_score_zero_percent(self):
        answers = {
            f"q{i}": str(
                (question["answer"] + 1) % len(question["options"])
            )
            for i, question in enumerate(QUESTIONS)
        }

        response = self.client.post("/", data=answers)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"0%", response.data)

    def test_missing_answers_are_handled(self):
        response = self.client.post("/", data={})

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"0%", response.data)
        self.assertIn(b"Not answered", response.data)

    def test_invalid_answer_is_handled(self):
        response = self.client.post(
            "/",
            data={"q0": "999", "q1": "invalid"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Not answered", response.data)


if __name__ == "__main__":
    unittest.main()
