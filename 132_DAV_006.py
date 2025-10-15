#!/usr/bin/env python
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt
import numpy as np

games = [1, 2, 3, 4, 5, 6]
points_scored = [95, 102, 78, 88, 110, 100]
opponent_points = [90, 88, 100, 85, 95, 100]
attendance = [1500, 1800, 1200, 1600, 2000, 1900]

avg_attendance = np.mean(attendance)
print(f"Average attendance: {avg_attendance}")

plt.figure(figsize=(8, 5))
plt.plot(games, attendance, marker="o", color="orange", label="Attendance per Game")
plt.axhline(y=average_attendance, color="red", linestyle="--", label=f"Average Attendance")

plt.title("Attendance Over the Season")
plt.xlabel("Game number")
plt.ylabel("Attendance")
plt.grid()
plt.legend()
plt.show()



players= ['A','B','C','D','E']
points= np.array([
    [20,15,25,18,17],
    [22,18,20,25,17],
    [15,12,28,10,13],
    [18,20,22,15,13],
    [25,25,30,20,10],
    [20,22,18,30,10]
])


total_points = np.sum(points, axis=0)
maximum_points = np.max(total_points)
player_score = dict(zip(players, total_points))
player_with_max_score = list(player_score.items())[0]
for i in player_score.items():
    if i[1] > player_with_max_score[1]:
        player_with_max_score = i
print(f"Player with max score = {player_with_max_score[0]}")
plt.figure(figsize=(8, 5))
plt.bar(players, total_points, color="skyblue")
plt.title("Total points scored by each player")
plt.xlabel("Player")
plt.ylabel("Total points scored")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()




threshold = 100
above_threshold = sum(1 for score in points_scored if score > threshold)

ranges = ['80-90', '90-100', '100-110', '110+']
counts = [sum(80 <= score < 90 for score in points_scored),
          sum(90 <= score < 100 for score in points_scored),
          sum(100 <= score < 110 for score in points_scored),
          sum(score >= 110 for score in points_scored)]

plt.bar(ranges, counts,color="orange")
plt.title('Number of games in different score ranges')
plt.grid(True)
plt.show()










best_opponent_index = np.argmin(opponent_points)
print(f"Best opponent performance was against game {best_opponent_index + 1}")

plt.bar(games, opponent_points)
plt.title('Points scored against each opponent')
plt.show()

plt.bar(games, attendance)
plt.title('Attendance for each game')
plt.show()






wins = [1 if points_scored[i] > opponent_points[i] else 0 for i in range(len(games))]
losses = [1 if points_scored[i] < opponent_points[i] else 0 for i in range(len(games))]

x = np.arange(len(games))
width = 0.35
fig, ax = plt.subplots()
ax.bar(x - width/2, wins, width, label='Wins')
ax.bar(x + width/2, losses, width, label='Losses')
ax.set_xticks(x)
ax.set_xticklabels(games)
ax.legend()
plt.title('Wins and Losses per Game')
plt.show()



plt.scatter(points_scored, wins)
plt.xlabel('Points Scored')
plt.ylabel('Wins')
plt.title('Points Scored vs Wins')
plt.show()


# In[ ]:




