
import sys
sys.path.append('lib/')
sys.path.append('../lib/')
import numpy as np
import quantumMC

def V(x):
  return -1.0/x + 0.25/(2*x*x)

c = quantumMC.SchroedingerDiffusionMC(V)
c.setXmin(-9.0)
c.setXmax(3.0)
c.setDeltaX(0.005)
c.logGrid(True)
c.setNSteps(10000)
c.setN(1200)
c.run()
x, psi = c.getPsi()
energy, energy_error = c.getEnergy()

print "Energy: %.8f +/- %.8f" % (energy, energy_error)


from bokeh.plotting import figure, output_file, save
from bokeh.models import Label, Range1d
output_file("test_radial.html", title="QuantumMC test result")
p = figure(title="QuantumMC test result", x_axis_label='r', y_axis_label='r R(r)', width = 800, height = 800)

r_a = np.asarray(x)
psi_a = np.asarray(psi)

p.line(r_a, 2*r_a*np.exp(-r_a), legend="r R(r) for H", line_width=2, line_color="blue")
p.circle(r_a, psi_a, legend="r R(r)", line_width=2, line_color="red")
p.line(r_a, V(r_a), legend="Effective potential for l = 0", line_width=2, line_color="green")
energy = Label(x=70, y=700, x_units='screen', y_units='screen',
                 text='Energy = %.8f +/- %.8f Hartree' % (energy, energy_error), render_mode='css',
                 border_line_color='black', border_line_alpha=0.0,
                 background_fill_color='white', background_fill_alpha=0.0)
p.add_layout(energy)
p.y_range = Range1d(np.min(V(r_a)), np.max(psi_a)*1.5)
p.x_range = Range1d(0, 8)

save(p, "test_radial.html", title = "QuantumMC test result")
