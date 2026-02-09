from io import StringIO
import sys
import core as c


class TestCore:

    def test_repeat_message_output(self):
        captured = StringIO()
        sys.stdout = captured
        c.repeat_message("Hi", 3)
        sys.stdout = sys.__stdout__
        assert captured.getvalue().strip().split("\n") == ["Hi", "Hi", "Hi"]

    def test_triangle_number(self):
        cases = [
            (1, False),
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (6, True)
        ]
        for n, expected in cases:
            assert c.is_triangle_number(n) == expected

    def test_print_odds_down(self):
        captured = StringIO()
        sys.stdout = captured
        c.print_odds_down(7)
        sys.stdout = sys.__stdout__
        assert captured.getvalue().strip().split("\n") == ["7", "5", "3", "1"]

    def test_rate_username(self):
        assert c.rate_username("") == "Invalid"
        assert c.rate_username("abc") == "Poor"
        assert c.rate_username("user123") == "Good"
        assert c.rate_username("user_123") == "Excellent"

    def test_mirror_sentence(self):
        assert c.mirror_sentence("Hello World") == "World Hello"
        assert c.mirror_sentence("  Learn   Python Fast ") == "Fast Python Learn"
        assert c.mirror_sentence("") == ""
