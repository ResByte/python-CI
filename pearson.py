#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pearson.py
#  
#  Copyright 2013 Abhinav <abhinav@abhinav-Presario-CQ62-Notebook-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from math import sqrt

def pearson(v1,v2):
	# simple sums 
	sum1 = sum(v1)
	sum2 = sum(v2)
	
	#sum of the squares 
	sum1Sq = sum([pow(v,2) for v in v1])	
	sum2Sq = sum([pow(v,2) for v in v2])
	
	#sum of products 
	pSum = sum([v1[i]*v2[i] for i in range(len(v1))])
	
	#calculate r (pearson score)
	num = pSum - (sum1*sum2/len(v1))
	den = sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))
	if den == 0: return 0
	
	return 1.0-num/den



def main():
	v1 = [2,4,5,6,7]
	v2 = [2,4,5,6,7]
	print pearson(v1,v2)
	return 0

if __name__ == '__main__':
	main()

