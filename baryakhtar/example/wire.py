import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt


import numpy as np
from pc import FDMesh
from baryakhtar import Sim
from baryakhtar import Demag
from baryakhtar import Zeeman
from baryakhtar import UniformExchange

def relax_system(mesh):
    
    sim = Sim(mesh,Me=8e5,name='relax')
    
    sim.set_options(rtol=1e-6,atol=1e-6)
    sim.alpha = 0.01
    sim.beta = 0
    sim.gamma = 2.211e5
    sim.Ms = 8.0e5
    sim.do_procession = False
    
    sim.set_m((1,0.25,0.1))
    #sim.set_m(np.load('m0.npy'))
    
    A = 1.3e-11
    exch = UniformExchange(A=A, chi=1e-4)
    sim.add(exch)
    
    mT = 795.7747154594767
    zeeman = Zeeman([-24.6*mT,4.3*mT,0],name='H')
    sim.add(zeeman, save_field=True)
    
    #demag = Demag()
    #sim.add(demag)
            
    ONE_DEGREE_PER_NS = 17453292.52
    sim.run_until(1e-12)
    
    #sim.relax(dt=1e-13, stopping_dmdt=0.01*ONE_DEGREE_PER_NS, max_steps=5000, save_m_steps=100, save_vtk_steps=50)
    
    np.save('m0.npy',sim.spin)

if __name__=="__main__":
    
    mesh = FDMesh(nx=20, ny=1, nz=1, dx=2.5, dy=2.5, dz=3, unit_length=1e-9)
    relax_system(mesh)
    

        
    
    