"""
Library
"""

import math

def calculate_distance(point1,point2):
	"""
	"""
	return math.sqrt(pow(point1[0]-point2[0],2) + pow(point1[1]-point2[1],2))

def calculate_distance_from_origin(point):
	"""
	"""
	return calculate_distance(point,(0,0))