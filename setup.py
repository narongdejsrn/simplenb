from distutils.core import setup
setup(
  name = 'simplenb',
  packages = ['simplenb'], # this must be the same as the name above
  version = '0.1',
  description = 'Simple text classification with Naive Bayes',
  author = 'Narongdej Sarnsuwan',
  author_email = 'narongdej@sarnsuwan.com',
  url = 'https://github.com/Zenyai/Python-Naive-Bayes-Classifier', # use the URL to the github repo
  download_url = 'https://github.com/Zenyai/Python-Naive-Bayes-Classifier/tarball/master', # I'll explain this in a second
  keywords = ['naive bayes', 'classifier', 'simple', 'zenyai'], # arbitrary keywords
  classifiers = [],
  install_requires=['scipy']
)
