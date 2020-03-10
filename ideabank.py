# Put your code here
def main():
    idea_list = []
    menu(idea_list)

def menu(idea_list):
    print("_"*30)
    print("           IdeaBank")
    print("_"*30)
    menu_number = input("Please chose option: \n 1 - Show idea list\n 2 - Add new idea\n 3 - Remove idea\n You can always exit Idea bank by pressing CRT+C\n")
    menu_choose(menu_number, idea_list)

def menu_choose(menu_number, idea_list):
    if menu_number == "1":
        idea_list_print(idea_list)
    elif menu_number == "2": 
        idea_list_add()
    elif menu_number == "3": 
        idea_list_del()

        
def idea_list_print(idea_list):
    print(idea_list)

def idea_list_add():
    new_idea = input("What is Your new idea?")
    idea_list.append(new_idea)
    print(idea_list)

def idea_list_del():
    pass


















if __name__ == '__main__':
    main()
