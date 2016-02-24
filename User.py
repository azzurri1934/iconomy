# coding: utf-8

import sys
import csv
import math

class User:

    def __init__(self, name, balance):
    	self.name = name
    	self.balance = balance
    	self.rank = 0
    	self.rank_str = ""

def get_user_list(file_name):

    reader = csv.reader(open(file_name, 'r'), delimiter=' ')
    user_list = []
    for row in reader:
    	user_list.append(User(row[0], int(float(row[1][8:]))))

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
                user_list[cnt].rank = cnt + 1
                user_list[cnt].rank_str = str(cnt+1)
                now_rank = cnt + 1

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

        flag_match = False

     	for x in sorted_user_list:

            if x.name == y.name:
                delta_rank = x.rank - y.rank
                delta_balance = y.balance - x.balance
                flag_match = True
                break

        if not flag_match:
            delta_rank = len(sorted_user_list) + 1 - y.rank
            delta_balance = y.balance

        if delta_rank > 0:
			delta_rank_str = u"<color red><fs 90%>↑(" + str(delta_rank) + u")</fs></color>"
        elif delta_rank == 0:
			delta_rank_str = u" "
        else:
			delta_rank_str = u"<color blue><fs 90%>↓(" + str(int(math.fabs(delta_rank))) + u")</fs></color>"

        if delta_balance > 0:
			delta_balance_str = u"<color red><fs 90%>↑</fs></color>|  <color red><fs 90%>" + str('{:,d}'.format(delta_balance)) + u"</fs></color>"
        elif delta_balance == 0:
			delta_balance_str = u" "
        else:
			delta_balance_str = u"<color blue><fs 90%>↓</fs></color>|  <color blue><fs 90%>" + str('{:,d}'.format(int(math.fabs(delta_balance)))) + u"</fs></color>"

        print u"|  " + y.rank_str + u"|" + delta_rank_str + u"|" + y.name + u"|  " + str('{:,d}'.format(y.balance)) + u"|" + delta_balance_str + u"|"
    print u""

if __name__ == '__main__':
    main()