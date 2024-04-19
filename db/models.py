from django.db import models

# class T_TRANSFER(models.Model):
#     trns_id = models.CharField(max_length=100, null=True)
#     media_id = models.CharField(max_length=50, null=True)
#     mkt_cd = models.CharField(max_length=50, null=True)
#     mkt_nm = models.CharField(max_length=100, null=True)
#     mkt_uid = models.CharField(max_length=100, null=True)
#     trns_gbn = models.CharField(max_length=50, null=True)
#     trns_stat = models.CharField(max_length=50, null=True)
#     report_yn = models.CharField(max_length=10, null=True)
#     customer_id = models.CharField(max_length=50, null=True)
#     customer_nm = models.CharField(max_length=100, null=True)
#     trns_date = models.DateField(null=True)
#     req_dtm = models.DateTimeField(null=True)
#     app_dtm = models.DateTimeField(null=True)
#     pre_month_amt = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#     reg_gbn = models.CharField(max_length=50, null=True)
#     pre_mkt_cd = models.CharField(max_length=50, null=True)
#     trns_note = models.TextField(blank=True, null=True)
#     orig_gbn = models.CharField(max_length=50, null=True)
#     orig_date = models.DateField(null=True)
#     scrap_amt_dtm = models.DateTimeField(null=True)
#     scrap_amt_stat = models.CharField(max_length=50, null=True)
#     scrap_amt_try = models.IntegerField(null=True)
#     delete_check = models.CharField(max_length=50, null=True)
#     reg_dtm = models.DateTimeField(null=True)
#     upd_dtm = models.DateTimeField(null=True)
#     del_dtm = models.DateTimeField(null=True, blank=True)
#     reg_uid = models.CharField(max_length=50, null=True)
#     reg_name = models.CharField(max_length=100, null=True)
#     upd_uid = models.CharField(max_length=50, null=True)
#     upd_name = models.CharField(max_length=100, null=True)
#     del_uid = models.CharField(max_length=50, blank=True, null=True)
#     del_name = models.CharField(max_length=100, blank=True, null=True)
#     reg_ip = models.CharField(max_length=100, null=True)
#     upd_ip = models.CharField(max_length=100, null=True)
#     del_ip = models.CharField(max_length=100, blank=True, null=True)

# class T_Sales_Day(models.Model):
#     sale_date = models.DateField()
#     sale_date_fr = models.CharField(max_length=50, null=True)
#     media_id = models.CharField(max_length=50, null=True)
#     customer_id = models.CharField(max_length=50, null=True)
#     customer_nm = models.CharField(max_length=100, null=True)
#     mkt_cd = models.CharField(max_length=50, null=True)
#     mkt_nm = models.CharField(max_length=100, null=True)
#     tot_amt = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#     reg_gbn = models.CharField(max_length=50, null=True)
#     sale_note = models.TextField(blank=True, null=True)
#     scrap_param = models.TextField(blank=True, null=True)
#     reg_dtm = models.DateTimeField(null=True)
#     upd_dtm = models.DateTimeField(null=True)
#     reg_uid = models.CharField(max_length=50, null=True)
#     reg_name = models.CharField(max_length=100, null=True)
#     upd_uid = models.CharField(max_length=50, null=True)
#     upd_name = models.CharField(max_length=100, null=True)
#     reg_ip = models.CharField(max_length=100, null=True)
#     upd_ip = models.CharField(max_length=100, null=True)

# class T_USERS(models.Model):
#     uid = models.CharField(max_length=50)
#     username = models.CharField(max_length=100)
#     ustate = models.CharField(max_length=1)
#     ugbn = models.CharField(max_length=1)
#     dept_code = models.CharField(max_length=50)
#     userid = models.CharField(max_length=50)
#     userpw = models.CharField(max_length=255)
#     uemail = models.EmailField()
#     mpop_email = models.EmailField()
#     uphone = models.CharField(max_length=50)
#     umobile = models.CharField(max_length=50)
#     user_note = models.TextField(null=True, blank=True)
#     join_date = models.DateField(null=True, blank=True)
#     leav_date = models.DateField(null=True, blank=True)
#     vac_date = models.DateField(null=True, blank=True)
#     work_time_yn = models.CharField(max_length=1)
#     dept_amt_yn = models.CharField(max_length=1)
#     reg_dtm = models.DateTimeField(null=True, blank=True)
#     upd_dtm = models.DateTimeField(null=True, blank=True)
#     del_dtm = models.DateTimeField(null=True, blank=True)
#     reg_uid = models.CharField(max_length=50, null=True, blank=True)
#     upd_uid = models.CharField(max_length=50, null=True, blank=True)
#     del_uid = models.CharField(max_length=50, null=True, blank=True)
#     reg_name = models.CharField(max_length=100, null=True, blank=True)
#     upd_name = models.CharField(max_length=100, null=True, blank=True)
#     del_name = models.CharField(max_length=100, null=True, blank=True)
#     reg_ip = models.CharField(max_length=50, null=True, blank=True)
#     upd_ip = models.CharField(max_length=50, null=True, blank=True)
#     del_ip = models.CharField(max_length=50, null=True, blank=True)
#     login_dtm = models.DateTimeField(null=True, blank=True)
#     login_ip = models.CharField(max_length=50, null=True, blank=True)
#     fcm_token = models.CharField(max_length=255, null=True, blank=True)
#     login_mode = models.CharField(max_length=50, null=True, blank=True)
#     device_model = models.CharField(max_length=100, null=True, blank=True)
#     version_code = models.CharField(max_length=50, null=True, blank=True)
#     and_sdk_int = models.CharField(max_length=50, null=True, blank=True)


# class T_DEPTS(models.Model):
#     dept_code = models.CharField(max_length=20, primary_key=True)
#     dept_name = models.CharField(max_length=50)
#     sort_code = models.IntegerField(null=True)
#     dept_note = models.CharField(max_length=255, null=True, blank=True)
#     reg_dtm = models.DateTimeField()
#     upd_dtm = models.DateTimeField(null=True, blank=True)
#     del_dtm = models.DateTimeField(null=True, blank=True)
#     reg_uid = models.CharField(max_length=50)
#     upd_uid = models.CharField(max_length=50, null=True, blank=True)
#     del_uid = models.CharField(max_length=50, null=True, blank=True)
#     reg_name = models.CharField(max_length=50)
#     upd_name = models.CharField(max_length=50, null=True, blank=True)
#     del_name = models.CharField(max_length=50, null=True, blank=True)
#     reg_ip = models.CharField(max_length=50, null=True, blank=True)
#     upd_ip = models.CharField(max_length=50, null=True, blank=True)
#     del_ip = models.CharField(max_length=50, null=True, blank=True)
    
# class T_CALL_DAY_LIST(models.Model):
#     call_id = models.CharField(max_length=100, primary_key=True)
#     sender = models.CharField(max_length=50,null=True )  # send 필드는 보내는 사람을 의미하는 것으로 추정됩니다.
#     receiver = models.CharField(max_length=50,null=True )  # recv 필드는 받는 사람을 의미하는 것으로 추정됩니다.
#     call_date = models.DateTimeField(null=True )  # call_date 필드에는 날짜와 시간 정보가 포함되어 있습니다.
#     call_duration = models.TimeField(null=True )  # call_time 필드는 통화 시간을 나타내므로 TimeField를 사용합니다.
#     time_to_sec = models.IntegerField(null=True)  # timeToSec 필드는 정수 값을 가지므로 IntegerField를 사용합니다.
    
# class T_NETSALES(models.Model):
#     sale_id = models.CharField(max_length=50, primary_key=True)
#     sale_month = models.CharField(max_length=6)  # 보통 연월은 6자리 숫자로 표현됩니다.
#     mkt_name = models.CharField(max_length=100)
#     tot_amt = models.BigIntegerField()  # 큰 금액을 다룰 수 있게 BigIntegerField를 사용합니다.
#     next_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
#     next_amt = models.BigIntegerField(null=True, blank=True)
#     target_time = models.IntegerField(null=True, blank=True)
#     target_call = models.IntegerField(null=True, blank=True)

##########################################################################################
##########################################################################################

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class T_CALL_DAY_LIST(models.Model):
    call_id = models.CharField(primary_key=True, max_length=40)
    send = models.CharField(max_length=20, blank=True, null=True)
    recv = models.CharField(max_length=20, blank=True, null=True)
    call_date = models.DateTimeField(blank=True, null=True)
    call_time = models.CharField(max_length=30, blank=True, null=True)
    timetosec = models.IntegerField(db_column='timeToSec', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_CALL_DAY_LIST'



class T_DEPTS(models.Model):
    dept_code = models.CharField(primary_key=True, max_length=12)
    dept_name = models.CharField(max_length=40)
    sort_code = models.SmallIntegerField()
    dept_note = models.CharField(max_length=500)
    reg_dtm = models.CharField(max_length=14)
    upd_dtm = models.CharField(max_length=14)
    del_dtm = models.CharField(max_length=14)
    reg_uid = models.CharField(max_length=12, blank=True, null=True)
    upd_uid = models.CharField(max_length=12, blank=True, null=True)
    del_uid = models.CharField(max_length=12, blank=True, null=True)
    reg_name = models.CharField(max_length=50, blank=True, null=True)
    upd_name = models.CharField(max_length=50, blank=True, null=True)
    del_name = models.CharField(max_length=50, blank=True, null=True)
    reg_ip = models.CharField(max_length=15, blank=True, null=True)
    upd_ip = models.CharField(max_length=15, blank=True, null=True)
    del_ip = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_DEPT'

class T_NETSALES(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=30)
    sale_month = models.IntegerField(blank=True, null=True)
    mkt_name = models.CharField(max_length=10, blank=True, null=True)
    tot_amt = models.IntegerField(blank=True, null=True)
    next_rate = models.IntegerField(blank=True, null=True)
    next_amt = models.BigIntegerField(blank=True, null=True)
    target_time = models.IntegerField(blank=True, null=True)
    target_call = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_NETSALES_TOTAL'


class T_Sales_Day(models.Model):
    sale_date = models.CharField(primary_key=True, max_length=8)
    sale_date_fr = models.CharField(max_length=8)
    media_id = models.CharField(max_length=20)
    customer_id = models.CharField(max_length=50)
    customer_nm = models.CharField(max_length=50)
    mkt_cd = models.CharField(max_length=50)
    mkt_nm = models.CharField(max_length=50)
    tot_amt = models.IntegerField()
    reg_gbn = models.CharField(max_length=1, blank=True, null=True)
    sale_note = models.CharField(max_length=100, blank=True, null=True)
    scrap_param = models.CharField(max_length=50, blank=True, null=True)
    reg_dtm = models.CharField(max_length=14, blank=True, null=True)
    upd_dtm = models.CharField(max_length=14, blank=True, null=True)
    reg_uid = models.CharField(max_length=12, blank=True, null=True)
    reg_name = models.CharField(max_length=20, blank=True, null=True)
    upd_uid = models.CharField(max_length=12, blank=True, null=True)
    upd_name = models.CharField(max_length=50, blank=True, null=True)
    reg_ip = models.CharField(max_length=15, blank=True, null=True)
    upd_ip = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_SALES_DAY'
        unique_together = (('sale_date', 'media_id', 'customer_id'),)

class T_TRANSFER(models.Model):
    trns_id = models.CharField(primary_key=True, max_length=12)
    media_id = models.CharField(max_length=20)
    mkt_cd = models.CharField(max_length=50)
    mkt_nm = models.CharField(max_length=50)
    mkt_uid = models.CharField(max_length=12)
    trns_gbn = models.CharField(max_length=1)
    trns_stat = models.CharField(max_length=1)
    report_yn = models.CharField(max_length=1)
    customer_id = models.CharField(max_length=50)
    customer_nm = models.CharField(max_length=50)
    trns_date = models.CharField(max_length=8, blank=True, null=True)
    req_dtm = models.CharField(max_length=14, blank=True, null=True)
    app_dtm = models.CharField(max_length=14, blank=True, null=True)
    pre_month_amt = models.IntegerField()
    reg_gbn = models.CharField(max_length=1, blank=True, null=True)
    pre_mkt_cd = models.CharField(max_length=50, blank=True, null=True)
    trns_note = models.CharField(max_length=255, blank=True, null=True)
    orig_gbn = models.CharField(max_length=1)
    orig_date = models.CharField(max_length=8, blank=True, null=True)
    scrap_amt_dtm = models.CharField(max_length=14, blank=True, null=True)
    scrap_amt_stat = models.CharField(max_length=1)
    scrap_amt_try = models.IntegerField()
    delete_check = models.CharField(max_length=1, blank=True, null=True)
    reg_dtm = models.CharField(max_length=14, blank=True, null=True)
    upd_dtm = models.CharField(max_length=14, blank=True, null=True)
    del_dtm = models.CharField(max_length=14, blank=True, null=True)
    reg_uid = models.CharField(max_length=12, blank=True, null=True)
    reg_name = models.CharField(max_length=20, blank=True, null=True)
    upd_uid = models.CharField(max_length=12, blank=True, null=True)
    upd_name = models.CharField(max_length=50, blank=True, null=True)
    del_uid = models.CharField(max_length=12, blank=True, null=True)
    del_name = models.CharField(max_length=50, blank=True, null=True)
    reg_ip = models.CharField(max_length=15, blank=True, null=True)
    upd_ip = models.CharField(max_length=15, blank=True, null=True)
    del_ip = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_TRANSFER'


class T_USERS(models.Model):
    uid = models.CharField(primary_key=True, max_length=12)
    username = models.CharField(max_length=50)
    ustate = models.CharField(max_length=1)
    ugbn = models.CharField(max_length=1)
    dept_code = models.CharField(max_length=12)
    userid = models.CharField(unique=True, max_length=50)
    userpw = models.CharField(max_length=50, blank=True, null=True)
    uemail = models.CharField(max_length=50, blank=True, null=True)
    mpop_email = models.CharField(max_length=50, blank=True, null=True)
    uphone = models.CharField(max_length=20, blank=True, null=True)
    umobile = models.CharField(max_length=20, blank=True, null=True)
    user_note = models.CharField(max_length=500, blank=True, null=True)
    join_date = models.CharField(max_length=8, blank=True, null=True)
    leav_date = models.CharField(max_length=8, blank=True, null=True)
    vac_date = models.CharField(max_length=8, blank=True, null=True)
    work_time_yn = models.CharField(max_length=1, blank=True, null=True)
    dept_amt_yn = models.CharField(max_length=1, blank=True, null=True)
    reg_dtm = models.CharField(max_length=14, blank=True, null=True)
    upd_dtm = models.CharField(max_length=14, blank=True, null=True)
    del_dtm = models.CharField(max_length=14, blank=True, null=True)
    reg_uid = models.CharField(max_length=12, blank=True, null=True)
    upd_uid = models.CharField(max_length=12, blank=True, null=True)
    del_uid = models.CharField(max_length=12, blank=True, null=True)
    reg_name = models.CharField(max_length=50, blank=True, null=True)
    upd_name = models.CharField(max_length=50, blank=True, null=True)
    del_name = models.CharField(max_length=50, blank=True, null=True)
    reg_ip = models.CharField(max_length=15, blank=True, null=True)
    upd_ip = models.CharField(max_length=15, blank=True, null=True)
    del_ip = models.CharField(max_length=15, blank=True, null=True)
    login_dtm = models.CharField(max_length=14, blank=True, null=True)
    login_ip = models.CharField(max_length=15, blank=True, null=True)
    fcm_token = models.CharField(max_length=200, blank=True, null=True)
    login_mode = models.CharField(max_length=10, blank=True, null=True)
    device_model = models.CharField(max_length=20, blank=True, null=True)
    version_code = models.CharField(max_length=5, blank=True, null=True)
    and_sdk_int = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_USER'
        
class T_Media_Marketer(models.Model):
    media_id = models.CharField(primary_key=True, max_length=20)
    mkt_cd = models.CharField(max_length=50)
    mkt_nm = models.CharField(max_length=50)
    mkt_stat = models.CharField(max_length=1)
    mkt_uid = models.CharField(max_length=12)
    app_dtm = models.CharField(max_length=14)
    media_note = models.CharField(max_length=2000, blank=True, null=True)
    reg_gbn = models.CharField(max_length=1, blank=True, null=True)
    reg_dtm = models.CharField(max_length=14, blank=True, null=True)
    upd_dtm = models.CharField(max_length=14, blank=True, null=True)
    del_dtm = models.CharField(max_length=14, blank=True, null=True)
    reg_uid = models.CharField(max_length=12, blank=True, null=True)
    reg_name = models.CharField(max_length=20, blank=True, null=True)
    upd_uid = models.CharField(max_length=12, blank=True, null=True)
    upd_name = models.CharField(max_length=50, blank=True, null=True)
    del_uid = models.CharField(max_length=12, blank=True, null=True)
    del_name = models.CharField(max_length=50, blank=True, null=True)
    reg_ip = models.CharField(max_length=15, blank=True, null=True)
    upd_ip = models.CharField(max_length=15, blank=True, null=True)
    del_ip = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_MEDIA_MARKETER'
        unique_together = (('media_id', 'mkt_cd'),)