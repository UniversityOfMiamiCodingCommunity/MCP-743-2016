answers = ["milwaukee","milw","milwa","w","milw",
	"Who controls the past, controls the future./n Who controls the present, controls the past.",
	"Who controls the present, controls the past./n Who controls the present, controls the past.",
	"Who controls the past, controls the future./n Who controls the past, controls the future.",
	"Who controls the past, controls the future./n Who controls the past, controls the future.",
	"i = 1", "i = 1", "i = -1", "i = 9", "i += 1", "i = 0", "conditional statement", "earth = 9",
	"i = 9", "i = 18", "i = 0", "i = 4", "i = 5", "i = 5", "i = 4", "i = 4", "i = 5", "j = 5, i = 9",
	"j = 0, i = 9", "j = 0, i = 18", "j = 0, i = 9", "j = 0, i = 0", "j = 0, i = 7", "i = 9, j = 9, k = 81",
	"k = 81, j = 9, i = 9, a = 45"]



keys = range(1,len(answers))
answerDict = {}
i = 1
for x in answers:
	answerDict[i] = answers[i-1]
	i += 1
print("answerDict", answerDict)