import argparse

#Dzieli wiersz o kodzie |qx| na 3 inne wiersze
def split_qx(line, result):
    if(line[0:2] == 'qx'):
        result.write("Nowa rozgrywka" + '\n')
        split = line.split("pc")
        split_deal(split[0], result)
        result.write('Gra' + '\n')
        for element in range(1, len(split)):
            if element == len(split)-1:
                result.write(split[element].translate({ord(i): None for i in '|pg'}))
            else:
                result.write(split[element].replace('|','') + '\n')

def split_deal(element, result):

    split = element.split("mb")

    for part in split:
        if part[0:2] == 'qx':
            result.write('Rozdanie' + '\n' + part + '\n' + 'Licytacja' + '\n')
        else:
            result.write(part.replace('|','') + '\n')


#Szuka kodu "|pc|", po czym zapisuje do pliku wyłożoną kartę
def search_the_pc_code(line, result, character):
    if (line[character] == 'p' and line[character + 1] == 'c'):
        result.write(line[character + 3] + line[character + 4] + '\n')


#Szukanie danych podczas rozgrywki
def play_format(line, result):
    if (line[0:2] == "pc"):
        for character in range(len(line)):
            search_the_pc_code(line, result, character)

#Funkcja wywoławcza
def main(data_file):

    with open(data_file) as file:
        with open("results3.txt", "a") as result:
            for line in file:
                split_qx(line,result)
                play_format(line, result)



if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='Podaj sciezke do pliku z danymi', dest="filename", required=True)
    args = parser.parse_args()

    main(args.filename)