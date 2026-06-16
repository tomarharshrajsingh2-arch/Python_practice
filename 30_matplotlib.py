import matplotlib.pyplot as plt
import numpy as np

Months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
sales = [45,52,48,61,58,72,69,75,68,82,90,95]

#line chart
plt.figure(figsize=(12,5))
plt.plot(Months,sales,marker='o',color='steelblue',linewidth=2,markersize=8)
plt.fill_between(Months,sales,alpha=0.15,color='steelblue')
plt.title("Monthly Sales 2024(Rs. Thousands)",fontsize=14,fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Sales (Rs .K)')
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.show()

# #Bar chart

cities=['Bhopal','Indore','Jabalpur','Gwalior','Ujjain']
students=[1200,2800,980,850,650]
colors=['#2196F3','#4CAF50','#ff9800','#9c27B0','#F44336']

plt.figure(figsize=(9,5))
bars = plt.bar(cities,students,color=colors,edgecolor='white',linewidth=1.5)
plt.title('Students Enrolled Per City')
plt.ylabel('No. of Students')
for bar,val in zip(bars,students):
    plt.text(bar.get_x()+ bar.get_width()/2,val+30,str(val),ha='center',fontweight='bold')

plt.tight_layout()
plt.show()



## scatter plot

study_hrs=np.random.uniform(2,10,50)
marks = study_hrs*7 + np.random.normal(0,8,50)
marks= np.clip(marks,30,100)
plt.figure(figsize=(8,5))
plt.scatter(study_hrs,marks,c=marks,cmap='RdYlGn',s=100,alpha=0.8)
plt.colorbar(label='Marks')
plt.title("Study Hours VS Exam marks")
plt.xlabel('Study Hours/Day')
plt.ylabel('Exam Marks')
plt.show()

