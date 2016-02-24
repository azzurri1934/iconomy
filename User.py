# coding: utf-8

import sys
import csv
import math

class User:

    def __init__(self):
    	name = ""
    	balance = 0
    	rank = 0
    	rank_str = ""

def get_user_list(file_name):
    reader = csv.reader(open(file_name, 'r'), delimiter=' ')
    user_list = []
    for row in reader:

    	user_obj = User()
    	user_obj.name = (row[0])
    	user_obj.balance = (int(float(row[1][8:])))

    	user_list.append(user_obj)

    user_list = sorted(user_list, cmp=lambda x,y: cmp(x.name.lower(), y.name.lower()))
    user_list = sorted(user_list, key=lambda User: User.balance, reverse=True)

    for cnt, item in enumerate(user_list):
        if cnt == 0:
            user_list[cnt].rank = 1
            user_list[cnt].rank_str = "1"
            now_rank = 1
        else:
            if user_list[cnt-1].balance == user_list[cnt].balance:
                user_list[cnt].rank = now_rank
                user_list[cnt].rank_str = u":::"
            else:
                user_list[cnt].rank = cnt+1
                user_list[cnt].rank_str = str(cnt+1)
                now_rank = cnt+1

    return user_list

def main():

    sorted_user_list = get_user_list(sys.argv[1])
    sorted_user_list2 = get_user_list(sys.argv[2])

    rank = u""
    print u"===== 長者番付 ====="
    print u"  * " + sys.argv[3] + u"年" + sys.argv[4] + u"月末時点のデータです。"
    print u"  * <color red>↑</color><color blue>↓</color>は前回からの増減値です。\n"
    print u"^  順位  ^^  名前  ^  所持金[円]  ^^^"
    for y in sorted_user_list2 :

    	cnt = 0
    	for x in sorted_user_list:
    		if x.name == y.name:
    			delta = x.rank - y.rank
    			if delta > 0:
    				delta_str = u"<color red><fs 90%>↑(" + str(delta) + u")</fs></color>"
    			elif delta == 0:
    				delta_str = u" "
    			else:
    				delta_str = u"<color blue><fs 90%>↓(" + str(int(math.fabs(delta))) + u")</fs></color>"

    			delta_level = y.balance - x.balance
    			if delta_level > 0:
    				delta_level_str = u"<color red><fs 90%>↑</fs></color>|  <color red><fs 90%>" + str('{:,d}'.format(delta_level)) + u"</fs></color>"
    			elif delta_level == 0:
    				delta_level_str = u" "
    			else:
    				delta_level_str = u"<color blue><fs 90%>↓</fs></color>|  <color blue><fs 90%>" + str('{:,d}'.format(int(math.fabs(delta_level)))) + u"</fs></color>"
    			break
    		if x.balance > 0:
    			cnt += 1
    	else:
    		delta = cnt + 1 - y.rank
    		if delta > 0:
    			delta_str = u"<color red><fs 90%>↑(" + str(delta) + u")</fs></color>"
    		elif delta == 0:
    			delta_str = u" "
    		else:
    			delta_str = u"<color blue><fs 90%>↓(" + str(int(math.fabs(delta))) + u")</fs></color>"
    		delta_level = y.balance
    		delta_level_str = u"<color red><fs 90%>↑</fs></color>|  <color red><fs 90%>" + str('{:,d}'.format(delta_level)) + u"</fs></color>"

    	print u"|  " + y.rank_str + u"|" + delta_str + u"|" + y.name + u"|  " + str('{:,d}'.format(y.balance)) + u"|" + delta_level_str + u"|"
    print u""

if __name__ == '__main__':
    main()