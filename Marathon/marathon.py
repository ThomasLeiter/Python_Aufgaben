import csv
from sorting_algorithm import merge_sort,quick_sort
class MarathonRunner:
    """A class to store the data of each marathon runner."""

    def __init__(self,Dict):
        self.Id = Dict['Start NR']
        self.FirstName = Dict['Vorname']
        self.LastName = Dict['Name']
        self.Time = Dict['Zeit']
        self.Sex = Dict['Geschlecht']
    
    def get_time_seconds(self):
        """Calculates and returns the running time in full seconds."""
        time_tpl = self.Time.split(':')
        return int(time_tpl[0])*3600 + int(time_tpl[1])*60 + int(time_tpl[2])

    def __le__(self,other):
        return self.get_time_seconds() <= other.get_time_seconds()

    def __gt__(self,other):
        return not self<=other
    
    def __eq__(self,other):
        return self<=other and other<=self

    def __ge__(self,other):
        return other<=self and not self==other
    
    def __lt__(self,other):
        return not self>=other

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
    
    def __repr__(self):
        return f"{self.Id},{self.LastName},{self.FirstName},{self.Time}"

def read_file_and_print_winners(filename,sorting_function):
    """
    Read given csv file and print winners of the race.
    Sorting is done via sorting_function.
    """
    with open(filename,'r',encoding="utf8") as file:
        data = csv.DictReader(file,delimiter=';')
        lst = [MarathonRunner(row) for row in data]
        sorted_lst = sorting_function(lst)
        # Find Winner
        winner = sorted_lst[0]
        # Find best Male and Female
        best_male,best_female = None,None
        for r in sorted_lst:
            if r.Sex=='m':
                best_male = r
                break
        for r in sorted_lst:
            if r.Sex=='w':
                best_female = r
                break
        print(f"GesamtsiegerIn: {winner}")
        print(f"Sieger Herren:  {best_male}")
        print(f"Siegerin Damen: {best_female}")
        print("LäuferInnen mit Laufzeit zwischen 2,5 und 3 Stunden:")
        for r in sorted_lst:
            if r.get_time_seconds()>=9000 and r.get_time_seconds()<=10800:
                print(f" {r.__repr__()}")

if __name__ == '__main__':
    # Read the file 'marathon.csv' and process its contents
    read_file_and_print_winners('./Marathon/marathon.csv',merge_sort)
    #read_file_and_print_winners('./Marathon/marathon.csv',quick_sort)