# GhidraCsvImporter
Ghidra Jython Scripts for CSV-Based Table, Label, and Function Import

This repository contains custom Jython scripts for Ghidra that automate the import of symbolic data from CSV files. 
Designed for reverse engineers working with automotive firmware or embedded systems, these scripts streamline the labeling of memory regions, functions, and data tables.

Table Import Script: Automatically labels and comments known data tables from CSV.

Advanced Import Script: Extends basic functionality by supporting label imports for both data and function addresses, enhancing project readability and analysis efficiency.

Usage: The script will create the follow menu items:  CSV Import > Import Labels & CSV Import > Import Labels With Functions

These tools help accelerate analysis by integrating pre-defined symbol information directly into your Ghidra project. Compatible with any architecture supported by Ghidra.

NOTE (for dummies): You must parse the A2L to CSV first.

Please do not contact me regarding this for support unless you are able to provide the solutions to any problems you may find or ideaas you may have.
