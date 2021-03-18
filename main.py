print("Programmed by @the_indian_dev")
import os
try:
    directory = os.listdir('./input')
except FileNotFoundError:
    print('Please create a input Directory!')
    quit()
if len(directory) != 0:
    for FileinInput in directory:
        FileinOutput_name,FileinOutput_ext = tuple(FileinInput.split("."))
        print("Now working on {} file.".format(FileinOutput_name))
        InFile = open('./input/{}'.format(FileinInput),'r')
        templines = []
        for line in InFile:
            if 'VAPORPO0' in line:
                templines.append('VAPORPO0  0.0m  1000000m 0.0m  #VAPOR POSITION (Wings Swept Back or no-VGW)\n')
            elif 'VAPORPO1' in line:
                templines.append('VAPORPO1  0.0m  1000000m 0.0m  #VAPOR POSITION (Wings Spread)\n')
                #This will make the contrail appear one million feet away, somewhere invisible.
            else:
                templines.append(line)
        InFile.close()
        try:
            OutFile = open('./output/{}.dat'.format(FileinOutput_name),'w')
        except FileNotFoundError:
            print("Please create a output folder!")
            quit()
        for line in templines:
            OutFile.write(line)
        OutFile.close()
        print("Eliminated the wingtip contrails from {}".format(FileinOutput_name))
    print("Complete!\nIf you liked it please give a star in the github repo. (It is completely Free!)")
else:
    print("Nothing found in './input' directory!")