import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
bat = pd.read_csv('C:\\Users\\ASUS\\Downloads\\bat.csv') 
bowl= pd.read_csv('C:\\Users\\ASUS\\Downloads\\bowl.csv') 
stat= pd.read_csv('C:\\Users\\ASUS\\Downloads\\stat.csv') 
players= pd.read_csv('C:\\Users\\ASUS\\Downloads\\players.csv') 
print(bat.head())
print(bowl.head())
print(stat.head())
print(players.head())

# bar chart
most_run = bat.groupby('Batsman_Name')['Runs'].sum().sort_values(ascending=False).reset_index().head(10)
print(most_run)
plt.figure(figsize=(10, 6))
plt.bar(most_run['Batsman_Name'], most_run['Runs'], color='skyblue')

plt.xlabel('Batsman Name')
plt.ylabel('Total Runs')
plt.title('Top 10 Batsmen by Runs')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#pie chart
most_fours = bat.groupby('Batsman_Name')['4s'].sum().sort_values(ascending=False).reset_index().head(10)
plt.figure(figsize=(8, 8))
plt.pie(most_fours['4s'], labels=most_fours['Batsman_Name'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Top 10 Batsmen by Fours (4s)')
plt.axis('equal')
plt.show()

# Histogram 
plt.figure(figsize=(10, 6))
plt.hist(bat['Runs'], bins=10, color='orange', edgecolor='black')
plt.xlabel('Runs Scored')
plt.ylabel('Frequency')
plt.title('Distribution of Runs Scored by Batsmen')
plt.xticks(rotation=45, ha='right')
plt.tight_layout() 
plt.show()

#line chart
batting_position_max_runs = bat.groupby('Batting_Position')['Runs'].max()
plt.figure(figsize=(10, 6))
plt.plot(batting_position_max_runs.index, batting_position_max_runs.values, marker='o', linestyle='-', color='b')
plt.xlabel('Batting Position')
plt.ylabel('Highest Runs Scored')
plt.title('Highest Runs Scored at Different Batting Positions')
plt.grid(True)
plt.show()

#bowlers visualization!!!!!!!!!!!!!!!!!!!!!
#line chart
bowl['Wickets'] = pd.to_numeric(bowl['Wickets'], errors='coerce')
top_3_wickets = bowl.nlargest(3, 'Wickets')
plt.figure(figsize=(12, 6))  
for bowler in top_3_wickets['Bowler_Name'].unique():
    bowler_data = bowl[bowl['Bowler_Name'] == bowler]
    plt.plot(bowler_data['Match_Between'], bowler_data['Wickets'], label=bowler, marker='o')
plt.xlabel('Match Between')
plt.ylabel('Wickets')
plt.title('Wickets Taken by Top 3 Bowlers Across Matches')
plt.xticks(rotation=45, ha='right')  
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

#pie chart
bowl['Maidens'] = pd.to_numeric(bowl['Maidens'], errors='coerce')
top_10_maidens = bowl.nlargest(10, 'Maidens')
maidens_counts = top_10_maidens.groupby('Bowler_Name')['Maidens'].sum()
plt.figure(figsize=(8, 8))
plt.pie(maidens_counts, labels=maidens_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Maidens Bowled by Top 10 Bowlers')
plt.axis('equal') 
plt.show()

#Histrogram
bowl['Economy'] = pd.to_numeric(bowl['Economy'], errors='coerce')
top_10_economy = bowl.nsmallest(10, 'Economy')
plt.figure(figsize=(10, 6))
plt.hist(top_10_economy['Economy'], bins=10, color='blue', edgecolor='black')
plt.xlabel('Economy Rate')
plt.ylabel('Frequency')
plt.title('Distribution of Economy Rates (Top 10 Bowlers)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

 # bar chart  
bowl['Wickets'] = pd.to_numeric(bowl['Wickets'], errors='coerce')
total_wickets = bowl.groupby('Bowler_Name')['Wickets'].sum().reset_index()
top_5_wickets = total_wickets.nlargest(5, 'Wickets')

# Bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_5_wickets['Bowler_Name'], top_5_wickets['Wickets'], color='blue')
plt.xlabel('Bowler Name')
plt.ylabel('Total Wickets')
plt.title('Top 5 Wicket Takers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
# stat !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# bar chart
winner_counts = stat['Winner'].value_counts()
top_winners = winner_counts.nlargest(5)
plt.figure(figsize=(10, 6))
plt.bar(top_winners.index, top_winners.values, color='purple')
plt.xlabel('Team Name')
plt.ylabel('Total Wins')
plt.title('Top 5 Teams Based on Wins')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#pie chart
venue_counts = stat['Venue'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(venue_counts, labels=venue_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribution of Matches by Venue')
plt.axis('equal')  
plt.show()


#line chart
role_counts = players['playingRole'].value_counts().sort_index()
plt.figure(figsize=(12, 4))
plt.plot(role_counts.index, role_counts.values, marker='o', color='green')
plt.xlabel('Playing Role')
plt.ylabel('Number of Players')
plt.title('Distribution of Players by Playing Role')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#scatter plot
batting_counts = players['battingStyle'].value_counts()
plt.figure(figsize=(10, 6))
plt.scatter(batting_counts.index, batting_counts.values, color='orange', s=100)
plt.xlabel('Batting Style')
plt.ylabel('Number of Players')
plt.title('Distribution of Batting Styles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()