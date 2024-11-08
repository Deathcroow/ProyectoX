**COMANDOS BASICOS MYSQL**

  **Backup de toda la base de datos**

    - mysqldump -u usuario -p mi_base_de_datos > backup.sql

  **Backup de una tabla específica**

    - mysqldump -u usuario -p mi_base_de_datos tabla_especifica > backup_tabla_especifica.sql

  **Restaurar en una base de datos existente**

    - mysql -u usuario -p nueva_base_de_datos < backup.SQL

  **Restaurar en un servidor diferente**

    - scp backup.sql usuario@servidor_destino:/ruta/destino

    - mysql -u usuario -p mi_base_de_datos < /ruta/destino/backup.sql

