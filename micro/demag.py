import clib 
import numpy as np

class Demag(object):
    def __init__(self, name='demag'):
        self.name = name
        self.oommf = True
        
    def setup(self, mesh, spin, Ms):
        self.mesh = mesh
        self.dx = mesh.dx
        self.dy = mesh.dy
        self.dz = mesh.dz
        self.nx = mesh.nx
        self.ny = mesh.ny
        self.nz = mesh.nz
        self.spin = spin
        self.field = np.zeros(3 * mesh.nxyz, dtype=np.float)
        
        self.Ms = Ms

        self.demag=clib.FFTDemag(self.dx,self.dy,self.dz,
                                 self.nx,self.ny,self.nz,
                                 self.oommf)
        
    def compute_field(self, t=0):
        
        self.demag.compute_field(self.spin,self.Ms,self.field)

        return self.field
    
    def compute_exact(self):
        field = np.zeros(3 * self.mesh.nxyz)
        self.demag.compute_exact(self.spin,self.Ms,field)
        return field

    def compute_energy(self):
        
        #energy=self.demag.compute_energy(self.spin,self.mu_s,self.field)
        
        return 0.0
    