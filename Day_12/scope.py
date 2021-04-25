enemies = 1

def increase_enemies():
	# global enemies
	print(f"enemies inside function: {enemies}")
	return enemies+1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

##Python has no Block Scope

game_level = 3

enemies = ['Skeleton','Aliens','Zombies']
if game_level < 5:
	new_enemy = enemies[0]
print(new_enemy)

enemies = 1

##Global Constants 

PI = 3.1415
URL = "https://www.youtube.com"
TWITTER_HANDLE = "@yu_angela"