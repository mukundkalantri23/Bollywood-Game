import random

f = open("movie_names.txt","r")
for x,name in enumerate(f,1):
    donothing = 0 # just a useless empty assignment to make the for loop work
maxrange = x
f.close()

ex = "N"
movie = ""
donemovies = []

while ex == "N" or ex == "n":
    print("Press 1 to play a new game.")
    print("Press 2 to add a movie into the movie list.")
    print("Press 3 to exit.\n")


    def newgame():
        count = 0
        contplaying = "Y"
        while contplaying == "Y" or contplaying == "y":
            if (count<maxrange):
                f = open("movie_names.txt","r")
                findnew = "Y"
                while findnew == "Y":
                    findnew = "N"
                    number = random.randint(1,maxrange) 
                    if number in donemovies:
                        findnew = "Y"       
                donemovies.append(number)
                for x,name in enumerate(f,1):
                    if x == number:
                        movie = name
                f.close()
                movie = movie.strip().upper();
                length = len(movie);
                game = list(("_"));
                for i in range(1,length):
                    game.append("_");

                bolly = list(('B','O','L','L','Y','W','O','O','D'))
                for i in range(0,length):
                    if movie[i] == 'A':
                        game[i] = 'A';
                    elif movie[i] == 'E':
                        game[i] = 'E';
                    elif movie[i] == 'I':
                        game[i] = 'I';
                    elif movie[i] == 'O':
                        game[i] = 'O';
                    elif movie[i] == 'U':
                        game[i] = 'U';
                    elif movie[i] == ' ':
                        game[i] = ' ';

                show="";
                for i in range(0,length):
                    show += game[i]+" ";

                print(show);
                print();
                answer = "";

                while(answer != movie and len(bolly)!=0):
                    print("enter an alphabet");
                    alpha = str(input()).upper();
                    flag = 0;
                    if(len(alpha)==1):
                        for i in range(0,length):
                            if(movie[i] == alpha):
                                game[i] = alpha;
                                flag = 1;

                        if(flag == 0):
                            bolly.pop(len(bolly)-1);
                        answer="";
                        show = "";
                        for i in range(0,length):
                            show += game[i]+" ";
                            answer += game[i];         
                        chances="";
                        for i in range(0,len(bolly)):
                            chances += bolly[i]+" ";

                        print(show+"                    "+"chances left:  "+chances);
                        print("");

                    else:
                        print("enter a single letter!");

                if(answer == movie):
                    print("CONGRATS! YOU WIN!");
                if(len(bolly) == 0):
                    print("SORRY, YOU LOSE! BETTER LUCK NEXT TIME!");

                acount = count+1
                contplaying = input("Do you want to continue playing? (Enter 'y' if yes)")
            
            else:
                print("All movies from the movie list are done! Stop playing and do some work now!")
                contplaying == "N"

    def addmovie():
        password = input("Enter password to access file: ")
        if password == "pass":
            f = open("movie_names.txt","a")
            newmovie = input("Enter movie name to add in the list: ")
            print()
            newmovie = "\n"+newmovie
            f.write(newmovie)
            n = n+1
            f.close()

    choice = input("Enter your choice:")
    if choice == "1":
        newgame()
    elif choice == "2":
        addmovie()
    elif choice == "3":
        ex = input("Are you sure you want to exit? Enter 'Y' if you want to exit ")
        if ex == "Y" or ex == "y":
            exit()
    else:
        print("Enter a valid choice!")

