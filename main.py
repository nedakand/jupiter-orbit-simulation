"""
Simulates a spacecraft gravity assist around Jupiter using numerical integration.
Tracks velocity change and visualizes trajectory and speed over time.
Graphs a velocity vs time graph to further help visualize the effects of gravity.
"""

# Constants
G = 6.7e-11
RJup = 7E7 # radius of Jupiter
mJup = 1.9E27  # mass of Jupiter
mCraft = 722 # mass of spacecraft

# Objects and initial values

Jupiter = sphere(pos=vec(0,0,0), radius = RJup, color=color.red)
Craft =  sphere(pos=Jupiter.pos + vec(-25.334*RJup, -25 * RJup, 0), color=color.white,  make_trail = True, radius  = RJup/12 )
vJup = vec(-1.3E4, 0, 0)
vCraft = vec(0, 1E4, 0)
pCraft = mCraft * vCraft

vinitial = vCraft
rinitial = mag(Craft.pos - Jupiter.pos)

deltat = 10
t = 0

# Make speed graph
g1 = graph(height = 300, title="Velocity vs t", xtitle="t (s)", ytitle="Velocity (m/s)")
gv = gcurve(color=color.blue, label="v")

# move camera to give a better view
scene.center = vec(5*RJup, 0, 0)  
# let camera zoom out automatically
scene.autoscale = True  

while t < 1e7:
  rate(5000)
  
  # spacecraft's motion
  r_vec = Craft.pos - Jupiter.pos
  r = mag(r_vec)
  
  
  Fgrav = -(G * mJup * mCraft / r**2) * (r_vec/r)

  pCraft = pCraft + Fgrav * deltat
  Craft.pos = Craft.pos + (pCraft / mCraft) * deltat
  
  rfinal = mag(Craft.pos - Jupiter.pos)

  # Jupiter's motion
  Jupiter.pos = Jupiter.pos + vJup * deltat
  
  # Update time
  t = t + deltat
  
  #Plot on graphs
  gv.plot(t, mag(pCraft/mCraft))
  
  if(r < RJup):
    print("Crashed on Jupiter")
    break
  if(rfinal > rinitial):
    break
  
print(mag((pCraft/mCraft) - vinitial))
  

  



