heart_rates = [72,60,126,85,90,59,76,131,88,121,64]
n=len(heart_rates)
mean=sum(heart_rates)/n
print("Patient number:", n)
print("Mean heart rate:", round(mean, 2))
#categorize heart rates low (<60), normal (60-120), high (>120)
low = 0
normal = 0
high = 0
for rate in heart_rates:
    if rate < 60:
        low += 1
    elif 60 <= rate <= 120:
        normal += 1 
    else:        
        high += 1
print("Low heart rates number:", low)
print("Normal heart rates number:", normal)
print("High heart rates number:", high)
categories = {"Low": low, "Normal": normal, "High": high}
max_category = max(categories, key=categories.get)
print("Most common heart rate category:", max_category)
import matplotlib.pyplot as plt
#pie chart of heart rate categories
labels = categories.keys()
sizes = categories.values()
colors = ['lightcoral', 'lightblue', 'lightgreen']
labels = ["Low (<60)", "Normal (60-120)", "High (>120)"]
sizes = [low, normal, high]

def show_count(pct):
    total = sum(sizes)
    return int(round(pct * total / 100))

# 绘制饼图
plt.pie(sizes, labels=labels, autopct=lambda pct: f"{int(pct/100*sum(sizes))} people")
plt.title("Heart Rate Category Distribution")
plt.show()