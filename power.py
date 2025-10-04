import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Connexion DB (déjà dans ton notebook, réutilise)
from pymongo import MongoClient
from datetime import datetime
client = MongoClient('mongodb://localhost:27017/')
db = client['eduhub_db']  # Ou 'eduhub' si c'est ton DB name

# Créer dossier images
os.makedirs('images', exist_ok=True)

# Thème : Vert EduHub (comme ta prez)
plt.style.use('seaborn-v0_8')  # Ou 'default' si pas seaborn
colors = ['#2E8B57', '#228B22', '#32CD32']  # Verts

# 1. VISUAL 1 : Bar Chart - Popular Categories (Slide 5 : Aggregations)
# Data de Cell 21 (popular_cats)
popular_data = {
    '_id': ['Programming', 'Data Science', 'Web Development'],
    'enrollCount': [32, 17, 16]
}
df_popular = pd.DataFrame(popular_data)

fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.barplot(data=df_popular, x='_id', y='enrollCount', palette=colors[:3], ax=ax1)
ax1.set_title('Category of most Popular Courses (Enrollments)', fontsize=14, fontweight='bold')
ax1.set_ylabel('Number of Enrollments')
ax1.set_xlabel('Category')
for i, v in enumerate(df_popular['enrollCount']):
    ax1.text(i, v + 0.5, str(v), ha='center', va='bottom', fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/popular_categories.png', dpi=300, bbox_inches='tight')
plt.show()
print("✅ Graphique 'popular_categories.png' sauvé pour Slide 5.")

# 2. VISUAL 2 : Line Chart - Monthly Enrollment Trends (Slide 5 : Trends)
# Data de Cell 21 (monthly_trends) - exemple réaliste de ton log
monthly_data = {
    '_id': ['2025-01', '2025-02', '2025-03'],
    'count': [5, 15, 10]  # Adapte avec tes vraies data si différent
}
df_monthly = pd.DataFrame(monthly_data)

fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.plot(df_monthly['_id'], df_monthly['count'], marker='o', linewidth=2, color=colors[0], markersize=8)
ax2.set_title('Monthly Enrollment Trends', fontsize=14, fontweight='bold')
ax2.set_ylabel('Number of Enrollments')
ax2.set_xlabel('Month')
ax2.grid(True, alpha=0.3)
for i, v in enumerate(df_monthly['count']):
    ax2.annotate(str(v), (i, v), textcoords="offset points", xytext=(0,10), ha='center', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/monthly_trends.png', dpi=300, bbox_inches='tight')
plt.show()
print("✅ Graphique 'monthly_trends.png' sauvé pour Slide 5.")

# 3. VISUAL 3 : Bar Chart - Performance Before/After (Slide 6 : Optimization)
# Data de Cell 22 (timing & docs examined)
perf_data = {
    'Metric': ['Docs Examinés', 'Temps (s)'],
    'Sans Index': [28, 0.0060],
    'Avec Index': [8, 0.0055]
}
df_perf = pd.DataFrame(perf_data)

fig3, ax3 = plt.subplots(figsize=(8, 5))
x = range(len(df_perf['Metric']))
width = 0.35
ax3.bar([i - width/2 for i in x], df_perf['Sans Index'], width, label='Sans Index', color='red', alpha=0.7)
ax3.bar([i + width/2 for i in x], df_perf['Avec Index'], width, label='Avec Index', color=colors[1], alpha=0.7)
ax3.set_title('Optimisation performance : Before/After Index', fontsize=14, fontweight='bold')
ax3.set_ylabel('Value')
ax3.set_xlabel('Metric')
ax3.set_xticks(x)
ax3.set_xticklabels(df_perf['Metric'])
ax3.legend()
ax3.grid(True, alpha=0.3)
# Ajoute valeurs sur barres
for i, row in df_perf.iterrows():
    ax3.text(i - width/2, row['Sans Index'] + 0.1, f'{row["Sans Index"]}', ha='center', va='bottom')
    ax3.text(i + width/2, row['Avec Index'] + 0.1, f'{row["Avec Index"]}', ha='center', va='bottom')
plt.tight_layout()
plt.savefig('images/performance_optimization.png', dpi=300, bbox_inches='tight')
plt.show()
print("✅ Graphique 'performance_optimization.png' sauvé pour Slide 6.")

# 4. BONUS : Pie Chart - Répartition Users (Slide 4 : Data Population)
# Data de Cell 24 (15 students, 5 instructors)
user_data = {'Role': ['Students', 'Instructors'], 'Count': [15, 5]}
df_user = pd.DataFrame(user_data)

fig4, ax4 = plt.subplots(figsize=(6, 6))
ax4.pie(df_user['Count'], labels=df_user['Role'], autopct='%1.1f%%', colors=colors[:2], startangle=90)
ax4.set_title('Distribution of Users', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/user_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
print("✅ Graphique 'user_distribution.png' sauvé pour Slide 4 (bonus).")

print("Tous les graphiques sauvés dans 'images/' – Insère-les dans PowerPoint !")