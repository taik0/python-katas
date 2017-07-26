# GoalTree (and-or-tree)
- `PutOn X Y`: pon el objeto X encima del objeto Y
- `PutOnTable X`: pon el objeto X en el suelo (espacio no definido)
- `FindSpace X`: haz sitio sobre el objeto X
- `FindSpaceOnTable`: encuentra la primer columna con espacio en el suelo
- `Move X Y`: mueve el objeto X a la columna Y (y apilalo)
- `UnGrasp X`: suelta el bloque X
- `ClearTop X`: despeja la parte superior del objeto X
- `Grasp X`: pilla el bloque X
- `GetRidOf X`: saca el objeto X del medio (edited)

https://files.slack.com/files-pri/T33C7RFU2-F6BDH15K3/captura_de_pantalla_2017-07-21_a_las_11.38.59.png

orden lógico de desarrollo:
- definir block (clase q representa el contenedor)
- definir table (clase q representa el espacio/escenario)
- crear método q inicializa el escenario con N contenendores aleatorios
- definir arm (clase q representa la grúa)
- crear métodos del algoritmo sobre arm
- crear goaltree
- crear nueva implementación de la grúa q use la nueva clase para dar info sobre la ejecución de la acción

montar una matriz para controlar el contenido de cada posición del espacio y q el primer índice represente las Y en vez del eje de las X
