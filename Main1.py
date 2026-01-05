grid=[[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
],
[
    [21,22,23,24],
    [25,26,27,28],
    [29.30,31,32]
],
]
#accessing the 1st element
print(grid[0])#First list
print(grid[0][0][0])#First element
print(grid[0][2][2])
print(grid[1][0][0])

#Accessing a dictionary inside a list
grid2=[{"name":"Niska","class":2,"age":7}]
print(grid2)
print(grid2[0].get("name"))
#Accessing a list inside a dictionary
movie_genres={"horror":["chucky","anabell"],"comedy":["home alone","young sheldon"],"adventure":["sweettooth","Lock and key"]}
print(movie_genres.get("horror")[0])

#Adding a new element
movie_genres["adventure"].append("miraculous ladybug")
print(movie_genres)