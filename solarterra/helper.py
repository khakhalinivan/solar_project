def cl():
    t = r"""public | auth_group                 | таблица | khakhalinivan
    public | auth_group_permissions     | таблица | khakhalinivan
    public | auth_permission            | таблица | khakhalinivan
    public | auth_user                  | таблица | khakhalinivan
    public | auth_user_groups           | таблица | khakhalinivan
    public | auth_user_user_permissions | таблица | khakhalinivan
    public | django_content_type        | таблица | khakhalinivan
    public | django_migrations          | таблица | khakhalinivan
    public | django_session             | таблица | khakhalinivan
    public | load_cdf_cdffilestored     | таблица | khakhalinivan
    public | load_cdf_dataset           | таблица | khakhalinivan
    public | load_cdf_datasetattribute  | таблица | khakhalinivan
    public | load_cdf_datatype          | таблица | khakhalinivan
    public | load_cdf_dynamicfield      | таблица | khakhalinivan
    public | load_cdf_dynamicmodel      | таблица | khakhalinivan
    public | load_cdf_logentry          | таблица | khakhalinivan
    public | load_cdf_upload            | таблица | khakhalinivan
    public | load_cdf_variable          | таблица | khakhalinivan
    public | load_cdf_variableattribute | таблица | khakhalinivan
    """

    lst = t.replace('|', '').split()
    print(',\n'.join(lst[1::4]))

    # смещение 1, период 4 

    # Очистили базу от ошметков импортированных данных
    # Зачищаю лог, делаю снова импорт
    # Нет отношения load_cdf_dataset
    # Забыл двойные кавычки на save_data
    # Составлю чеклист и попробую заново
    # [х] - удалить все таблицы питоном, НЕ ПОЛУЧИЛОСЬ, удалил psql-ем
    # [х] - проверить psql
    # [х] - python solarterra/manage.py makemigrations
    # [х] - python solarterra/manage.py migrate

    # [ ] - python manage.py makemigrations load_cdf --skip-checks
    # [ ] - python manage.py migrate load_cdf --skip-checks

    # [х] - python manage.py runserver  - проверим, что сайт работает
    # [х] - python manage.py create_datatype
    # [х] - python solarterra/manage.py evaluate "INTERBALL_IT_H0_DOK_v01_u2026-01-28T16-45-00.zip" "INTERBALL_IT_H0_DOK_v01_matchfile.json"   - проверим с кавычками. 
    # Проверил, работает
    # # <b>The last command  018_create_data_model_template requires immediate migrations (of the data_cdf app) 
    # # and web-server restart, otherwise the system is left in the unstable state.</b>
    # # Хм-хм. Без make migrations? Может она что-то затирает?
    # [х] - python solarterra/manage.py migrate
    # [х] - python solarterra/manage.py save_data "2026-01-28T16-45-00" "INTERBALL_IT_H0_DOK_v01"

# --------------------------------------------
    # [х] - python solarterra/manage.py evaluate "INTERBALL_IT_H0_DOK_v01_u2026-01-28T16-45-00.zip" "INTERBALL_IT_H0_DOK_v01_matchfile.json"





def cleandb():

    # Source - https://stackoverflow.com/a/73802708
    # Posted by egvo
    # Retrieved 3/19/2026, License - CC BY-SA 4.0

    import os, django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "solarterra.settings")
    django.setup()


    settings.configure()
    print('test')
    from django.db import connection

    with connection.cursor() as cursor:
        # Отключаем проверку внешних ключей, чтобы легко удалить все таблицы
        cursor.execute("SET session_replication_role = 'replica';")
        # Получаем список всех таблиц в публичной схеме
        cursor.execute("SELECT tablename FROM pg_tables WHERE schemaname = 'public';")
        tables = cursor.fetchall()
        for table_name in tables:
            print(f"Dropping table: {table_name[0]}")
            cursor.execute(f'DROP TABLE IF EXISTS "{table_name[0]}" CASCADE;')
        # Включаем проверку внешних ключей обратно
        cursor.execute("SET session_replication_role = 'origin';")


def count_cdf_files():
    # from load_cdf.models import *
    upload = Upload.objects.get(u_tag='2026-03-19T21-08-00')
    files = CDFFileStored.objects.filter(upload=upload)
    print(f"Найдено файлов: {files.count()}")
    if files.exists():
        print(f"Первый файл: {files.first().full_path}")

# cleandb()
# cl()
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "solarterra.settings")
django.setup()
from load_cdf.models import *
count_cdf_files()

# cd projects/solar_project/ && . solar_venv/bin/activate


# 