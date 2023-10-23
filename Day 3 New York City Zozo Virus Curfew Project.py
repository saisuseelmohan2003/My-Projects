print("Hello !!!")
print("Welcome to New York!")
print("There has been a curfew in entire new york city due to the spread of new virus 'Zozo'.")
print("People are ordered to stay inside their house.")
print("Police are not allowing the citizens to roam outside.")
print("""
____            ____            ____
                   /....\          /....\          /.....|
           .-.    |::::::|    .-. |::::::|    .-. |::::::|
           | |    |::::::|    | | |::::::|    | | |::::::|
           | |    (`:'':')    | | (`:'':')    | | (`:'':')
           | |   _--|__|--__  | |.--|__|--__  | |_--|__|--__
           | |  |   ________|_|_|_  ________|_|_|_  ________|_____
           | | /    |            |  |            |  |            |
           | |/  /  |            |  |            |  |            |
           |_| |/|  |            |  |            |  |            |
          (===)| |  |  POLICE    |  |  POLICE    |  |  POLICE    |
          `==='  |`-|            |`-|            |`-|            |
           | |   |`-|            |`-|            |`-|            |
           |_|   |  |            |  |            |  |            |
                 |  |            |  |            |  |            |
                 |  |            |  |            |  |            |
                 |`-|            |`-|            |`-|            |
                 |__|            |__|            |__|            |
                 /_ |            |_ |            |_ |            |
                |___`-__________-'__`-__________-'__`-__________-'
                """)

print("You are only allowed to  'buy medicines', 'buy groceries', 'go to hospital'.")
need=input("Why do you want to come out of your house? ")
if need == "buy medicines":
    print("You are allowed to go!","Go to your house as soon as you buy medicines!!!",sep="\n")
    print("""| `--'           `--'   `---'         `-'           |
|         ,--,     |        |     |       |  |      |
|        / __ ,--. |-       |  |  |  ,--. |  |      |
|       (   |(---' |        |  |  | (---' |  |      |
|        `--' `--' `--'     `--^--'  `--' `- `-     |
|             ,---.                    | |          |
|            (____   ,--.  ,--.  ,--.  | |          |
|                 ) (    )(    ) |  |  ' '          |
              `--'   `--'  `--'  '  '  o o""")
elif need == "buy groceries":
    print("You are allowed to go!","Go to your house as soon as you buy groceries!!!",sep="\n")
    print("""  
 __________________________________________________________________________
|: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : |
| : : : : : : : : : : : : : : : :_________________________: : : : : : : : :|
|: : : : : : : : : : : : : : : _)                         (_ : : : : : : : |
| : : : : : : : : : : : : : : )_ :  Grocery Shop        :  _( : : : : : : :|
|: : Elevator  : : : :__________)_________________________(__________  : : |
| _____________ : _ :/ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ\: _ :|
||  _________  | /_\ '.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.' /_\ |
|| |    |    | |:=|=: |Flowers * Perfumes________Groceries * Candles| :=|=:|
|| |    |    | | : : :|   ______    _  .'         '.  _    ______   |: : : |
|| |    |    | |======| .' ,|,  '. /_\ |           | /_\ .'  ,|, '. |======|
|| |    |    |:|Lounge| | ;;;;;  | =|= |           | =|= |  ;;;;; | |Casino|
|| |    |    | |<---  | |_';;;'_n|     |  n______  |     |$_';;;'_| |  --->|
|| |    |    | |      | |_|-;-|__|     |-|_______|-|     |__|-;-|_| |      |
|| |    |    | |      | |________|     |           |     |________| |      |
|| |    |    | |      |                |           |                |      |
lc_|____|____|_|______|________________|           |________________|______|""")
elif need == "go to hospital":
    happen=input("What happened to you?")
    happen=happen.lower()
    if "zozo" in happen:
        print("Please urgently rush him to the hospital!")
        print('''       .---------.
       _    |:: [-=-] |
      | |   |_________|
      |~|
      |_|                    ,;;;;,
       I\  ,__ ,;;;, __,    ///  |||
       I |{   / . . \   }   / "  \|||
       I | ) (   _   ) (    \_= _///
       I |{___'-. .-'___}\___ )_/
       I ||~/,'~~~~~,\~~|'---((  /
       I \ //         \ |     \ \ /
       I  \/         // |     | /-/
       I (/         (/  |     |/|||
       I  |             |     |    |
       I  |             |     |____/
       I  :-----_o_-----:      || |
       I  | /~~|===|~~\ |      (( |
       I  ||   |===|   ||      ||_/
      /^\ "~   '^^^'   ""     ((__|
                                        ''')
    else:
        print("You can go to hospital")
        print(""" 
     oo
     .U
   __=__                        ,,,   
  |.  __|___                    oo ; 
  ||_/  /  /                    U= _  0
  \_/__/__E   o                 /. .| |
   (___ ||    |~~~~~~~~~~~~~~~~'----'~|
   I---|||    |-----------------------|
   I   |||    |       c(__)           |
   ^   '--''  ^                       ^
   """)
else:
    print("You are arrested for violating curfew rules!")
    print("""  _________________________
     ||   ||     ||   ||
     ||   ||, , ,||   ||
     ||  (||/|/(\||/  ||
     ||  ||| _'_`|||  ||
     ||   || o o ||   ||
     ||  (||  - `||)  ||
     ||   ||  =  ||   ||
     ||   ||\___/||   ||
     ||___||) , (||___||
    /||---||-\_/-||---||\  """)
          

    
