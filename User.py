# coding: utf-8

import sys
import csv
import math

class User:
	name = ""
	balance = 0	
	rank = 0
	rank_str = ""

	def set_name(self, name):
		self.name = name
		
	def set_balance(self, balance):
		self.balance = balance

	def set_rank(self, rank):
		self.rank = rank

	def set_rank_str(self, rank_str):
		self.rank_str = rank_str

	def get_name(self):
		return self.name
	
	def get_balance(self):
		return self.balance

	def get_rank(self):
		return self.rank

	def get_rank_str(self):
		return self.rank_str

argvs = sys.argv
argc = len(argvs)

#print argvs
#print argc

#print User.func(User)

spamReader1 = csv.reader(open(argvs[1], 'r'), delimiter=' ')
user_list = []
for row in spamReader1:
	
	
	user_obj = User()
	user_obj.set_name(row[0])
	user_obj.set_balance(int(float(row[1][8:])))
	
	if user_obj.get_balance() <= 30:
		continue
	
	user_list.append(user_obj)

# for x in user_list:
# 	print x.get_name()
# 	print x.get_balance()

spamReader = csv.reader(open(argvs[2], 'r'), delimiter=' ')
user_list2 = []
for row in spamReader:
	
	user_obj = User()
	user_obj.set_name(row[0])
	user_obj.set_balance(int(float(row[1][8:])))
	
	if user_obj.get_balance() <= 30:
		continue
	
	user_list2.append(user_obj)

# for x in user_list2:
# 	print x.get_name()
# 	print x.get_balance()

#　Woodcutter - 木こり
sorted_user_list = sorted(user_list, cmp=lambda x,y: cmp(x.get_name().lower(), y.get_name().lower()))
sorted_user_list = sorted(sorted_user_list, key=lambda User: User.get_balance(), reverse=True)

sorted_user_list2 = sorted(user_list2, cmp=lambda x,y: cmp(x.get_name().lower(), y.get_name().lower()))
sorted_user_list2 = sorted(sorted_user_list2, key=lambda User: User.get_balance(), reverse=True)

for x in [sorted_user_list, sorted_user_list2]:
	for y in x :

		index2 = x.index(y)
		if index2 == 0 :
			y.set_rank(1)
			now_rank = 1
			y.set_rank_str("1")
		else :
			if x[index2-1].get_balance() == y.get_balance():
				y.set_rank(now_rank)
				y.set_rank_str(":::")
			else:
				y.set_rank(index2 + 1)
				now_rank = index2 + 1
				y.set_rank_str(str(index2 + 1))

rank = ""
print "===== 長者番付 ====="
print "  * " + argvs[3] + "年" + argvs[4] + "月末時点のデータです。"
print "  * <color red>↑</color><color blue>↓</color>は前回からの増減値です。\n"
print "^  順位  ^^  名前  ^  所持金[円]  ^^^"
for y in sorted_user_list2 :

	cnt = 0
	for x in sorted_user_list: 
		if x.name == y.name:
			delta = x.rank - y.rank
			if delta > 0:
				delta_str = "<color red><fs 90%>↑(" + str(delta) + ")</fs></color>"
			elif delta == 0:
				delta_str = " "
			else:
				delta_str = "<color blue><fs 90%>↓(" + str(int(math.fabs(delta))) + ")</fs></color>"

			delta_level = y.get_balance() - x.get_balance()
			if delta_level > 0:
				delta_level_str = "<color red><fs 90%>↑</fs></color>|  <color red><fs 90%>" + str('{:,d}'.format(delta_level)) + "</fs></color>"
			elif delta_level == 0:
				delta_level_str = " "
			else:
				delta_level_str = "<color blue><fs 90%>↓</fs></color>|  <color blue><fs 90%>" + str('{:,d}'.format(int(math.fabs(delta_level)))) + "</fs></color>"
			break
		if x.get_balance() > 0:
			cnt += 1
	else:
		delta = cnt + 1 - y.rank
		if delta > 0:
			delta_str = "<color red><fs 90%>↑(" + str(delta) + ")</fs></color>"
		elif delta == 0:
			delta_str = " "
		else:
			delta_str = "<color blue><fs 90%>↓(" + str(int(math.fabs(delta))) + ")</fs></color>"
		delta_level = y.get_balance()
		delta_level_str = "<color red><fs 90%>↑</fs></color>|  <color red><fs 90%>" + str('{:,d}'.format(delta_level)) + "</fs></color>"
		
	print "|  " + y.rank_str + "|" + delta_str + "|" + y.name + "|  " + str('{:,d}'.format(y.get_balance())) + "|" + delta_level_str + "|" 
print ""
