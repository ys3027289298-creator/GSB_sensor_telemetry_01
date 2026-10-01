import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_empty_tokenize(self):
        self.assertEqual(core.tokenize(""), [])

    def test_02_strip_tokens(self):
        self.assertEqual(core.tokenize(" a , b "), ["a", "b"])

    def test_03_ignore_empty_fields(self):
        self.assertEqual(core.tokenize("a,,b"), ["a", "b"])

    def test_04_normalize_dedup(self):
        self.assertEqual(core.normalize(["a", "a", "b"]), ["a", "b"])

    def test_05_empty_field_invalid(self):
        self.assertFalse(core.validate(["a", ""]))

    def test_06_non_numeric_invalid(self):
        self.assertFalse(core.validate(["a", "x"]))

    def test_07_count_nonempty(self):
        self.assertEqual(core.count_fields(["a", "", "b"]), 2)

    def test_08_find_error_index(self):
        self.assertEqual(core.find_error(["a", "", "b"]), 1)

    def test_09_transform_removes_none(self):
        self.assertEqual(core.transform(["a", None, "b"]), ["a", "b"])

    def test_10_load_preserves_id(self):
        state = core.new_game()
        state["next_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["next_id"], 4)


if __name__ == "__main__":
    unittest.main()
