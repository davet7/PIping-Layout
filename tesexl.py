equipos = ["bomba1", "bomba2", "reactor1", "reactor2","tanque1", "tanque2" ]
tagEquipos = [1,2,3,4,5,6]
corEX = [5,90, 40, 50, 70, 90]
corEY = [5,10, 40, 50, 70, 72]


path = []
xs = [x[1] for x in path]
ys = [y[0] for y in path]


import xlsxwriter as xls

workbook = xls.Workbook('reporte_Major_Pipiing_Layout.xlsx')
worksheet = workbook.add_worksheet('hoja 1')
worksheet.write(0,0,"EQUIPOS")
worksheet.write(1,0,"Nombre")
worksheet.write(2,0,"TAG")
worksheet.write(3,0,"Coor. en x")
worksheet.write(4,0,"Coor. en y")
worksheet.write(5,0,"COORDENADAS DE LAS TUBERIAS")
worksheet.write(6,0,"Coor. en x")
worksheet.write(7,0,"Coor. en y")

for col_num, data in enumerate(equipos):
    worksheet.write(1, col_num+1, data)
for col_num, data in enumerate(tagEquipos):
    worksheet.write(2, col_num+1, data)
for col_num, data in enumerate(corEX):
    worksheet.write(3, col_num+1, data)
for col_num, data in enumerate(corEY):
    worksheet.write(4, col_num+1, data)
for col_num, data in enumerate(xs):
    worksheet.write(6, col_num+1, data)
for col_num, data in enumerate(ys):
    worksheet.write(7, col_num+1, data)


workbook.close()