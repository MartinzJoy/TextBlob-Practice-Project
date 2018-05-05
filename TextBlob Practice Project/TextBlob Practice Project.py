#Doing Some sentiment analysis practice
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy
#opening a file and giving it read mode only
file = open("SONA Speeche's/2016_Zuma.txt","r")

#reading text from the file
text_read = file.read()
#getting all sentences from the text
blob = TextBlob(text_read)
sentences = blob.sentences
print("Number of sentences is :"+str(len(sentences)))
count_positive = 0
count_negative = 0
count_neutral = 0
count_objective = 0
count_subjective = 0

positive_array = []
negative_array = []
neutral_array = []
for sentence in blob.sentences:
    pol = TextBlob(sentence.string)
    senti = pol.sentiment.polarity
    #Checking sentiments
    if senti < 0:
        count_negative+=1
        negative_array.append(count_negative)
    elif senti > 0:
        count_positive+=1
        positive_array.append(count_positive)
    elif senti == 0:
        count_neutral+=1
        neutral_array.append(count_neutral)
    #Checking subjectivity
    subj = sentence.sentiment.subjectivity
    if subj > 0.5:
        count_subjective+=1
    elif subj < 0.5:
        count_objective+=1

print(
    "Positive: "+str(count_positive)+"\n"
    +"Negative: "+str(count_negative)+"\n"
    +"Neutral: "+str(count_neutral)+"\n"
    )

#IF the negative value is the biggest
if count_negative > count_positive and count_negative > count_neutral:
    print("Most of the stuff this guy said was negative, what a pessimist!\nShame on you man!")
#IF the positive value is the biggest
elif count_negative < count_positive and count_positive > count_neutral:
    print("This chap was a very positve man! Wow that's great to know hey!")
#IF the neutral value is the biggest
elif count_negative < count_neutral and count_positive < count_neutral:
    print("This dude was very neutral in this speech")
else:
    print("Not much can be said about this dude hey")


print("\nSubjective: "+str(count_subjective)+"\n"
      "Objective: "+str(count_objective)+"\n"
      )

#If subjective or not
if count_subjective > count_objective:
    print("What a subjective speech, I hope the people don't get fooled by this guy.")
else:
    print("Very objective guy, that's nice and cool.")

#Ploting a simple pie chart
Sentiment_Labels = ["Positive", "Negative", "Neutral"]
Sentistats = [count_positive, count_negative, count_neutral]
plt.axis("equal") #This is to make the chart circel, otherwise it's oval by default
plt.pie(Sentistats, labels = Sentiment_Labels, shadow = True)
plt.title("Sentiments")
plt.show()
