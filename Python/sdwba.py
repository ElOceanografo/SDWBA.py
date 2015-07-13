import scipy as sp
from scipy import linalg
import matplotlib.pyplot as plt

class Scatterer(object):
	"""
	Representation of the shape and material properties of a fluid-like
	sound scatterer.
	"""
	def __init__(self, x, y, z, a, g, h):
		"""
		Construct a Scatterer object, encapsulating the shape and material
		properties of a deformed-cylindrical object with sound speed and
		density similar to the surrounding fluid medium.

		Parameters
		----------
		x, y, z : array-like
			Posiions delimiting the central axis of the scatterer.
		a : array-like
			Array of radii along the centerline of the scatterer.
		g : array-like
			Array of sound speed contrasts (sound speed inside the scatterer
			divided by sound speed in the surrounding medium)
		h : array-like
			Array of density contrasts (density inside the scatterer
			divided by density in the surrounding medium)

		"""
		super(Scatterer, self).__init__()
		self.r = sp.matrix([x, y, z])
		self.a = sp.array(a)
		self.g = sp.array(g)
		self.h = sp.array(h)
		self.cum_rotation = sp.matrix(sp.eye(3))
	
	def rotate(self, roll=0, tilt=0, yaw=0):
		"""
		Rotate the scatterer in space.

		Parameters
		----------
		roll, tilt, yaw : float
			Angles (in degrees) by which to rotate the scatterer. The 
			rotations are applied in order (roll, then tilt, then yaw).
		"""
		tilt, roll, yaw = sp.deg2rad(tilt), sp.deg2rad(roll), sp.deg2rad(yaw)
		Rx = sp.matrix([[1, 0, 0], [0, sp.cos(roll), -sp.sin(roll)], [0, sp.sin(roll), sp.cos(roll)]])
		Ry = sp.matrix([[sp.cos(tilt), 0, sp.sin(tilt)], [0, 1, 0], [-sp.sin(tilt), 0, sp.cos(tilt)]])
		Rz = sp.matrix([[sp.cos(yaw), -sp.sin(yaw), 0], [sp.sin(yaw), sp.cos(yaw), 0], [0, 0, 1]])
		R = Rz * Ry * Rx
		self.cum_rotation = R * self.cum_rotation
		for i in range(self.r.shape[1]):
			self.r[:, i] = R * self.r[:, i]

  	def reset_rotation(self):
  		for i in range(self.r.shape[1]):
  			self.r[:, i] = linalg.solve(self.cum_rotation, self.r[:, i])
		

	def form_function(self, k, phase_sd=0):
		f_bs = 0j
		for i in range(self.r.shape[1] - 1):
			dr = r[:, i+1] - r[:, i]
			alphatilt = sp.acos(sp.dot(k, ))

	def form_function_continuous(self, k):
		pass

	def backscatter_xsection(self, k, phase_sd=0, method="discrete"):
		pass

	def TS(self):
		pass