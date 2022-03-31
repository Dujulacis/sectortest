import matplotlib.pyplot as plt
def make_autopct(pieces):
    def my_autopct(pct):
        total = sum(pieces)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
plt.title("Zveri zoodarza")
pieces=[30, 100, 200, 20, 90]
pietitles=("Merkaki", "Zaki", "Zurkas", "Zirafes", "Krokodili")
colors=("Green", "Blue", "Purple", "Red", "Orange")
explosion=[0.05, 0.05, 0.05, 0.05, 0.05]
plt.pie(pieces, labels=pietitles, colors=colors, explode=explosion, autopct=make_autopct(pieces))
plt.show()