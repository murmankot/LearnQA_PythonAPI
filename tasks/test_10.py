class TestEx10:

    def test_length_of_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Phrase {phrase} longer than 15 symbols"
