#Doing Some sentiment analysis practice
from textblob import TextBlob
from matplotlib import pyplot as plt
import pandas as pd
from glob import glob #This module makes it possible for us to loop through every file that is available in a particular folder(SONA Speeche's in our case)

file_list = glob("C:/Users/Martin/Desktop/Machine Learning Practice Projects/TextBlob Practice Project/SONA Speeche's/*.txt") # Getting all files that have the extension .txt in this folder

#Creating other count vars for each president

#No. of speeches per president
count_deKlerk = 0
count_Mandela = 0
count_Mbeki = 0
count_Motlanthe = 0
count_Zuma = 0
count_Ramaphosa = 0

#Positives
count_positive_deKlerk = 0
count_positive_Mandela = 0
count_positive_Mbeki = 0
count_positive_Motlanthe = 0
count_positive_Zuma = 0
count_positive_Ramaphosa = 0

#Negatives
count_negative_deKlerk = 0
count_negative_Mandela = 0
count_negative_Mbeki = 0
count_negative_Motlanthe = 0
count_negative_Zuma = 0
count_negative_Ramaphosa = 0

#Neutrals
count_neutral_deKlerk = 0
count_neutral_Mandela = 0
count_neutral_Mbeki = 0
count_neutral_Motlanthe = 0
count_neutral_Zuma = 0
count_neutral_Ramaphosa = 0

#Subjectivity
count_subjective_deKlerk = 0
count_subjective_Mandela = 0
count_subjective_Mbeki = 0
count_subjective_Motlanthe = 0
count_subjective_Zuma = 0
count_subjective_Ramaphosa = 0

#Objectivity
count_objective_deKlerk = 0
count_objective_Mandela = 0
count_objective_Mbeki = 0
count_objective_Motlanthe = 0
count_objective_Zuma = 0
count_objective_Ramaphosa = 0

#This is one huge loop!!!
for filepath in file_list:
    
    file = open(file = filepath,mode = "r",encoding = "UTF8") #Opening a file with read mode using the UTF8 encoding

    #reading text from the file
    text_read = file.read()
    file.close() #Closing the file

    #getting all sentences from the text
    blob = TextBlob(text_read)
    sentences = blob.sentences
    #print("Number of sentences is :"+str(len(sentences)))
    count_positive = 0
    count_negative = 0
    count_neutral = 0
    count_objective = 0
    count_subjective = 0

    positive_array = []
    negative_array = []
    neutral_array = []
    #Calculations start to happen here
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

    #Doing operations for each president
    #The .count method checks if the string occurs in the file path name
    if filepath.count("deKlerk") > 0:
        count_deKlerk +=1
        count_positive_deKlerk += count_positive
        count_negative_deKlerk += count_negative
        count_neutral_deKlerk += count_neutral
        count_subjective_deKlerk += count_subjective
        count_objective_deKlerk += count_objective
    elif filepath.count("Mandela") > 0:
        count_Mandela +=1
        count_positive_Mandela += count_positive
        count_negative_Mandela += count_negative
        count_neutral_Mandela += count_neutral
        count_subjective_Mandela += count_subjective
        count_objective_Mandela += count_objective
    elif filepath.count("Mbeki") > 0:
        count_Mbeki +=1
        count_positive_Mbeki += count_positive
        count_negative_Mbeki += count_negative
        count_neutral_Mbeki += count_neutral
        count_subjective_Mbeki += count_subjective
        count_objective_Mbeki += count_objective
    elif filepath.count("Motlanthe") > 0:
        count_Motlanthe +=1
        count_positive_Motlanthe += count_positive
        count_negative_Motlanthe += count_negative
        count_neutral_Motlanthe += count_neutral
        count_subjective_Motlanthe += count_subjective
        count_objective_Motlanthe += count_objective
    elif filepath.count("Zuma") > 0:
        count_Zuma +=1
        count_positive_Zuma += count_positive
        count_negative_Zuma += count_negative
        count_neutral_Zuma += count_neutral
        count_subjective_Zuma += count_subjective
        count_objective_Zuma += count_objective
    elif filepath.count("Ramaphosa") > 0:
        count_Ramaphosa +=1
        count_positive_Ramaphosa += count_positive
        count_negative_Ramaphosa += count_negative
        count_neutral_Ramaphosa += count_neutral
        count_subjective_Ramaphosa += count_subjective
        count_objective_Ramaphosa += count_objective
        
    '''
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
    plt.show() '''

#This is after the loop'
    '''
print("\n\nStatistics for deKlerk:")
print("Number of SONA speeches as Pres is "+str(count_deKlerk))
print("Positive: "+str(count_positive_deKlerk)+"\n"
      +"Negative: "+str(count_negative_deKlerk)+"\n"
      +"Neutral: "+str(count_neutral_deKlerk)+"\n"
      +"\nSubjectivity: "+str(count_subjective_deKlerk)+"\n"
      +"Objectivity: "+str(count_objective_deKlerk)
      )

print("\n\nStatistics for Mandela:")
print("Number of SONA speeches as Pres is "+str(count_Mandela))
print("Positive: "+str(count_positive_Mandela)+"\n"
      +"Negative: "+str(count_negative_Mandela)+"\n"
      +"Neutral: "+str(count_neutral_Mandela)+"\n"
      +"\nSubjectivity: "+str(count_subjective_Mandela)+"\n"
      +"Objectivity: "+str(count_objective_Mandela)
      )

print("\n\nStatistics for Mbeki:")
print("Number of SONA speeches as Pres is "+str(count_Mbeki))
print("Positive: "+str(count_positive_Mbeki)+"\n"
      +"Negative: "+str(count_negative_Mbeki)+"\n"
      +"Neutral: "+str(count_neutral_Mbeki)+"\n"
      +"\nSubjectivity: "+str(count_subjective_Mbeki)+"\n"
      +"Objectivity: "+str(count_objective_Mbeki)
      )

print("\n\nStatistics for Motlanthe:")
print("Number of SONA speeches as Pres is "+str(count_Motlanthe))
print("Positive: "+str(count_positive_Motlanthe)+"\n"
      +"Negative: "+str(count_negative_Motlanthe)+"\n"
      +"Neutral: "+str(count_neutral_Motlanthe)+"\n"
      +"\nSubjectivity: "+str(count_subjective_Motlanthe)+"\n"
      +"Objectivity: "+str(count_objective_Motlanthe)
      )

print("\n\nStatistics for Zuma:")
print("Number of SONA speeches as Pres is "+str(count_Zuma))
print("Positive: "+str(count_positive_Zuma)+"\n"
      +"Negative: "+str(count_negative_Zuma)+"\n"
      +"Neutral: "+str(count_neutral_Zuma)+"\n"
      +"\nSubjectivity: "+str(count_subjective_Zuma)+"\n"
      +"Objectivity: "+str(count_objective_Zuma)
      )

print("\n\nStatistics for Ramaphosa:")
print("Number of SONA speeches as Pres is "+str(count_Ramaphosa))
print("Positive: "+str(count_positive_Ramaphosa)+"\n"
      +"Negative: "+str(count_negative_Ramaphosa)+"\n"
      +"Neutral: "+str(count_neutral_Ramaphosa)+"\n"
      +"\nSubjectivity: "+str(count_subjective_Ramaphosa)+"\n"
      +"Objectivity: "+str(count_objective_Ramaphosa)
      )
'''


values_deKlerk = [count_deKlerk, count_positive_deKlerk, count_negative_deKlerk, count_neutral_deKlerk, count_subjective_deKlerk, count_objective_deKlerk]
values_Mandela = [count_Mandela, count_positive_Mandela, count_negative_Mandela, count_neutral_Mandela, count_subjective_Mandela, count_objective_Mandela]
values_Mbeki = [count_Mbeki, count_positive_Mbeki, count_negative_Mbeki, count_neutral_Mbeki, count_subjective_Mbeki, count_objective_Mbeki]
values_Motlanthe = [count_Motlanthe, count_positive_Motlanthe, count_negative_Motlanthe, count_neutral_Motlanthe, count_subjective_Motlanthe, count_objective_Motlanthe]
values_Zuma = [count_Zuma, count_positive_Zuma, count_negative_Zuma, count_neutral_Zuma, count_subjective_Zuma, count_objective_Zuma]
values_Ramaphosa = [count_Ramaphosa, count_positive_Ramaphosa, count_negative_Ramaphosa, count_neutral_Ramaphosa, count_subjective_Ramaphosa, count_objective_Ramaphosa]

values = [values_deKlerk, values_Mandela, values_Mbeki, values_Motlanthe, values_Zuma, values_Ramaphosa]

presidents = ["deKlerk", "Mandela", "Mbeki", "Motlanthe", "Zuma", "Ramaphosa"]
sentiment_analysis = ["speeches","positivity", "negativity", "neutrality", "subjectivity", "objectivity"]
count_speech = [count_deKlerk, count_Mandela, count_Mbeki, count_Motlanthe, count_Zuma, count_Ramaphosa]
count_pos = [count_positive_deKlerk, count_positive_Mandela, count_positive_Mbeki, count_positive_Motlanthe, count_positive_Zuma, count_positive_Ramaphosa]
count_neg = [count_negative_deKlerk, count_negative_Mandela, count_negative_Mbeki, count_negative_Motlanthe, count_negative_Zuma, count_negative_Ramaphosa]
cout_neu = [count_neutral_deKlerk, count_neutral_Mandela, count_neutral_Mbeki, count_neutral_Motlanthe, count_neutral_Zuma, count_neutral_Ramaphosa]
count_sub = [count_subjective_deKlerk, count_subjective_Mandela, count_subjective_Mbeki, count_subjective_Motlanthe, count_subjective_Zuma, count_subjective_Ramaphosa]
count_obj = [count_objective_deKlerk, count_objective_Mandela, count_objective_Mbeki, count_objective_Motlanthe, count_objective_Zuma, count_objective_Ramaphosa]

data = {
        "Speech": count_speech,
        "Positive": count_pos,
        "Negative": count_neg,
        "Neutral": cout_neu,
        "Subjective": count_sub,
        "Objective": count_obj
    }

obj = pd.DataFrame(data, index = presidents)

print(obj)
