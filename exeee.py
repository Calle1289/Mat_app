from HTML_matspar import livsmedel_lista_lista as matspar_lista
from API_livsmedelsverket import livsmedel_lista as livsmedelsverket_lista
from thefuzz import process
from thefuzz import fuzz
from pprint import pprint as pp

counter = 0
for i in list(livsmedelsverket_lista.keys()):
    score2 = process.extractOne(i, matspar_lista.keys(), scorer=fuzz.token_sort_ratio)
    score3 = process.extractOne(i, matspar_lista.keys(), scorer=fuzz.ratio)
    max_score = max([score2, score3], key=lambda x: x[1])

    if i.split()[0].lower() in [
        score.split()[0].lower() for score in [score2[0], score3[0]]
    ]:
        for score in [score2, score3]:
            if i.split()[0].lower() == score[0].split()[0].lower() and score[1] >= 60:
                livsmedelsverket_lista[i] = (
                    livsmedelsverket_lista[i]
                    | matspar_lista[score[0]]
                    | {"score_name":score[0],"score": score[1]}
                )
                break
    elif (
        (score2[1] + score3[1]) / 2 >= 60
        and score2[1] >= 70
        or score3[1] >= 70
    ):
        if i.split()[0].lower() not in [
            score.split()[0].lower() for score in [score2[0], score3[0]]
        ]:
            livsmedelsverket_lista[i] = (
                livsmedelsverket_lista[i]
                | matspar_lista[max_score[0]]
                | {"score_name":max_score[0],"score": max_score[1]}
            )
    counter += 1
pp('Done')