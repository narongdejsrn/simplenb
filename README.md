### simplenb - Python Naive Bayes Classifier
Simple text classification with Naive Bayes
implementation is based on [BionicSpirit](https://www.bionicspirit.com/blog/2012/02/09/howto-build-naive-bayes-classifier.html) blog

You can use it for any basic text classfication such as 
* Spam Detection
* Assign category to items automatically
* Sentiment analysis
* and much more..

## Requirement
```
- Python 2.7+ (other version will probably work too)
- Numpy (http://www.scipy.org/install.html)
```

## Installation
```
pip install simplenb
```

## Example Usage
go check out [naivebayes.py](https://github.com/Zenyai/Python-Naive-Bayes-Classifier/blob/master/simplenb/naivebayes.py), you should be able to understand it pretty easily. Below are an example from test.py
```
from simplenb import naivebayes

nb = naivebayes.NaiveBayes()
nb.stop_word = ["the", "to", "you", "he", "only", "if", "it"]
nb.train("spam", "Buy viagra for a chance to win $million as")
nb.train("spam", "Work hard get laid by pretty at playboy mansion")
nb.train("ham", "Can you forward me the files from")
nb.train("ham", "That company called yesterday for advertisement")

print nb.classify("Could you advertisement zenyai student")
```
