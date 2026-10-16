import matplotlib.pyplot as plt
import numpy as np

# 3(a) Line Plot
Overs = list(range(5, 51, 5))

Indian_Score = [30, 55, 90, 129, 165, 200, 239, 270, 310, 350]
Srilankan_Score = [25, 70, 90, 120, 140, 170, 195, 220, 255, 279]

plt.plot(Overs, Indian_Score, label="INDIA")
plt.plot(Overs, Srilankan_Score, label="SRILANKA")

plt.title("INDIA Vs SRILANKA")
plt.xlabel("Overs")
plt.ylabel("Score")
plt.legend()
plt.show()


# 3(b) Bar Chart
Names = ['SHREE', 'DEV', 'KEERTHI', 'PRIYA', 'SHAN', 'KUMARAN']

xaxis = np.arange(len(Names))
Percentage_hsc = [96, 91, 94, 75, 45, 81]

plt.bar(Names, Percentage_hsc)
plt.xticks(xaxis, Names, rotation=45)

plt.xlabel("Names of Pupil")
plt.ylabel("Percentage")
plt.title("Comparison of HSC Percentage")
plt.show()


# 3(c) Pie Chart
labels = ['CANDIDATE 1', 'CANDIDATE 2',
          'CANDIDATE 3', 'CANDIDATE 4']

Votes = [315, 130, 245, 210]

colors = ['green', 'yellow', 'red', 'orange']
explode = (0.2, 0, 0, 0)

plt.pie(Votes,
        labels=labels,
        colors=colors,
        explode=explode,
        autopct='%0.2f%%')

plt.title("Election Results")
plt.show()