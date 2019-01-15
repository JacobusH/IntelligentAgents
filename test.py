import json
import os
import math
import pprint
from owlready2 import *
from partPicker import get_label, get_subclasses_recur, get_subclasses_onelevel


onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\James25.owl").load()
obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
# sync_reasoner()

### working list all classes
# for x in list(onto.classes()):
# 	x = str(x)
# 	class_name = ""
# 	if 'webprotege' in x:
# 		_id = x.split('.')[3]
# 		class_name = obo[_id].label[0]
# 	else: # ont1
# 		_id = x.split('.')[1]
# 		class_name = _id
# print(class_name)

### working get wildcard label
# search_label = onto.search(label = "Memory")
# print(search_label[0])

### working get subclasses
# search_subclasses = onto.search(subclass_of = obo['RDpBs6DXJfwjWljvKnjFFK7']) # bleh finally got this POS to work
# for x in search_subclasses:
# 	parent = str(x.is_a[0])
# 	if 'RDpBs6DXJfwjWljvKnjFFK7' in parent: 
# 		print('X: %s' , x)
# 		print('ISA: %s' , x.is_a[0])


### working save individuals
# new_gpu1 = obo.Corsair_200R("indiv_case_1")
# new_gpu2 = obo.Corsair_200R("indiv_case_2")
# new_gpu3 = obo.Corsair_200R("indiv_case_3")
# onto.save("E:\\Homework\\Intelligent Agents\\PartPicker\\James16.owl")

# my_drug = obo.Case("my_case", namespace = onto, item_price = [100])
# onto.save("E:\\Homework\\Intelligent Agents\\PartPicker\\James25.owl")

### working get individuals
# for i in obo.Corsair_200R.instances(): # has direct indivs
# 	print(i)
for i in obo.Case.instances(): # only has bottom level indivs
	print(i)



# ['MotherboardBrands', 'MSI', 'MSI_GTX_1050_Ti_GAMING_X_4G', 'MSI_RX_580_ARMOR_8G_OC']

# xpUFBIdmzwyCPpbfIg4hh.MotherboardBrands
# xpUFBIdmzwyCPpbfIg4hh.CPU
# xpUFBIdmzwyCPpbfIg4hh.Case
# xpUFBIdmzwyCPpbfIg4hh.Cooling
# xpUFBIdmzwyCPpbfIg4hh.GPU
# xpUFBIdmzwyCPpbfIg4hh.Memory
# xpUFBIdmzwyCPpbfIg4hh.Motherboard
# xpUFBIdmzwyCPpbfIg4hh.PSU
# xpUFBIdmzwyCPpbfIg4hh.Storage
# xpUFBIdmzwyCPpbfIg4hh.DDR2
# xpUFBIdmzwyCPpbfIg4hh.DDR3
# xpUFBIdmzwyCPpbfIg4hh.DDR4
# xpUFBIdmzwyCPpbfIg4hh.EVGA_02G-P4-6150-KR
# xpUFBIdmzwyCPpbfIg4hh.EVGA_04G-P4-6251-KR
# xpUFBIdmzwyCPpbfIg4hh.Gigabyte_GV-N1050OC-2GD

### recursive indentation...
# # default with a level of 0, and an indent of 4 characters
# 	def write(p, depth=0, indent=4):
# 		if p==None:
# 			return
# 		# here we multiply the level by the number of indents
# 		# and then you multiply that number with a space character
# 		# which will magically show as that number of spaces.
# 		print("{}{}".format(" "*(indent*depth), p.value))
# 		if p.down!=None:
# 			# then you do not need your print(…, end='') hack
# 			# simply increase the depth
# 			write(p.down, depth=depth+1, indent=indent)
# 		# and for siblings, do not increase the depth
# 		write(p.right, depth=depth, indent=indent)

### CREATE YOUR OWN INDIVIDUALS FOR TESTING!!
# # xpUFBIdmzwyCPpbfIg4hh.CPUBrands
# # xpUFBIdmzwyCPpbfIg4hh.AMD
# obo.AMD("AMD1")
# # xpUFBIdmzwyCPpbfIg4hh.INTEL
# obo.INTEL("INTEL1")
# # xpUFBIdmzwyCPpbfIg4hh.MotherboardBrands
# # xpUFBIdmzwyCPpbfIg4hh.MSI
# obo.MSI("MSI1")
# obo.MSI("MSI2")
# # xpUFBIdmzwyCPpbfIg4hh.MSI_GTX_1050_Ti_GAMING_X_4G
# obo.MSI_GTX_1050_Ti_GAMING_X_4G("MSI_GTX_1050_Ti_GAMING_X_4G_1")
# obo.MSI_GTX_1050_Ti_GAMING_X_4G("MSI_GTX_1050_Ti_GAMING_X_4G_2")
# # xpUFBIdmzwyCPpbfIg4hh.MSI_RX_580_ARMOR_8G_OC
# obo.MSI_RX_580_ARMOR_8G_OC("MSI_RX_580_ARMOR_8G_OC_1")
# obo.MSI_RX_580_ARMOR_8G_OC("MSI_RX_580_ARMOR_8G_OC_2")
# # xpUFBIdmzwyCPpbfIg4hh.CoolingBrands
# # xpUFBIdmzwyCPpbfIg4hh.Cooler_Master_-_Hyper_212_EVO_82.9_CFM_Sleeve_Bearing_CPU_Cooler
# obo['Cooler_Master_-_Hyper_212_EVO_82.9_CFM_Sleeve_Bearing_CPU_Cooler']("Cooler_Master_-_Hyper_212_EVO_82.9_CFM_Sleeve_Bearing_CPU_Cooler_1")
# # xpUFBIdmzwyCPpbfIg4hh.CoolerMaster
# obo.CoolerMaster("CoolerMaster_1")
# obo.CoolerMaster("CoolerMaster_2")
# # xpUFBIdmzwyCPpbfIg4hh.MemoryQuantities
# # xpUFBIdmzwyCPpbfIg4hh.MemoryBrands
# # xpUFBIdmzwyCPpbfIg4hh.MemorySpeeds
# # xpUFBIdmzwyCPpbfIg4hh.HighMemory
# # xpUFBIdmzwyCPpbfIg4hh.MediumMemory
# # xpUFBIdmzwyCPpbfIg4hh.UltraHighMemory
# # xpUFBIdmzwyCPpbfIg4hh.LowMemory
# # xpUFBIdmzwyCPpbfIg4hh.VeryLowMemory
# # xpUFBIdmzwyCPpbfIg4hh.DDR3
# obo.DDR3("DDR3_1")
# obo.DDR3("DDR3_2")
# # xpUFBIdmzwyCPpbfIg4hh.DDR4
# obo.DDR4("DDR4_1")
# # xpUFBIdmzwyCPpbfIg4hh.DDR2
# obo.DDR2("DDR2_1")
# obo.DDR2("DDR2_2")
# # xpUFBIdmzwyCPpbfIg4hh.G.Skill
# obo["G.Skill"]("G.Skill_1")
# obo["G.Skill"]("G.Skill_2")
# # xpUFBIdmzwyCPpbfIg4hh.BigStorage
# # xpUFBIdmzwyCPpbfIg4hh.MediumStorage
# # xpUFBIdmzwyCPpbfIg4hh.LowStorage
# # xpUFBIdmzwyCPpbfIg4hh.StorageBrands
# # xpUFBIdmzwyCPpbfIg4hh.SSD
# obo.SSD("SSD_1")
# obo.SSD("SSD_2")
# # xpUFBIdmzwyCPpbfIg4hh.HDD
# obo.HDD("HDD_1")
# obo.HDD("HDD_2")
# # xpUFBIdmzwyCPpbfIg4hh.CT500MX500SSD1
# obo.CT500MX500SSD1("CT500MX500SSD1_1")
# obo.CT500MX500SSD1("CT500MX500SSD1_2")
# # xpUFBIdmzwyCPpbfIg4hh.Western_Digital_-_AV-GP_500_GB
# obo["Western_Digital_-_AV-GP_500_GB"]("Western_Digital_-_AV-GP_500_GB_1")
# obo["Western_Digital_-_AV-GP_500_GB"]("Western_Digital_-_AV-GP_500_GB_2")
# # xpUFBIdmzwyCPpbfIg4hh.MZ-76E250B/EU
# obo['MZ-76E250B/EU']("MZ-76E250B/EU_1")
# obo['MZ-76E250B/EU']("MZ-76E250B/EU_2")
# # xpUFBIdmzwyCPpbfIg4hh.SA400S37/120G
# obo["SA400S37/120G"]("SA400S37/120G_1")
# obo["SA400S37/120G"]("SA400S37/120G_2")
# # xpUFBIdmzwyCPpbfIg4hh.WesternDigital
# # xpUFBIdmzwyCPpbfIg4hh.CaseBrands
# # xpUFBIdmzwyCPpbfIg4hh.Corsair_200R
# # xpUFBIdmzwyCPpbfIg4hh.PSUBrands
# # xpUFBIdmzwyCPpbfIg4hh.Corsair_-_CXM_550_W_80+
# obo["Corsair_-_CXM_550_W_80+"]("Corsair_-_CXM_550_W_80+_1")
# obo["Corsair_-_CXM_550_W_80+"]("Corsair_-_CXM_550_W_80+_2")
# # xpUFBIdmzwyCPpbfIg4hh.GPUBrands
# # xpUFBIdmzwyCPpbfIg4hh.BigGPU
# # xpUFBIdmzwyCPpbfIg4hh.SmallGPU
# # xpUFBIdmzwyCPpbfIg4hh.MediumGPU
# # xpUFBIdmzwyCPpbfIg4hh.EVGA
# # xpUFBIdmzwyCPpbfIg4hh.Gigabyte_GV-N2070WF3-8GC
# obo["Gigabyte_GV-N2070WF3-8GC"]("Gigabyte_GV-N2070WF3-8GC_1")
# obo["Gigabyte_GV-N2070WF3-8GC"]("Gigabyte_GV-N2070WF3-8GC_2")
# # xpUFBIdmzwyCPpbfIg4hh.MSI_RX_580_ARMOR_8G_OC
# obo["MSI_RX_580_ARMOR_8G_OC"]("MSI_RX_580_ARMOR_8G_OC_1")
# obo["MSI_RX_580_ARMOR_8G_OC"]("MSI_RX_580_ARMOR_8G_OC_2")
# # xpUFBIdmzwyCPpbfIg4hh.EVGA_02G-P4-6150-KR
# obo["EVGA_02G-P4-6150-KR"]("EVGA_02G-P4-6150-KR_1")
# obo["EVGA_02G-P4-6150-KR"]("EVGA_02G-P4-6150-KR_2")
# # xpUFBIdmzwyCPpbfIg4hh.EVGA_04G-P4-6251-KR
# obo["EVGA_04G-P4-6251-KR"]("EVGA_04G-P4-6251-KR_1")
# obo["EVGA_04G-P4-6251-KR"]("EVGA_04G-P4-6251-KR_2")
# # xpUFBIdmzwyCPpbfIg4hh.Gigabyte_GV-N1050OC-2GD
# obo["Gigabyte_GV-N1050OC-2GD"]("Gigabyte_GV-N1050OC-2GD_1")
# obo["Gigabyte_GV-N1050OC-2GD"]("Gigabyte_GV-N1050OC-2GD_2")
# # xpUFBIdmzwyCPpbfIg4hh.MSI_GTX_1050_Ti_GAMING_X_4G
# # obo["MSI_GTX_1050_Ti_GAMING_X_4G"]("MSI_GTX_1050_Ti_GAMING_X_4G_1")
# # obo["MSI_GTX_1050_Ti_GAMING_X_4G"]("MSI_GTX_1050_Ti_GAMING_X_4G_2")
# onto.save("E:\\Homework\\Intelligent Agents\\PartPicker\\James16.owl")