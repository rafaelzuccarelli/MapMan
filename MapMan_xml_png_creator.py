import sys
import os
from PIL import Image, ImageDraw, ImageFont

wd = os.getcwd()

print('reading dictionary file...')
input_bin_dic_file = wd + '/dic_files/bin_dic.csv'
input_bin_dic = open(input_bin_dic_file, 'r', encoding = "utf-8")
bin_dic = {}
for line in input_bin_dic:
    line_list = list(line.split('\t'))
    bin_dic[line_list[0].replace('"', '')] = line_list[1].rstrip("\n").replace('"', '') 

print('Reading bin list...')
input_directory = wd + '/Input'
for currentpath, folders, files in os.walk(input_directory):
    for file in files:
        input_bin_file = input_directory + '/' + file
        input_bin = open(input_bin_file, 'r', encoding = "utf-8")
        #creates file based on input file name
        input_bin_file_name_path = input_bin_file.split('/')
        input_bin_file_name_extension = input_bin_file_name_path[-1].split('.')
        input_bin_file_name = input_bin_file_name_extension[0]
        output_xml_file = wd + '/Output/' + input_bin_file_name + '.xml'
        output = open(output_xml_file, 'w')
         
        output.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n' + '\n'
                    + '<Image image="" modified="10.02.2005 12:18:43" scaling="3.0" model="1" datasize="5" bgcolor="2" markmode="0" legendX="10" legendY="10">' + '\n')
        bin_list = []
        for line in input_bin:
            line_list = line.split('\t')
            bin_list.append(line_list[0].rstrip('\n'))
        yh = 165
        for bin in bin_list:
            output.write('  <DataArea x="1300" y="'+ str(yh) + '" blockFormat="" visualizationType="1" type="">' + '\n'
                         + '    <Identifier ' + 'id="'+  str(bin).replace('"','') + '" recursive="true"/>' + '\n'
                         + '  </DataArea>' + '\n')
            yh = yh + 35
        print(bin_list)
        output.write('</Image>')
        
        image_png_file = wd + '/Output/' + input_bin_file_name + '.png'
        img = Image.new('RGB', (2480, 3508), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf', 25)
        yn = 160
        BinCode = ''
        for bin in bin_list:
            BinCode = bin.replace('"','')
            if BinCode in bin_dic.keys():
                BinName = bin_dic[BinCode]
                BinName_list = BinName.split('.')
                BinName2nd = BinName_list[1] + '.' + BinName_list[2]
                d.text((20,yn), BinName2nd, font=fnt, fill=(0,0,0))
                yn = yn + 35        
        img.save(image_png_file, 'PNG')
