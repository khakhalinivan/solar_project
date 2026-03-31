#!/bin/bash

# Параметры подключения
DB_NAME="test_project_khakhalinivan"
DB_USER="khakhalinivan"
export PGPASSWORD='kjydQEu156!w'


# Удаление таблицы
psql -U $DB_USER -d $DB_NAME << EOF
DO \$\$ 
DECLARE 
    r RECORD;
BEGIN
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') 
    LOOP
        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
    END LOOP;
END \$\$;
EOF
