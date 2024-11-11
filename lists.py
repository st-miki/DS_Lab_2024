bicycle = ["trek", "cannondale", "redline", "specialized"]
bicycle.insert(len(bicycle), "jeep")
print(bicycle)


motorcycles =["honda","yamaha","suzuki"]
motorcycles.insert(0,'ducati')
motorcycles.insert(1, 'toyota')
motorcycles.insert(-1, 'toyota')
motorcycles[-1:] = [motorcycles[-1], "Range Rover"]
print(motorcycles)