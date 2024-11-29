
import matplotlib.pyplot as plt

mp_results = {
    'BJP': 163,
    'INC': 66,
    'BSP': 0,
    'Others': 1
}

rajasthan_results = {
    'INC': 69,
    'BJP': 115,
    'BSP': 2,
    'Others': 13
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

ax1.pie(mp_results.values(), labels=mp_results.keys(), autopct='%1.1f%%',
        explode=[0.1 if key == max(mp_results, key=mp_results.get) else 0 for key in mp_results.keys()])
ax1.set_title("Madhya Pradesh Assembly Results 2023")

ax2.pie(rajasthan_results.values(), labels=rajasthan_results.keys(), autopct='%1.1f%%',
        explode=[0.1 if key == max(rajasthan_results, key=rajasthan_results.get) else 0 for key in rajasthan_results.keys()])
ax2.set_title("Rajasthan Assembly Results 2023")

plt.show()

parties = list(set(mp_results.keys()).union(rajasthan_results.keys()))
mp_seats = [mp_results.get(party, 0) for party in parties]
rajasthan_seats = [rajasthan_results.get(party, 0) for party in parties]

x = range(len(parties)) 
width = 0.35 

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar([i - width/2 for i in x], mp_seats, width, label='Madhya Pradesh', color='skyblue')
ax.bar([i + width/2 for i in x], rajasthan_seats, width, label='Rajasthan', color='orange')

ax.set_xlabel('Parties')
ax.set_ylabel('Seats Won')
ax.set_title('Seat Share in Assembly Elections 2023')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.legend()

plt.show()
