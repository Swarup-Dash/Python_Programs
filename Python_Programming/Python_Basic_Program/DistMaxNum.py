def find_top_scores(information):
    studentName = None
    maxMark = 0
    maxPercentage = 0
    for i, details in information.items():
        name, mark1, mark2, mark3 = details
        sum = mark1 + mark2 + mark3
        percentage = (sum/300)*100
    
        if sum > maxMark:
            maxMark = sum
            studentName = name
            maxPercentage = percentage
        
    return maxMark, studentName, maxPercentage

information = {
    100: ("Swarup", 52, 89, 98),
    101: ("Amrit", 85, 85, 92),
    102: ("Sanjaya", 62, 59, 68),
    103: ("Kunal", 48, 49, 98),
}

topStudent, topMark, topPercentage = find_top_scores(information)
print(topStudent, topMark, topPercentage)