import csv, time

def my_sort(lst,key=lambda x: x):
    if len(lst)<=1:
        return lst
    pivot = key(lst[len(lst)//2])
    lo = [x for x in lst if key(x)<pivot]
    pi = [x for x in lst if key(x)==pivot]
    hi = [x for x in lst if key(x)>pivot]
    return my_sort(lo,key) + pi + my_sort(hi,key)

def read_file(filename):
    with open(filename,'r',encoding='utf8') as file:
        lst_of_runners = list(csv.DictReader(file,delimiter=';'))
        lst_of_runners = my_sort(
            lst_of_runners,
            key=lambda r: time.strptime(r['Zeit'],"%H:%M:%S"))
        winner = lst_of_runners[0]
        best_m = [r for r in lst_of_runners if r['Geschlecht']=='m'][0]
        best_w = [r for r in lst_of_runners if r['Geschlecht']=='w'][0]
        print(f"GesamtSiegerIn: {winner['Vorname']} {winner['Name']}")
        print(f"Sieger Herren:  {best_m['Vorname']} {best_m['Name']}")
        print(f"Siegerin Damen: {best_w['Vorname']} {best_w['Name']}")
        lo,hi = time.strptime('2:30:00',"%H:%M:%S"),time.strptime('3:00:00',"%H:%M:%S")
        subset = [
            r for r in lst_of_runners 
            if  time.strptime(r['Zeit'],"%H:%M:%S")>=lo
            and time.strptime(r['Zeit'],"%H:%M:%S")<=hi]
        for r in subset:
            print(f"{r['Start NR']:>4s}: {r['Vorname']:15s} {r['Name']:15s} {r['Zeit']:>8s}")

if __name__=='__main__':
    read_file('marathon.csv')