# solution 2 for the interview question

X = ["Poster", "Framed Poster", 'whiteboard']
Y = ["canvas", "Framed Poster"]
Z = ["Canvas", "Poster"]

dic = {0: 1.4984074067880424, 1: 1.0984074067880423, 2: 1.8984074067880425, 3: 2.2984074067880425,
       4: 2.2984074067880425}
# maximum value
max_value = max(dic.values())
# finding all keys containing the maximum
max_keys = [k for k, v in dic.items() if v == max_value]
print(max_value, max_keys)
# Find the key that contains Max Value
sampleDict = {'Poster': 19, 'Canvas': 68, 'Framed Poster': 11}
itemMaxValue = max(sampleDict.items(), key=lambda x: x[1])
print('Max value in Dict: ', itemMaxValue[1])
print('Key With Max value in Dict: ', itemMaxValue[0])
sampleDict = {'Canvas': 7, 'Framed Poster': 1, 'Poster': 120}
itemMaxValue = max(sampleDict.items(), key=lambda x: x[1])
print('Max value in Dict: ', itemMaxValue[1])
print('Key With Max value in Dict: ', itemMaxValue[0])
sampleDict = {'Framed Poster': 11, 'Poster': 76, 'Canvas': 15}
itemMaxValue = max(sampleDict.items(), key=lambda x: x[1])
print('Max value in Dict: ', itemMaxValue[1])
print('Key With Max value in Dict: ', itemMaxValue[0])
a_dict = {}
