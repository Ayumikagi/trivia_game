from textwrap import dedent

def q(question):
    A = B = C = None
    if question == 1: 
        A = True
        B = C = False
        print(dedent('''
What color is red?

[A. Red] [B. Blue] [C. Green]
'''))
    elif question == 2:
        C = True
        A = B = False
        print(dedent('''
What does the letter S mean on a compass?

[A. North] [B. South Park] [C. South]
'''))
    elif question == 3:
        A = True
        B = C = False
        print(dedent('''
Who barks?

[A. Dogs] [B. Cats] [C. Your neighbor at 3am]
'''))
    elif question == 4:
        A = True
        B = C = False
        print(dedent('''
What is an iron shield made of?

[A. Iron] [B. Wood] [C. Plastic]
'''))
    elif question == 5:
        B = True
        A = C = False
        print(dedent('''
What comes after today?

[A. Yesterday] [B. Tomorrow] [C. Fromday]
'''))
    return A, B, C