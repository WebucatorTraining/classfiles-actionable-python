from datetime import date
from operator import itemgetter

def main():
    ww2_leaders = []
    ww2_leaders.append(
        {'fname':'Winston', 'lname':'Churchill', 'dob':date(1889,4,20)}
    )
    ww2_leaders.append(
        {'fname':'Charles', 'lname':'de Gaulle', 'dob':date(1883,7,29)}
    )
    ww2_leaders.append(
        {'fname':'Adolph', 'lname':'Hitler', 'dob':date(1890,11,22)}
    )
    ww2_leaders.append(
        {'fname':'Benito', 'lname':'Mussolini', 'dob':date(1882,1,30)}
    )
    ww2_leaders.append(
        {'fname':'Franklin', 'lname':'Roosevelt', 'dob':date(1884,12,30)}
    )
    ww2_leaders.append(
        {'fname':'Joseph', 'lname':'Stalin', 'dob':date(1878,12,18)}
    )
    ww2_leaders.append(
        {'fname':'Hideki', 'lname':'Tojo', 'dob':date(1874,11,30)}
    )

    ww2_leaders.sort(key=itemgetter('dob'))
    print('First born:', ww2_leaders[0]['fname'])

    ww2_leaders.sort(key=itemgetter('lname', 'fname'))
    print('First in Encyclopedia:', ww2_leaders[0]['fname'])

main()