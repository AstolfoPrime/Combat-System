import andrew_CS120_tbc as tbc

def main():
    hero = tbc.Character("Anonymous", 10, 5, 50, 5)
    monster = tbc.Character("CIA", 10, 3, 10, 5)
    tbc.fight(hero, monster)
if __name__ == "__main__":
    main()
