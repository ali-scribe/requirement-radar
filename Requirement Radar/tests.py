import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import run_rule_checks


class TestRuleChecks(unittest.TestCase):
    def test_short_requirement_is_flagged(self):
        findings = run_rule_checks(
            "Login",
            {"acceptance_criteria": ["User can log in"]},
        )
        self.assertTrue(any("very short" in x for x in findings))

    def test_vague_wording_is_flagged(self):
        findings = run_rule_checks(
            "The app should provide a user-friendly experience.",
            {"acceptance_criteria": ["The user can create an account"]},
        )
        self.assertTrue(any("vague wording" in x for x in findings))

    def test_missing_action_is_flagged(self):
        findings = run_rule_checks(
            "Customers and account information.",
            {"acceptance_criteria": []},
        )
        self.assertTrue(any("expected outcome" in x for x in findings))
        self.assertTrue(any("No acceptance criteria" in x for x in findings))

    def test_clear_requirement_still_has_result(self):
        findings = run_rule_checks(
            "The system must save the selected language and display it "
            "on the next visit.",
            {"acceptance_criteria": ["Save and restore the selected language"]},
        )
        self.assertTrue(len(findings) > 0)


if __name__ == "__main__":
    unittest.main()
