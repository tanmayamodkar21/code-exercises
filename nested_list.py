if __name__ == '__main__':
    
    Student = []
    Lscore = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Student.append([name , score])
        Lscore.append(score)
        
    seclast = sorted(set(Lscore))[1]
    for i,j in sorted(Student):
        if j == seclast:
            print(i)