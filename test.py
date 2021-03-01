# this program simply take marks form student and calculate grade

# credit of subjects
# for convieience we are tacking 1 as subject code for MCSE-011
subject_to_code = {
	"11" : "MCS_011",
	"12" : "MCS_012",
	"13" : "MCS_013",
	"14" : "MCS_014",
	"15" : "MCS_015",
	"16" : "MCSL_016",
	"17" : "MCSL_017",
	"21" : "MCS_021",
	"22" : "MCS_022",
	"23" : "MCS_023",
	"24" : "MCS_024",
	"25" : "MCSL_025",
	"31" : "MCS_031",
	"32" : "MCS_032",
	"33" : "MCS_033",
	"34" : "MCS_034",
	"35" : "MCS_035",
	"36" : "MCSL_036",
	"41" : "MCS_041",
	"42" : "MCS_042",
	"43" : "MCS_043",
	"44" : "MCS_044",
	"45" : "MCSL_045",
	"51" : "MCS_051",
	"52" : "MCS_052",
	"53" : "MCS_053",
	"54" : "MCSL_054",
	"3" : "MCSE_003",
	"4" : "MCSE_004",
	"1" : "MCSE_011",
	"60" : "MCSP_060",
}

weights = {
	"11" : 3,
	"12" : 4,
	"13" : 2,
	"14" : 3,
	"15" : 2,
	"16" : 2,
	"17" : 2,
	"21" : 4,
	"22" : 4,
	"23" : 3,
	"24" : 3,
	"25" : 4,
	"31" : 4,
	"32" : 3,
	"33" : 2,
	"34" : 3,
	"35" : 3,
	"36" : 3,
	"41" : 4,
	"42" : 4,
	"43" : 4,
	"44" : 4,
	"45" : 2,
	"51" : 3,
	"52" : 2,
	"53" : 4,
	"54" : 2,
	"3" :  3,
	"4" :  3,
	"1" :  3,
	"60" : 16,
}


# list_of_subjects = [11,12,13,14,15,16,17,21,22,23,24,25,31,32,33,34,35,36,41,42,43,44,45,51,52,53,54,3,4,1,60]
list_of_subjects = [11,12]

def print_result():
	print('Result is ')
	print('subjects\tAssig.\tTEE\ttotal\tweighted_total')
	for x in range(total_sub):
		for y in range(5):
			if y == 0:
				print(subject_to_code[str(result[x][y])] + "\t\t",end='')
			else:
				print(str(result[x][y]) + "\t",end='')
		print("")
	# for x in result:
	# 	print(x)


# we need dictionary to map list_of_subjects with name of subjects
# weights = {
# 	"11" : 3,
# 	"12" : 2
# }

# we need dictionary to map list_of_subjects wiht credit

# removing the subjects for which we don't want to calculate
# print('enter subject number you want to remove (type- 00 for exit) :')
# while True:
# 	remove_subject = int(input('enter number: '))
# 	if remove_subject != 00:
# 		list_of_subjects.remove(remove_subject)
# 	else:
# 		break
# print('now result will be shown for bellow subjects only')
# print(list_of_subjects)

# result represents a result with structure bellow
# first column = subject name
# secound column = assignment marks
# third column = term end exam marks
# fourth column = total
# fifth column = weighted_total

# the percentage is sum of fifth column(weighted_total) divided by total weight

total_sub = len(list_of_subjects)
# print(total_sub)
# initializing all element to 0
result = [[0.0 for x in range(5)] for y in range(total_sub)]
# print(result[30][4])


temp = 0
for x in list_of_subjects:
	result[temp][0] = x
	temp += 1



# getting marks from student
for x in result:
	x[1] = float(input('marks of assignment of ' + str(x[0]) + ": "))
	x[2] = float(input('marks of assignment of ' + str(x[0]) + ": "))

# calculate result
weight_sum = 0
sum_weighted_total = 0
for x in result:
	x[3] = float(x[1]*0.25 + x[2]*0.75)
	x[4] = float(x[3] * weights[str(x[0])])
	weight_sum += weights[str(x[0])]
	sum_weighted_total += x[4]


# for x in result:
	
# 	print(sum_weighted_total)

# print(weight_sum, sum_weighted_total)
print_result()
percentage = sum_weighted_total / weight_sum
print('percentage is ' + str(percentage))
# print(MCS_011)



