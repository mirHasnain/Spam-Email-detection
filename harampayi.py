import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('spambase_dataset.csv')

# Separate spam and non-spam emails
spam_emails = data[data['is_spam'] == 1]
non_spam_emails = data[data['is_spam'] == 0]

# Plot histograms
plt.figure(figsize=(12, 6))

# Histogram for spam emails
plt.subplot(1, 2, 1)
plt.hist(spam_emails['word_freq_make'], bins=20, color='red', edgecolor='black')
plt.title('Frequency of "make" in Spam Emails')
plt.xlabel('Frequency of "make"')
plt.ylabel('Count')

# Histogram for non-spam emails
plt.subplot(1, 2, 2)
plt.hist(non_spam_emails['word_freq_make'], bins=20, color='blue', edgecolor='black')
plt.title('Frequency of "make" in Non-Spam Emails')
plt.xlabel('Frequency of "make"')
plt.ylabel('Count')

plt.tight_layout()
plt.show()
