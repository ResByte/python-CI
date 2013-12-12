#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
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

def readfile(filename):
	lines = [line for line in file(filename)]
	
	#first line is the column titles 
	colnames = lines[0].strip().split('\t')[1:]
	rownames =[]
	data = []
	for line in lines[1:]:
		p  = line.strip().split('\t')
		# first column in each row is the rowname
		rownames.append(p[0])
		# the data for this row is the remainder of the row 
		data.append([float(x)for x in p[1:]])
	return rownames,colnames,data

def main():
	
	return 0

if __name__ == '__main__':
	main()

