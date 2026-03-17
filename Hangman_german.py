import random

words = [
    # A
    "affe", "apfel", "arbeit", "ast", "aufgabe", "auge", "auto", "abend", "antwort", "anzug",
    "arzt", "ausflug", "anfang", "angst", "arm", "acht", "adler", "ameise",
    # B
    "baum", "berg", "bett", "bild", "blatt", "blume", "boot", "brot", "buch",
    "burg", "butter", "bach", "ball", "bank", "brief", "bruder", "boden",
    # C
    "computer",
    # D
    "dach", "dorf", "dose", "draht", "dunkel", "dusche",
    # E
    "ei", "eis", "eimer", "ente", "erde", "esel",
    # F
    "faden", "farbe", "feder", "fenster", "feuer", "finger", "fisch", "flasche", "fluss",
    "frosch", "fuchs", "fuss",
    # G
    "gabel", "garten", "glas", "grenze", "gruppe", "gurke",
    # H
    "hals", "hand", "haus", "heft", "herz", "himmel", "holz", "hund", "hunger", "hut",
    "hafen", "hammer", "hahn", "hase",
    # I
    "igel", "insel",
    # J
    "jacke", "jahr", "junge",
    # K
    "katze", "kind", "kirche", "kissen", "kleid", "knochen", "kopf", "korb",
    "kuh", "kunst", "karte", "kerze",
    # L
    "lampe", "land", "leder", "leiter", "licht", "lippe", "luft", "lunge",
    # M
    "mond", "maus", "messer", "milch", "mitternacht", "morgen", "mutter", "mauer", "meer",
    # N
    "nadel", "nase", "nacht", "nebel", "nest", "netz",
    # O
    "ofen", "ohr", "onkel",
    # P
    "pfanne", "pferd", "pflanze", "pilz", "platz", "puppe",
    # Q
    "quelle",
    # R
    "rad", "regen", "ring", "rose", "ruhe",
    # S
    "sand", "schaf", "schloss", "schnee", "schule", "schwein", "see", "seife", "sonne",
    "stein", "stern", "stift", "strasse", "stuhl", "suppe",
    # T
    "tasche", "tasse", "tisch", "turm", "topf", "traum", "tiger",
    # U
    "uhr", "ufer",
    # V
    "vogel", "volk", "vater",
    # W
    "wand", "wasser", "weg", "wein", "welt", "wolke", "wurzel", "wurm", "wald", "wiese",
    # Z
    "zahn", "zaun", "zeit", "zelt", "ziege", "zimmer", "zunge",
]

hangman_stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

randomword = random.choice(words)
# print("\n" + randomword)
# makes a list containing each letter of the random word
letters_in_randomword = set(randomword)


def userinput():
    display = '_ ' * len(randomword)
    guessed_letters = []  # creates a list of guessed letters
    # max_wrong needs to be number 6 on the list, but because lists start with index 0 and length with index 1 total length of hangman_stages needs to be -1 to get to 6.
    max_wrong = len(hangman_stages) - 1
    n = 1
    print("\n" + display)
    while n <= max_wrong:
        letter = input("\nGuess a letter: ").lower()

        if not letter.isalpha():
            print("\nOnly letters allowed!")
        elif letter in guessed_letters:
            print("\nLetter already used!")
        elif len(letter) != 1:
            print("\nOnly one letter allowed!")
        else:
            guessed_letters.append(letter)
            if letter in letters_in_randomword:
                display = ""
                for char in randomword:
                    if char in guessed_letters:
                        display += char + " "
                    else:
                        display += "_ "
                print("")
                print(display)
                print(f"\nused: {str(sorted(guessed_letters))}")
                if "_ " not in display:
                    print("\nYOU WIN!\n")
                    print(f"The Word was: {str(randomword)}\n")
                    return

            else:
                print(hangman_stages[n])
                print(" ")
                print(display)
                print(f"\nused: {str(sorted(guessed_letters))}")
                n += 1
    print("""   
        L               L    
            O       O
                S
            T       T
        !                !
                    """)
    print(f"The Word was: {str(randomword)}\n")


userinput()
