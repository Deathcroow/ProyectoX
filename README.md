# Proyecto Web con MySQL y Docker 🐬

Este es un proyecto web que utiliza MySQL como base de datos, con un contenedor Docker para facilitar su implementación. A continuación, se detallan algunos de los pasos básicos para hacer respaldos y restauraciones en MySQL, así como la estructura del proyecto.

## Estructura del Proyecto

La estructura básica de este proyecto es la siguiente:
**COMANDOS BASICOS MYSQL**🐬

  **Backup de toda la base de datos**

    - mysqldump -u usuario -p mi_base_de_datos > backup.sql

  **Backup de una tabla específica**

    - mysqldump -u usuario -p mi_base_de_datos tabla_especifica > backup_tabla_especifica.sql

  **Restaurar en una base de datos existente**

    - mysql -u usuario -p nueva_base_de_datos < backup.SQL

  **Restaurar en un servidor diferente**

    - scp backup.sql usuario@servidor_destino:/ruta/destino

    - mysql -u usuario -p mi_base_de_datos < /ruta/destino/backup.sql

