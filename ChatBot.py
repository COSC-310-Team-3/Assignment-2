import nltk
import tkinter
from tkinter import *
from nltk.chat.util import Chat, reflections



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
    mesWin.delete("1.0", END)
    reply = chatbot.converse(userInput)
    print(reply)
    
    

#generate the  and run the chat interface
def beginClick():
    begin.destroy()
    # place the Chat window
    chatWin.place(x=6, y=6, height=385, width=370)
    # place the message window
    mesWin.place(x=128, y=400, height=88, width=260)
    #Scroll bar for the Chat
    scroll = Scrollbar(root, command=chatWin.yview, cursor="star")
    scroll.place(x=375, y=5, height=385)
    #Button to send your message
    sendIn = Button(root, text="Send", width=12, height=5, bd=0, bg="#0080FF", activebackground="#00BFFF", foreground="#FFFFFF", font=("Arial", 12), command=sendClick)
    sendIn.place(x=6, y=400, height=88)

    
    

    

#this section is where the GUI will be built
root = Tk()
root.title("Chatbot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

#this section is textboxes that will be placed by the beginClick function
#chat window
chatWin = Text(root, bd=1, bg="black", width=50, height=8, font=("Arial", 25), foreground="#00FFFF")
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
    ['(.*) most gold medals?', ['Michael Phelps with 23.']]
]


#Entry Screen
#When this button is clicked it will call the beginClick function to generate the chat interface
chatbot = modifiedChat(pairs, reflections)

begin = Button(text="Click me to begin chatting with SportBot!", width=400, height=500, bg="black", fg="white", command=beginClick, font=("Arial", 12))
begin.pack()



#when the code reaches this point it begins to loop a chat


root.mainloop()
