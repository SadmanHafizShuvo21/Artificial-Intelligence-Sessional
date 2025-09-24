import math
from collections import defaultdict, Counter

class NaiveBayes:
    def __init__(self):
        self.word_counts = defaultdict(Counter)
        self.total_words = defaultdict(int)
        self.doc_counts = defaultdict(int)
        self.vocab = set()

    def train(self, data):
        for text, label in data:
            self.doc_counts[label] += 1
            words = text.lower().split()
            for word in words:
                self.word_counts[label][word] += 1
                self.total_words[label] += 1
                self.vocab.add(word)

    def predict_prob(self, text, label):
        total_docs = sum(self.doc_counts.values())
        log_prob = math.log(self.doc_counts[label] / total_docs)
        for word in text.lower().split():
            count = self.word_counts[label][word]
            prob = (count + 1) / (self.total_words[label] + len(self.vocab))
            log_prob += math.log(prob)
        return log_prob

    def predict_with_probs(self, text):
        log_probs = {label: self.predict_prob(text, label) for label in self.doc_counts}
        max_log = max(log_probs.values())
        exp_probs = {label: math.exp(lp - max_log) for label, lp in log_probs.items()}
        total = sum(exp_probs.values())
        probs = {label: val/total for label, val in exp_probs.items()}
        prediction = max(probs, key=probs.get)
        return prediction, probs

# Example usage
if __name__ == "__main__":
    training_data = [
        ("buy cheap meds now", 1),
        ("limited time offer", 1),
        ("hello friend how are you", 0),
        ("let's meet for lunch", 0)
    ]
    nb = NaiveBayes()
    nb.train(training_data)

    pred, probs = nb.predict_with_probs("cheap offer now")

    print(f"Ham (0): {probs[0]:.6f}")
    print(f"Spam (1): {probs[1]:.6f}")
    print("Final Prediction:", "Spam" if pred == 1 else "Ham")
