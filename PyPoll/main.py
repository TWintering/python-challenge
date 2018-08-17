import csv

candidates=[]
votes=[]
candidate_votes={}
win_votes=0

with open('election_data.csv',newline='') as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        vote=row[2]
        votes.append(vote)
        if vote not in candidates:
            candidates.append(vote)
num_votes=len(votes)


print('Election Results')
print('-------------------------')
print('Total Votes: %d' % (num_votes))
print('-------------------------')

with open('poll_output.txt','w') as txt: 
    txt.write('Election Results\n')
    txt.write('-------------------------\n')
    txt.write('Total Votes: %d\n' % (num_votes))
    txt.write('-------------------------\n')
    for i in range(len(candidates)):
        name=candidates[i]
        num=votes.count(candidates[i])
        percent=(num / num_votes) * 100
        if num > win_votes:
            winner=candidates[i]
            win_votes=num
        print('%10s: %10.3f%%   (%d)' % (name,percent,num))
        txt.write('%10s: %10.3f%%  (%d)\n' % (name,percent,num))
    print('-------------------------')
    txt.write('-------------------------\n')
    print('Winner: %s' % (winner))
    txt.write('Winner: %s\n' % (winner))
    print('-------------------------')
    txt.write('-------------------------\n')
txt.close()




