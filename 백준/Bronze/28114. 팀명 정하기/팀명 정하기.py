def team_names(members):

    sorted_by_year = sorted(members, key=lambda x: x[1])
    first_team_name = ''.join(str(member[1] % 100) for member in sorted_by_year)
    

    sorted_by_problems = sorted(members, key=lambda x: -x[0])
    second_team_name = ''.join(member[2][0] for member in sorted_by_problems)
    
    return first_team_name, second_team_name


members = []
for _ in range(3):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    members.append((a, b, c))


first_team_name, second_team_name = team_names(members)


print(first_team_name)
print(second_team_name)
