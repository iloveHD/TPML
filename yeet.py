import csv,io,sys
players = {}
teams = {}
szns = []
f = open('readme.txt','r')
lines = f.readlines()
f.close()
for line in lines[8:]:
  szns.append(int(line))
szns.sort()
if int(sys.argv[1]) in szns:
  print('this season is already included dumb dumb\n')
  sys.exit()
szns.append(sys.argv[1])
try:
  with open('playerwins.csv', newline='') as csvfile:
    readmedaddy = csv.reader(csvfile, delimiter=',')
    for player in readmedaddy:
      players[player[0]] = [int(player[1]),int(player[2])]
    csvfile.close()
except: pass
with open('teams{}.csv'.format(sys.argv[1]), newline='') as csvfile:
  readmedaddy = csv.reader(csvfile, delimiter=',')
  for team in readmedaddy:
    tem_name = team[0]
    teams[tem_name] = []
    for i in range(1,5):
      teams[tem_name].append(team[i])
      players[team[i]] = players.get(team[i],[0,0])
  csvfile.close()
with open('scores{}.csv'.format(sys.argv[1]), newline='') as csvfile:
  readmedaddy = csv.reader(csvfile, delimiter=',')
  i = 0
  for line in readmedaddy:
    if i%4 == 0:
      tem_1_nem = line[0]
      tem_1_scr = line[2]
    elif i%4 == 1:
      tem_2_nem = line[0]
      tem_2_scr = line[1]
    elif i%4 == 2:
      if tem_1_scr > tem_2_scr:
        for player in teams[tem_1_nem]:
          players[player][0] += 1
        for player in teams[tem_2_nem]:
          players[player][1] += 1
      elif tem_2_scr > tem_1_scr:
        for player in teams[tem_2_nem]:
          players[player][0] += 1
        for player in teams[tem_1_nem]:
          players[player][1] += 1
    i+=1
  csvfile.close()
f = open("playerwins.csv","w")
for player in players:
  wins = players[player][0]
  losses = players[player][1]
  f.write('{},{},{},{:.3f}\n'.format(player,wins,losses,wins/(wins+losses)))
f.close()
f = open('readme.txt','w')
f.write('requires python 3.  from command line run:\n\t py yeet.py n\nwhere n is the season number\ndirectory should include files scores<n>.csv and teams<n>.csv\nfiles from seasons 1 and 2 are given as examples of formatting.\npls no edit this readme file\n\ncurrently the following seasons are included in playerwins.csv:\n')
for szn in szns:
  f.write(str(szn)+'\n')
f.close()