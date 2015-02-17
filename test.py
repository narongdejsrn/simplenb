from simplenb import naivebayes

nb = naivebayes.NaiveBayes()
nb.stop_word = ["the", "to", "you", "he", "only", "if", "it"]
nb.train("spam", "Buy viagra for a chance to win $million as")
nb.train("spam", "Work hard get laid by pretty at playboy mansion")
nb.train("ham", "Can you forward me the files from")
nb.train("ham", "That company called yesterday for advertisement")

print nb.classify("Could you advertisement zenyai student")
