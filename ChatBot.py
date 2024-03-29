
import nltk
import tkinter
from tkinter import *
from nltk.chat.util import Chat, reflections
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize

# This is a modified converse function from nltk.chat.util
class modifiedChat(Chat):
    def converse(self, user_input):
        while user_input[-1] in "!.":
            user_input = user_input[:-1]
        return self.respond(user_input)

####################################################################
# The following is our chatbot implementation                      #
####################################################################
                


#this section is functions

#this function ends the window
def kill():
    root.destroy()
    
#this function creates the menu
def makeMenu():
    mainMenu = Menu(root)
    mainMenu.add_command(label = "Quit", command=kill)
    root.config(menu=mainMenu)
    
#This function retrieves the userInput and then passes it to the console
def sendClick():     
    userInput = mesWin.get("1.0", END)
    userInput = userInput.lower();
    text = word_tokenize(userInput);
    print(nltk.pos_tag(text));
    mesWin.delete("1.0", END)
    reply = chatbot.converse(userInput)
    output = ""
    chatWin.configure(state="normal")
    if "To begin" in chatWin.get("1.0", END):
        chatWin.delete("1.0", END)
        output = userInput + "\n                        " + reply + "\n"
    else:
        output = "\n" + userInput + "\n        " + reply + "\n"
    chatWin.insert(END, output)
    chatWin.see(END)
    chatWin.configure(state="disabled")
    
    

#generate the  and run the chat interface
def beginClick():
    begin.destroy()
    # place the Chat window
    chatWin.place(x=6, y=6, height=385, width=562.5)
    # place the message window
    mesWin.place(x=128, y=400, height=88, width=440)
    mesWin.place(x=6, y=400, height=88, width=440)
    #Button to send your message
    sendIn = Button(root, text="Send", width=12, height=5, bd=0, bg="#0080FF", activebackground="#00BFFF", foreground="#FFFFFF", font=("Arial", 12), command=sendClick)
    sendIn.place(x=455, y=400, height=88)

    
    

    

#this section is where the GUI will be built
root = Tk()
root.title("Chatbot")
root.geometry("575x500")
root.resizable(width=FALSE, height=FALSE)

#this section is textboxes that will be placed by the beginClick function
#chat window
chatWin = Text(root, bd=1, bg="black", width=50, height=8, font=("Arial", 25), foreground="#00FFFF", wrap=WORD)
chatWin.insert(END, "To begin chatting type your message into the textbox on the bottom\n")
chatWin.configure(state="disabled")
#Message window
mesWin = Text(root, bd=0, bg="black",width="30", height="4", font=("Arial", 23), foreground="#00ffff")


#generate the menu at the top
makeMenu()



#these are conversation pairs
pairs = [
    ['Hello|Hi', ['Hi, what is your name?']],
    ['my name is (.*)', ['Hello %1, my name is sports bot. Do you play any sports']],
    ['(.*) play (.*)', ['Thats so cool! I used to play %2 as well. Do you watch %2?']],
    ['yes, i watch (.*)', ['Who is your favourite player?']],
    ['No, i do not watch (.*)', ['Really? What sport do you watch']],
    ['i watch (.*)', ['Who is your favourite player?']],
    ['my favourite player is (.*)', ['%1? I have never heard of him, how many points a game do they score?']],
    ['(.*) scores (.*)', ['Thats not too bad but I bet I could beat him 1 on 1']],
    ['No you could not', ['Yes I could, how many points can you score in your sport?']],
    ['Yes you could', ['I know, how many points can you score in your sport?']],
    ['I can score (.*)', ['You can score %1? How old are you?']],
    ['i am (.*) years old', ['I guess thats not bad for a %1 year old. Is there anything you want to ask me regarding sports?']],
    ['(.*) favourite sport?', ['Hockey, anything else?']],
    ['(.*) old are you?', ['I am a bot I do not age']],
    ['(.*) favourite player?', ['Loui Erikkson of the Vancouver Canucks, he definitely deserves his $36 million contract']],
    ['(.*) to a game?', ['No, I am a bot. I am unable to be physically anywhere.']],
    ['(.*) Stanley Cup this year?', ['Any team but Vancouver']],
    ['(.*) watch the game last night?', ['I did not watch it, but all the stats automatically uploaded to my personal hard drive']],
    ['(.*) next summer olympics?', ['This summer in Tokyo']],
    ['(.*) next winter olympics?', ['2022 in Beijing']],
    ['(.*) most gold medals?', ['Michael Phelps with 23.']],
    ['how are you?', ['I am well. And you?']],
    ['i am (.*)', ['Alright']],
    ['when is the next world cup?', ['Next year in Qatar']],
    ['who will win the next world cup?',['Canada, no doubt. They are a soccer powerhouse']],
    ['who are you', ['I am sports bot. It is my duty to assist you in anything related to sports.']],
    ['(.*) favourite team?', ['I have no allegiance to any sports organization']],
    ['(.*) favourite basketball player?', ['The legend Alex Caruso']],
    ['(.*) favourite goal of all time?', ['Any of Loui Erikksons empty nets']],
    ['who is the most well known canadian hockey player', ['That is Wayne Gretzky easily']],
    ['how many hockey players can you name', ['I can name about 10 or so do you want me to name them all?']],
    ['yes name them all', ['Okay then we have Wayne Gretzky, Sidney Crosby, Alexander Ovechkin, Patrick Kane, Jonathan Toews, Steven Stamkos, Robert Orr, Gordie Howe, P. K. Subban, and finally Tim Hortons']],
    ['who made you (.*)', ['I was made by Keegan Wright, Jivraj Grewal, Owen Spicker, Brenden Trieu, and Hassan Brar']],
    ['what year is it', ['The current year is 2021 as of my last update']],
    ['what stopped sports last year', ['The COVID-19 pandemic halted everything for a while but we are slowly recovering']],
    ['(.*) do you think i will get better if i practice sports', ['As they say practice makes perfect but remember Rome was not built in a day so it may take some time']],
    ['(.*) win the premier league this year?',['It is looking increasingly likely that Manchester City will win the title.']],
    ['what is the premier league?', ['The Premier League is the top division of soccer in England.']],
    ['(.*) best premier league team?', ['All time, Manchester United have won the most titles. But more recently, Manchester City']],
    ['(.*) most premier league goals?', ['Alan Shearer, with 260 goals']],
    ['what is the champions league?', ['The UEFA Champions League is an annual soccer competition consisting of the best teams in Europe.']],
    ['(.*) win the champions league this year?', ['At this point, it is too close to determine.']],
    ['(.*) best champions league team?', ['All time, Real Madrid have been the most successful team with 13 titles.']],
    ['(.*) most champions league goals?', ['Cristiano Ronaldo, with 134 goals and counting']],
    ['(.*) favourite soccer player?', ['Adebayo Akinfenwa']],
    ['(.*) best soccer player ever?', ['Many have said Pele, however no one has ever been as good as Messi']],
    ['(.*) best soccer team in Canada?', ['Vancouver Whitecaps']],
    ['(.*) best canadian soccer player?', ['Alphonso Davies']],
    ['(.*)', ['Sorry can you try again I do not understand']],
    ['', ['Sorry can you try again I do not understand']]
]


#Entry Screen
#When this button is clicked it will call the beginClick function to generate the chat interface
chatbot = modifiedChat(pairs, reflections)

begin = Button(text="Click me to begin chatting with SportBot!", width=400, height=500, bg="white", fg="black", command=beginClick, font=("Arial", 20))
begin.pack()


#when the code reaches this point it begins to loop a chat


root.mainloop()