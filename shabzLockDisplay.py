g = (0,255,0)
r = (255,0,0)
s = (0,0,0)
b = (139,69,19)
w = (255,255,255)
h = (244,164,96)
d = (0,0,255)

padlock_locked = [
  s,s,s,s,s,s,s,s,
  s,s,s,r,r,s,s,s,
  s,s,r,s,s,r,s,s,
  s,s,r,s,s,r,s,s,  
  s,r,r,r,r,r,r,s,
  s,r,r,r,r,r,r,s,
  s,r,r,r,r,r,r,s,
  s,r,r,r,r,r,r,s
]

padlock_unlocked = [
  s,s,s,s,s,s,s,s,
  s,s,s,g,g,s,s,s,
  s,s,g,s,s,g,s,s,
  s,s,s,s,s,g,s,s,
  s,g,g,g,g,g,g,s,
  s,g,g,g,g,g,g,s,
  s,g,g,g,g,g,g,s,
  s,g,g,g,g,g,g,s
]

tree_locked= [
  s,s,s,r,r,s,s,s,
  s,s,r,r,r,r,s,s,
  s,s,r,r,r,r,s,s, 
  s,r,r,r,r,r,r,s,
  s,r,r,r,r,r,r,s,
  r,r,r,r,r,r,r,r,
  s,s,s,b,b,s,s,s,
  s,s,s,b,b,s,s,s
]

tree_unlocked = [
  s,s,s,g,g,s,s,s,
  s,s,g,g,g,g,s,s,
  s,s,g,g,g,g,s,s,  
  s,g,g,g,g,g,g,s,
  s,g,g,g,g,g,g,s,
  g,g,g,g,g,g,g,g,
  s,s,s,b,b,s,s,s,
  s,s,s,b,b,s,s,s
]

firework_locked= [
  s,s,s,s,s,s,s,s,
  r,s,s,r,s,s,r,s,
  s,r,s,r,s,r,s,s,
  s,s,r,r,r,s,s,s,  
  r,r,r,r,r,r,r,s,
  s,s,r,r,r,s,s,s,
  s,r,s,r,s,r,s,s,
  r,s,s,r,s,s,r,s
]

firework_unlocked = [
  s,s,s,s,s,s,s,s,
  g,s,s,g,s,s,g,s,
  s,g,s,g,s,g,s,s,
  s,s,g,g,g,s,s,s,  
  g,g,g,g,g,g,g,s,
  s,s,g,g,g,s,s,s,
  s,g,s,g,s,g,s,s,
  g,s,s,g,s,s,g,s
]

star_locked= [
  s,s,r,r,r,r,s,s,
  s,s,r,r,r,w,r,s,
  s,s,h,d,h,d,s,s,
  h,r,h,h,b,b,r,h,  
  s,s,d,r,r,d,s,s,
  s,s,d,d,d,d,s,s,
  s,s,d,d,d,d,s,s,
  s,s,b,s,s,b,s,s
]

star_unlocked= [
  s,s,g,g,g,g,s,s,
  s,s,g,g,g,w,g,s,
  s,s,h,d,h,d,s,s,
  h,g,h,h,b,b,g,h,  
  s,s,d,g,g,d,s,s,
  s,s,d,d,d,d,s,s,
  s,s,d,d,d,d,s,s,
  s,s,b,s,s,b,s,s
]
