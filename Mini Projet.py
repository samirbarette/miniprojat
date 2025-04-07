import pandas as pd
import matplotlib.pyplot as plt

#  Importation des données
data = pd.read_csv('C:/Users/hp/Downloads/StudentsPerformance.csv')

# Exploration des données
data.info()

data.head()

print(data.describe())

# Nettoyage des données
print(data.isnull().sum())

# Moyenne des trois scores pour chaque ligne
data['average_score'] = data[['math score', 'reading score', 'writing score']].mean(axis=1)

# Filtrage : étudiants ayant une moyenne >= 70
top_students = data[data['average_score'] >= 70]

# Trier par moyenne
data_sorted = data.sort_values(by='average_score', ascending=False)

# calcul et afichage de Moyenne générale, Médiane et Écart-type
mean_score = data['average_score'].mean()
median_score = data['average_score'].median()
std_score = data['average_score'].std()

print("Moyenne générale :", mean_score)
print("Médiane :", median_score)
print("Écart-type :", std_score)

# Moyenne par genre
print("\nMoyenne par genre :")
print(data.groupby('gender')['average_score'].mean())

# Moyenne par niveau d'éducation des parents
print("\nMoyenne par niveau d'éducation des parents :")
print(data.groupby('parental level of education')['average_score'].mean())

# Visualisation : Histogramme des moyennes
data['average_score'].hist(bins=20)
plt.title('Répartition des Moyennes Générales')
plt.xlabel('Moyenne')
plt.ylabel('Nombre des etudiants')
plt.grid(True)
plt.show()

# Boxplot des moyennes par genre
data.boxplot(column='average_score', by='gender')
plt.title('Moyenne par Genre')
plt.suptitle('')
plt.xlabel('Genre')
plt.ylabel('Moyenne')
plt.show()

# Boxplot des moyennes par niveau d'éducation des parents
data.boxplot(column='average_score', by='parental level of education')
plt.title('Moyenne par parental level of education')
plt.suptitle('')
plt.xlabel('parental level of education')
plt.ylabel('Moyenne')
plt.show()

# Boxplot des moyennes par race/ethnicity
data.boxplot(column='average_score', by='race/ethnicity')
plt.title('Moyenne par race/ethnicity')
plt.suptitle('')
plt.xlabel('race/ethnicity')
plt.ylabel('Moyenne')
plt.show()

# Boxplot des moyennes par lunch
data.boxplot(column='average_score', by='lunch')
plt.title('Moyenne par lunch')
plt.suptitle('')
plt.xlabel('lunch')
plt.ylabel('Moyenne')
plt.show()

# Boxplot des moyennes par test preparation course
data.boxplot(column='average_score', by='test preparation course')
plt.title('Moyenne par test preparation course')
plt.suptitle('')
plt.xlabel('test preparation course')
plt.ylabel('Moyenne')
plt.show()

# Courbe : Score moyen par le genre
grouped_edu = data.groupby('gender')['average_score'].mean()
grouped_edu.plot(kind='bar', title="Score moyen selon le genre")
plt.ylabel("Moyenne")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Courbe : Score moyen par niveau d'éducation des parents
grouped_edu = data.groupby('parental level of education')['average_score'].mean()
grouped_edu.plot(kind='bar', title="Score moyen selon le niveau d'éducation des parents")
plt.ylabel("Moyenne")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Courbe : Score moyen par niveau du race/ethnicity
grouped_edu = data.groupby('race/ethnicity')['average_score'].mean()
grouped_edu.plot(kind='bar', title="Score moyen selon race/ethnicity")
plt.ylabel("Moyenne")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Courbe : Score moyen par niveau du lunch
grouped_edu = data.groupby('lunch')['average_score'].mean()
grouped_edu.plot(kind='bar', title="Score moyen selon lunch")
plt.ylabel("Moyenne")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Courbe : Score moyen par niveau du test preparation course
grouped_edu = data.groupby('test preparation course')['average_score'].mean()
grouped_edu.plot(kind='bar', title="Score moyen selon test preparation course")
plt.ylabel("Moyenne")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
