import os
import time
os.system('COLOR a')

def Date_Of_Birth_Collector():
    # ASKING USER WITH THE DATE OF BIRTH IN A PROPER WAY!
    try:
        print("\nPlease Enter the Details As Per As Instructed By The Program!")
        print("Provide Me With The Year You Were Born: Example: '2001' ")
        birth_year = int(input("Enter The Year You Were Born: "))
        os.system('cls')
        print("Provide Me With The Month You Were Born: Example: '12', which denotes December right ? "
              "\nSo, what your birth day month, please enter the value in numeric ;) ")


        month_of_birth = int(input("Enter The Month You were Born: "))
        if ( month_of_birth < 13 and month_of_birth > 0): # The Condition to check if the entered month is valid or not !
            os.system('cls')
            pass
        else:
            print("Error, Your Birth Month Cannot Be {}!".format(month_of_birth))
            print("Try Again !")
            print("Hint- Look at the examples provided by the program ;)")
            Date_Of_Birth_Collector()

        print("Provide Me With The Day You Were Born: Eg- 13 ")
        day_of_birth = int(input("Enter The Day You Were Born: "))
        if (day_of_birth > 0 and day_of_birth < 33): # Condition to check date of birth !
            pass
        else:
            print("Error, Your Birth Day Cannot Be {}".format(day_of_birth))
            print("Try, Again!")
            print("Hint- Look at the examples provided by the program ;)")
            Date_Of_Birth_Collector()

    except ValueError:
        print("Value Error: You Must Have Entered Wrong Detail! "
              "\nPlease Read The Instructions Carefully Before Entering The Data".format())
        print("Hint We Only Accept Numeric Values, (Numbers)")
        Date_Of_Birth_Collector()

    finally:
        print("Well, Done Thanks For Entering The Data, Analyzing Your Data "
        "\nPlease Wait..........")

        # THE VALUE FOR DRIVER NUMBER !
        driver_number = str(day_of_birth)

        # Module To Find Out The Sum Of Conductor Number!

        conductor_number_string = str(birth_year) + str(month_of_birth) + str(day_of_birth)
        print("The Total Birth Number: {}".format(conductor_number_string))
        conductor_number = 0
        for x in range(len(conductor_number_string)):
            conductor_number = conductor_number + int(str(conductor_number_string[x]))
        print("The Sum of the conductor Number: {}".format(conductor_number))

        # Moudel to check whether the conductor number is greater then 1 ?

        if (len(str(conductor_number)) == 2):
            conductor_number = int(str(conductor_number)[0]) + int(str(conductor_number)[1])
        else:
            pass

        print("The Conductor Number is: {}!".format(conductor_number))

        # THE DRIVER NUMBER!
        if (len(driver_number) == 2):
            driver_number = int(str(day_of_birth)[0]) + int(str(day_of_birth)[1])
            driver_number = int(str(driver_number)[0]) # Making Sure There's Only 1 Driver Number,

        # Else, PASS
        else:
            pass

        print("The Driver Number is: {}".format(driver_number))
        first_note(int(driver_number),int(conductor_number))


def first_note(driver_number, conductor_number):
    print("Okay, So Let Me Firstly Make Your Clear About Driver Number And Conductor Number!")
    print("""
Driver Number: Leads our life, 
Conductor Number: Dealing with others in our life will be regulated through Conductor Number!
So try to find your Driver & Conductor and try to make combination and co-operation between 
Driver and Conductor, So that you face the challenges of the life very conveniently.
Always remember, The problems or obstacles demands change for the good or bad, which is a part of our 
life journey, nobody can escape from it” problems or obstacles will come, stay & Go but how we react on it,
that’s matter……\n""")

    print("Never Let A Astrologist Let Your Demotivated In Life, 'YOUR LIMITLESS!'")
    print("So, Your Driver Number Is: {}, ".format(driver_number))
    print("And Your Conductor Number Is: {}\n".format(conductor_number))

    if (driver_number == conductor_number):
        checking_the_user_input(driver_number)

    elif (driver_number != conductor_number):
        checking_the_user_input(driver_number)
        checking_the_user_input2(conductor_number)


def driver_number_1():
    print("Your Driver Number Describes Your Day To Day Life! ")
    print("Driver number '1' Sign = ('SUN')")
    print("Driver Number: 1 - ('BORN LEADERS !', This is how I will define driver number 1 in a word ;) )")
    print("\nSo, Folk Your Creative, You Have A Strong Determinative, Your A Researcher, Your Also A Good Administrator")
    print("Here's a brief explanation, ")
    print("""Sun rises everyday and is considered as the source of life’s creation. 
It comes at first place and hence is represented as number 1. As Sun is considered as lord of all planets 
People born on these dates possess true leadership qualities and they can do very well in politics. 
These people are strong headed and enjoy high repute in the society. 
These people are highly social and have good network of friends. They have the ability to make friends in flick of seconds, 
which lasts throughout their lifetime. They are highly disciplined and determined. Their approach towards life is very clear, 
being analytical and intelligent, they know how to achieve their goals. Sun gives them the power & fortune to rule. 
They can do very well in any stream or profession but the best suited for them are government roles,
administrative job, politician, publisher etc. Being highly dominating they may face issues in their married life 
but they are one the most honest and loyal partners.
In terms of health, Sun born people generally follow good health. they are more prone to high blood pressure,   
heat stroke, weak eyesight since young age, indigestions, heart and neuro related ailments.""")
    print("By The Way Here's A Little Tip To You, Offering water to Sun every morning will be very benefical to you ;)\n")

def driver_number_2():
    print("Your Driver Number Describes Your Day To Day Life! ")
    print("Driver Number: 2 - ('Sentiments!', This is how I will define driver number 2 in a word ;) )")
    print("And Your Driver Number Is: 2 = ('Moon')")
    print("So, Folk Your Imaginative, Artistic, And Romantic Too ")
    print("Here's A Breif Explanation, ")
    print("""
These people keep a very refined taste in art and beauty. 
Since they have good analytical skills so they do well in field of law, orator, advisory, artist, painter, 
musician etc. Businesses in fields of dairy products, cosmetics, chemicals, liquids also proves favorable 
for them. In terms of health, these people are more prone to diseases of stomach, mind and 
lungs like cold, cough, liver, gall bladder, kidney, depression, addiction etc. 
For better health, these people should avoid taking milk at night. 
Also, for healthy mind, they should keep water in a container by 
the side of their bed at night and pour that water early in the morning in the plants.\n""")

def driver_number_3():
    print("Your Driver Number Describes Your Day To Day Life! ")
    print("Driver Number: 3 - ('Vision!', This Is How I will Define Driver Number 3 in a word ;))")
    print("Driver Number: 3 Sign= ('Jupiter')")
    print("So, Folk Your, High aspirational, Can Also Be A Leader, A Controller, Your A Faithful Person, Your Also A Good Teacher ")
    print("Here's a Brief Explanation, ")
    print("""
Your highly ambitious, principled and determined. You do have a high sense of self-respect and 
are highly egoistic. You will achieve success in your profession or businesses but the best suited fields 
for you are teaching, writer, banking sector officials, high positions in govt departments, orators etc. 
You are religious at heart and follow your rituals very diligently. Your truly hilarious and have good 
network of friends. You will gain a lot through foreign travels. Family pride is of outmost importance to 
you. In terms of health, people having driver number 3 are more prone to diseases of obesity, liver, 
skin allergies, jaundice, arthritis and paralysis etc.\n""")

def driver_number_4():
    print("Your Driver Number Describes Your Day To Day Life! ")
    print("Driver Number: 4 - ('IDEAS'), This Is How I Will Define Driver Number 4 In A Word! ")
    print("Driver Number: 4 = ('Uranus')")
    print("So, Folk Your, A Debater, A Different Thought Person!")
    print("Here's A Brief Explanation, ")
    print("""
A ‘box full of ideas’ or ‘bundle of thoughts’ is the main characteristic of this number. 
When a person speaks on a particular topic and immediately switch over to another, in middle of nowhere, 
is an easy recognition of number 4. Because of so many thoughts running over their head at the same time, 
makes these people highly unorganized and messy in their personal lives. But when it comes to real life 
situations, they can accomplish surprising and most difficult assignments in a very normal way. 
They are great revolutionaries, scientists and politicians. They have suddenness of stunning events. 
They play leading role in a group or society but their arrogant and egoistic attitude makes them less 
friendly and always struggle in relationships. Scriptures, magic, research, religion and occult interest 
them a lot. Because of influence of Uranus, their life is full of struggle and hardships, which can be 
overcome only through hard work and following spirituality.

In terms of health, they may suffer from un-diagnosable diseases. Headaches, backaches and digestive 
disorders are some of the common problem with number 4 people.\n""")
def driver_number_5():
    print("Your Driver Number Describes Your Day To Day Life! ")
    print("Driver Number: 5 Sign = ('Mercury')")
    print("So, Folk Your, Friendly Nature Person, But Also A high tempered Person!")
    print("Here's A Brief Explanation, ")
    print("""
This is the most dynamic number of all numbers. This number is also known as the balancer number.  
These people possess very fertile mind and great business skills. They can revolutionize society 
with the kind of thinking they have. They are generally very busy people, as they understand the 
value of time. They have huge network of trustworthy and loyal friends. They are quick learners, 
multilingual and intellectual figures. In terms of profession, they prove to be a good businessman. 
They should choose industries like wireless and telecom, printing, transport, tourism, insurance, 
banking, budgeting, share trading, investors etc. They generally enjoy good health but are prone 
to diseases like insomnia, weakness in legs and hands.\n""")

def driver_number_6():
    print("Driver Number: 6 = Sign ('Venus')")
    print("So, Folk You Have The Power of attraction, Also the power to get love and respect, you also do love beautiful things")
    print("""
This number possesses high degree of life force. Girls of this number have very attractive personality 
and fond of fashionable clothes. These people have great interest in artistic things, music, dance, 
theater, films and designing. They generally live for only materialistic pleasures (luxuries) in life, 
which sometimes make them spend more than their earnings. They need to diligently work hard and control
their expenses. Students with this number have to put lot of efforts to get good education. They may face
property and money related issues or disputes. Family life is normal, sometimes may face differences with
father. They are frequent travellers and may travel around the world. Life is more or less satisfying.\n""")

def driver_number_7():
    print("Your Driver Number Describes Your Day To Day Life! ")
    print("Driver Number: 7 ('The Judge'), This Is How I Will Define Driver 7 In A Word!")
    print("Driver Number: 7 = Sign ('Saturn')")
    print("So, Folk You Have, the art of becoming a writer, artist. You Do Also take interest in outside world")
    print("Here's A Breif Explanation, ")
    print("""
According to Indian system The Lord of number 7 is ‘Ketu’.
It is very difficult to understand these people because they have several hidden secrets. 
Their site is piercing and dominating. They are well versed in reading the mind of others. 
They are art lovers, Studious with great interest in occult science and religious activities. 
They are visionary, farsighted and principle oriented people. They know how to take care of their time. 
They are serious people and wise spenders. They are lovers of solitude. They accomplish very high level 
of task and for that matter command respect in the society. Certainly they enjoy prosperous and happy life.
They are more prone to disease relating to nervous system disorder, respiratory, black patches under their 
eyes and also lungs related ones, Therefore, they should take food at proper time and should go out for 
walk on regular basis. Apple juice or other fruit juices are beneficial for them. In terms of profession, 
anything related to propagation of religious principles, writing books, publication business, watch making,
photography, pharmaceutical business, detective agency, travel air hostess, dairy farming or fish seller 
are appropriate rolls they can do.""")

def driver_number_8():
    print("Your Driver Number Describes Your Day To Day Life! ")
    print("Driver Number: 8 ('The Judge'), This Is How I Will Define Driver 8 In A Word!")
    print("Driver Number: 8 ('Saturn')")
    print("So, Folk You Have, the art of becoming a writer, artist. You Do Also take interest in outside world")
    print("Here's A Breif Explanation, ")
    print("""
This number is basically a karmic number of a person that means only hard work would bring success 
to their lives. Success doesn’t come by chance for this number, they may face lot of hardships and 
sufferings but their persistent hard work makes them successful in end. If a person of this number 
is not serious in life than they become more lazy and isolated. This number is ruled by Saturn, 
which means ‘a Judge’ of past karmas i.e. what had been sown in the past will reap now. They are best 
suited in roles of administrative jobs, judge, spiritual preachers, jailors, business of iron & steel, 
woolen clothes, mining and other labor intensive industries etc. These people should take special care 
of not cutting nails and hair on Saturdays, as they fall under the ambit of Saturn. Headaches, weak 
digestion, joint pains, intestinal trouble or stomach related ailments, are few common problem with 
number 8 people.""")

def driver_number_9():
    print("Your Driver Number Describes Your Day To Day Life! ")
    print("Driver Number: 9 ('Force'), This Is How I Will Define Driver 9 In A Word!")
    print("Driver Number: 9 Sign = ('Mars') ")
    print("So, Folk You Have Anger, low patience, work on inner motivation")
    print("""
Number 9 is ruled by ‘Mars’, which represents power and service. The power or force required to convert a 
plan into action, comes from Mars. These people are brave, courageous and commanding. They have high levels 
of energy and constantly on the go.The best professions to unleash their excessive energy are to put them 
in fields like Army, Police, bureaucrats, civil construction and anything related to heavy machinery etc. 
This is the most aggressive number among all and if impacted negatively by number, these people might adopt 
physical means to get their work done. This number rules over blood, bone marrow, digestive system, 
headaches, piles or urinary problems. They should regularly go for morning walks and keep away from items 
related to fireworks.""")

#def last_note():


def checking_the_user_input(driver_number):
    if(driver_number == 1):
        driver_number_1()
    elif (driver_number == 2):
        driver_number_2()
    elif (driver_number == 3):
        driver_number_3()
    elif (driver_number == 4):
        driver_number_4()
    elif (driver_number == 5):
        driver_number_5()
    elif (driver_number == 6):
        driver_number_6()
    elif (driver_number == 7):
        driver_number_7()
    elif (driver_number == 8):
        driver_number_8()
    elif (driver_number == 9):
        driver_number_9()
def checking_the_user_input2(conductor_number):
    if (conductor_number == 1):
        print("Your Conductor Number Describes Your Overall Life!")
        print("Conductor Number: {} Sign = ('Sun') ".format(conductor_number))
        print("Conductor Number: 1 - ('BORN LEADERS !', This is how I will define conductor number 1 in a word ;) )")
        print("So, Folk Your Creative, You Have A Strong Determinative, Your A Researcher, Your Also A Good Administrator")
        print("Here's a brief explanation, ")
        print("""Sun rises everyday and is considered as the source of life’s creation. 
        It comes at first place and hence is represented as number 1. As Sun is considered as lord of all planets 
        People born on these dates possess true leadership qualities and they can do very well in politics. 
        These people are strong headed and enjoy high repute in the society. 
        These people are highly social and have good network of friends. They have the ability to make friends in flick of seconds, 
        which lasts throughout their lifetime. They are highly disciplined and determined. Their approach towards life is very clear, 
        being analytical and intelligent, they know how to achieve their goals. Sun gives them the power & fortune to rule. 
        They can do very well in any stream or profession but the best suited for them are government roles,
        administrative job, politician, publisher etc. Being highly dominating they may face issues in their married life 
        but they are one the most honest and loyal partners.
        In terms of health, Sun born people generally follow good health. they are more prone to high blood pressure,   
        heat stroke, weak eyesight since young age, indigestions, heart and neuro related ailments.""")
        print(
            "By The Way Here's A Little Tip To You, Offering water to Sun every morning will be very benefical to you ;)")

    elif (conductor_number == 2):
        print("Your Conductor Number Describes Your Overall Life!")
        print("Conductor Number: 2 - ('Sentiments!', This is how I will define conductor number 2 in a word ;) )")
        print("Conductor Number: 2 Sign = ('Moon')")
        print("So, Folk Your Imaginative, Artistic, And Romantic Too ")
        print("Here's A Breif Explanation, ")
        print("""
These people keep a very refined taste in art and beauty. 
Since they have good analytical skills so they do well in field of law, orator, advisory, artist, painter, 
musician etc. Businesses in fields of dairy products, cosmetics, chemicals, liquids also proves favorable 
for them. In terms of health, these people are more prone to diseases of stomach, mind and 
lungs like cold, cough, liver, gall bladder, kidney, depression, addiction etc. 
For better health, these people should avoid taking milk at night. 
Also, for healthy mind, they should keep water in a container by 
the side of their bed at night and pour that water early in the morning in the plants.""")


    elif (conductor_number == 3):
        print("Your Conductor Number Describes Your Overall Life!")
        print("Your Conductor Number Is: {}".format(conductor_number))
        print("Conductor Number: 3 - ('Vision!)', This Is How I will Define Conductor Number 3 in a word ;))")
        print("Conductor Number: 3 Sign = ('Jupiter')")
        print("So, Folk Your, High aspirational, Can Also Be A Leader, A Controller, Your A Faithful Person, Your Also A Good Teacher ")
        print("Here's a Brief Explanation, ")
        print("""
Your highly ambitious, principled and determined. You do have a high sense of self-respect and 
are highly egoistic. You will achieve success in your profession or businesses but the best suited fields 
for you are teaching, writer, banking sector officials, high positions in govt departments, orators etc. 
You are religious at heart and follow your rituals very diligently. Your truly hilarious and have good 
network of friends. You will gain a lot through foreign travels. Family pride is of outmost importance to 
you. In terms of health, people having driver number 3 are more prone to diseases of obesity, liver, 
skin allergies, jaundice, arthritis and paralysis etc.""")

    elif (conductor_number == 4):
        print("Your Conductor Number Describes Your Overall Life!")
        print("Your Conductor Number Is: {}".format(conductor_number))
        print("Conductor Number: 4 - ('IDEAS', This Is How I Will Define Driver Number 4 In A Word! ")
        print("Conductor Number: 4 Sign = ('Uranus')")
        print("So, Folk Your, A Debater, A Different Thought Person!")
        print("Here's A Brief Explanation, ")
        print("""
A ‘box full of ideas’ or ‘bundle of thoughts’ is the main characteristic of this number. 
When a person speaks on a particular topic and immediately switch over to another, in middle of nowhere, 
is an easy recognition of number 4. Because of so many thoughts running over their head at the same time, 
makes these people highly unorganized and messy in their personal lives. But when it comes to real life 
situations, they can accomplish surprising and most difficult assignments in a very normal way. 
They are great revolutionaries, scientists and politicians. They have suddenness of stunning events. 
They play leading role in a group or society but their arrogant and egoistic attitude makes them less 
friendly and always struggle in relationships. Scriptures, magic, research, religion and occult interest 
them a lot. Because of influence of Uranus, their life is full of struggle and hardships, which can be 
overcome only through hard work and following spirituality.
In terms of health, they may suffer from un-diagnosable diseases. Headaches, backaches and digestive 
disorders are some of the common problem with number 4 people.""")

    elif (conductor_number == 5):
        print("Your Conductor Number Describes Your Overall Life!")
        print("Your Conductor Number Is: {}".format(conductor_number))
        print("Conductor Number: 5 - ('IDEAS', This Is How I Will Define Driver Number 4 In A Word! ")
        print("Conductor Number: 5 Sign = ('Uranus')")
        print("So, Folk Your, Friendly Nature Person, But Also A high tempered Person!")
        print("Here's A Brief Explanation, ")
        print("""
This is the most dynamic number of all numbers. This number is also known as the balancer number.  
These people possess very fertile mind and great business skills. They can revolutionize society 
with the kind of thinking they have. They are generally very busy people, as they understand the 
value of time. They have huge network of trustworthy and loyal friends. They are quick learners, 
multilingual and intellectual figures. In terms of profession, they prove to be a good businessman. 
They should choose industries like wireless and telecom, printing, transport, tourism, insurance, 
banking, budgeting, share trading, investors etc. They generally enjoy good health but are prone 
to diseases like insomnia, weakness in legs and hands.""")

    elif (conductor_number == 6):
        print("Your Conductor Number Describes Your Overall Life!")
        print("Conductor Number: 6 - ('IDEAS'), This Is How I Will Define Conductor Number 6 In A Word!")
        print("Conductor Number: 6 = Sign = ('Venus')")
        print("So, Folk You Have The Power of attraction, Also the power to get love and respect, you also do love beautiful things")
        print("""
This number possesses high degree of life force. Girls of this number have very attractive personality 
and fond of fashionable clothes. These people have great interest in artistic things, music, dance, 
theater, films and designing. They generally live for only materialistic pleasures (luxuries) in life, 
which sometimes make them spend more than their earnings. They need to diligently work hard and control
their expenses. Students with this number have to put lot of efforts to get good education. They may face
property and money related issues or disputes. Family life is normal, sometimes may face differences with
father. They are frequent travellers and may travel around the world. Life is more or less satisfying.""")

    elif (conductor_number == 7):
        print("Your Conductor Number Describes Your Overall Life!")
        print("Conductor Number: 7 ('Action'), This Is How I Will Define Driver 7 In A Word!")
        print("Conductor Number: 7 Sign = ('KETU')")
        print("So, Folk You Have, the art of becoming a writer, artist. You Do Also take interest in outside world")
        print("Here's A Breif Explanation, ")
        print("""
According to Indian system The Lord of number 7 is ‘Ketu’.
It is very difficult to understand these people because they have several hidden secrets. 
Their site is piercing and dominating. They are well versed in reading the mind of others. 
They are art lovers, Studious with great interest in occult science and religious activities. 
They are visionary, farsighted and principle oriented people. They know how to take care of their time. 
They are serious people and wise spenders. They are lovers of solitude. They accomplish very high level 
of task and for that matter command respect in the society. Certainly they enjoy prosperous and happy life.
They are more prone to disease relating to nervous system disorder, respiratory, black patches under their 
eyes and also lungs related ones, Therefore, they should take food at proper time and should go out for 
walk on regular basis. Apple juice or other fruit juices are beneficial for them. In terms of profession, 
anything related to propagation of religious principles, writing books, publication business, watch making,
photography, pharmaceutical business, detective agency, travel air hostess, dairy farming or fish seller 
are appropriate rolls they can do.""")

    elif (conductor_number == 8):
        print("Your Conductor Number Describes Your Overall Life!")
        print("Conductor Number: 8 ('The Judge'), This Is How I Will Define Driver 8 In A Word!")
        print("Conductor Number: 8 Sign = ('Saturn')")
        print("So, Folk You Have, the art of becoming a writer, artist. You Do Also take interest in outside world")
        print("Here's A Breif Explanation, ")
        print("""
This number is basically a karmic number of a person that means only hard work would bring success 
to their lives. Success doesn’t come by chance for this number, they may face lot of hardships and 
sufferings but their persistent hard work makes them successful in end. If a person of this number 
is not serious in life than they become more lazy and isolated. This number is ruled by Saturn, 
which means ‘a Judge’ of past karmas i.e. what had been sown in the past will reap now. They are best 
suited in roles of administrative jobs, judge, spiritual preachers, jailors, business of iron & steel, 
woolen clothes, mining and other labor intensive industries etc. These people should take special care 
of not cutting nails and hair on Saturdays, as they fall under the ambit of Saturn. Headaches, weak 
digestion, joint pains, intestinal trouble or stomach related ailments, are few common problem with 
number 8 people.""")

    elif (conductor_number == 9):
        print("Your Conductor Number Is: {}".format(conductor_number))
        print("Your Conductor Number Describes Your Overall Life!")
        print("Conductor Number: 9 ('Force'), This Is How I Will Define Driver 9 In A Word!")
        print("Conductor Number: 9 Sign = ('MARS') ")
        print("So, Folk You Have Anger, low patience, work on inner motivation")
        print("""
Number 9 is ruled by ‘Mars’, which represents power and service. The power or force required to convert a 
plan into action, comes from Mars. These people are brave, courageous and commanding. They have high levels 
of energy and constantly on the go.The best professions to unleash their excessive energy are to put them 
in fields like Army, Police, bureaucrats, civil construction and anything related to heavy machinery etc. 
This is the most aggressive number among all and if impacted negatively by number, these people might adopt 
physical means to get their work done. This number rules over blood, bone marrow, digestive system, 
headaches, piles or urinary problems. They should regularly go for morning walks and keep away from items 
related to fireworks.""")


#Calling The Required Method!
Date_Of_Birth_Collector()
os.system('PAUSE')
