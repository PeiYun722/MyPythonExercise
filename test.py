import  xml.etree.cElementTree as ET
tree=ET.parse("hsinchuybike.xml")
root=tree.getroot()
for child in root.findall("Data"):
    month=child.find("所屬年月").text
    print(month)
   
 
print(" ")   
for child in root.findall("Data"):    
    for grandchild in child:
        if grandchild.tag=="所屬年月":
            print(grandchild.text)

# for child in root.findall("Data"):
#     month=child.find("所屬年月").text
#     if month != "2021-7":
#         child.remove(child)

