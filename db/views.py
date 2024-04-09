from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import *
import pandas as pd
from datetime import datetime

# 날짜와 시간 데이터를 파싱하는 함수

def parse_date(value):
    try:
        return datetime.strptime(str(int(value)), '%Y%m%d').date()
    except (ValueError, TypeError):
        print(f"Date parsing error for value: {value}")
        return None

def parse_datetime(value):
    try:
        return datetime.strptime(str(int(value)), '%Y%m%d%H%M%S')
    except (ValueError, TypeError):
        print(f"Datetime parsing error for value: {value}")
        return None

############################# T_TRANSFER ################################

def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)

            # DataFrame의 각 행을 처리합니다.
            for _, row in df.iterrows():
                # 날짜와 시간 데이터 파싱
                
                trns_date = parse_date(row['trns_date'])
                orig_date = parse_date(row['orig_date'])
                
                reg_dtm=parse_datetime(row['reg_dtm'])
                upd_dtm=parse_datetime(row['upd_dtm'])
                scrap_amt_dtm=parse_datetime(row['scrap_amt_dtm'])
                req_dtm = parse_datetime(row['req_dtm'])
                app_dtm = parse_datetime(row['app_dtm'])
                del_dtm = parse_datetime(row['del_dtm'])
                            
                # T_TRANSFER 인스턴스 생성
                transfer = T_TRANSFER(
                    # ... 다른 필드를 처리
                    trns_date=trns_date,
                    
                    req_dtm=req_dtm,
                    app_dtm=app_dtm,
                    reg_dtm=reg_dtm,
                    upd_dtm=upd_dtm,
                    scrap_amt_dtm=scrap_amt_dtm,
                    del_dtm=del_dtm,
                    orig_date=orig_date,
                    
                    trns_id=row.get('trns_id'),
                    media_id=row.get('media_id'),
                    mkt_cd=row.get('mkt_cd'),
                    mkt_nm=row.get('mkt_nm'),
                    mkt_uid=row.get('mkt_uid'),
                    trns_gbn=row.get('trns_gbn'),
                    trns_stat=row.get('trns_stat'),
                    report_yn=row.get('report_yn'),
                    customer_id=row.get('customer_id'),
                    customer_nm=row.get('customer_nm'),
                    pre_month_amt=row.get('pre_month_amt'),
                    reg_gbn=row.get('reg_gbn'),
                    pre_mkt_cd=row.get('pre_mkt_cd'),
                    trns_note=row.get('trns_note'),
                    orig_gbn=row.get('orig_gbn'),
                    scrap_amt_stat=row.get('scrap_amt_stat'),
                    scrap_amt_try=row.get('scrap_amt_try'),
                    delete_check=row.get('delete_check'),
                    reg_uid=row.get('reg_uid'),
                    reg_name=row.get('reg_name'),
                    upd_uid=row.get('upd_uid'),
                    upd_name=row.get('upd_name'),
                    del_uid=row.get('del_uid'),
                    del_name=row.get('del_name'),
                    reg_ip=row.get('reg_ip'),
                    upd_ip=row.get('upd_ip'),
                    del_ip=row.get('del_ip'),
                    # ... 나머지 필드
                )
                transfer.save()

        return render(request, 'db/upload_file.html', {'form': form})  # 성공 URL로 리디렉트

    else:
        form = UploadFileForm()
    return render(request, 'db/upload_file.html', {'form': form})


############################# T_SALES_DAY ################################

# def upload_file_view(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             excel_file = request.FILES['file']
#             df = pd.read_excel(excel_file)

#             # DataFrame의 각 행을 처리합니다.
#             for _, row in df.iterrows():
#                 # 날짜와 시간 데이터 파싱
                
#                 sale_date = parse_date(row['sale_date'])
                
#                 reg_dtm = parse_datetime(row['reg_dtm'])
#                 upd_dtm = parse_datetime(row['upd_dtm'])
                            
#                 # T_TRANSFER 인스턴스 생성
#                 transfer = T_Sales_Day(
#                     # ... 다른 필드를 처리
#                     sale_date = sale_date,
#                     reg_dtm = reg_dtm,
#                     upd_dtm = upd_dtm,
                    
#                     sale_date_fr = row.get('sale_date_fr'),
#                     media_id = row.get('media_id'),
#                     customer_id = row.get('customer_id'),
#                     customer_nm = row.get('customer_nm'),
#                     mkt_cd = row.get('mkt_cd'),
#                     mkt_nm = row.get('mkt_nm'),
#                     tot_amt = row.get('tot_amt'),
#                     reg_gbn = row.get('reg_gbn'),
#                     sale_note = row.get('sale_note'),
#                     scrap_param = row.get('scrap_param'),
#                     reg_uid = row.get('reg_uid'),
#                     reg_name = row.get('reg_name'),
#                     upd_uid = row.get('upd_uid'),
#                     upd_name = row.get('upd_name'),
#                     reg_ip = row.get('reg_ip'),
#                     upd_ip = row.get('upd_ip'),
#                     # ... 나머지 필드
#                 )
#                 transfer.save()

#         return render(request, 'db/upload_file.html', {'form': form})  # 성공 URL로 리디렉트

#     else:
#         form = UploadFileForm()
#     return render(request, 'db/upload_file.html', {'form': form})


############################# T_USER ################################

# def upload_file_view(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             excel_file = request.FILES['file']
#             df = pd.read_excel(excel_file)

#             # DataFrame의 각 행을 처리합니다.
#             for _, row in df.iterrows():
#                 # 날짜와 시간 데이터 파싱
                
#                 join_date = parse_date(row['join_date'])
#                 leav_date = parse_date(row['leav_date'])
#                 vac_date = parse_date(row['vac_date'])
#                 reg_dtm = parse_datetime(row['reg_dtm'])
#                 upd_dtm = parse_datetime(row['upd_dtm'])
#                 del_dtm = parse_datetime(row['del_dtm'])
#                 login_dtm = parse_datetime(row['login_dtm'])
                            
#                 # T_TRANSFER 인스턴스 생성
#                 transfer = T_USERS(
#                     uid = row['uid'],
#                     username = row['username'],
#                     ustate = row['ustate'],
#                     ugbn = row['ugbn'],
#                     dept_code = row['dept_code'],
#                     userid = row['userid'],
#                     userpw = row['userpw'],
#                     uemail = row['uemail'],
#                     mpop_email = row['mpop_email'],
#                     uphone = row['uphone'],
#                     umobile = row['umobile'],
#                     user_note = row['user_note'],
#                     join_date = join_date,
#                     leav_date = leav_date,
#                     vac_date = vac_date,
#                     work_time_yn = row['work_time_yn'],
#                     dept_amt_yn = row['dept_amt_yn'],
#                     reg_dtm = reg_dtm,
#                     upd_dtm = upd_dtm,
#                     del_dtm = del_dtm,
#                     reg_uid = row['reg_uid'],
#                     upd_uid = row['upd_uid'],
#                     del_uid = row['del_uid'],
#                     reg_name = row['reg_name'],
#                     upd_name = row['upd_name'],
#                     del_name = row['del_name'],
#                     reg_ip = row['reg_ip'],
#                     upd_ip = row['upd_ip'],
#                     del_ip = row['del_ip'],
#                     login_dtm = login_dtm,
#                     login_ip = row['login_ip'],
#                     fcm_token = row['fcm_token'],
#                     login_mode = row['login_mode'],
#                     device_model = row['device_model'],
#                     version_code = row['version_code'],
#                     and_sdk_int = row['and_sdk_int'],
#                     # ... 나머지 필드
#                 )
#                 transfer.save()

#         return render(request, 'db/upload_file.html', {'form': form})  # 성공 URL로 리디렉트

#     else:
#         form = UploadFileForm()
#     return render(request, 'db/upload_file.html', {'form': form})


############################# T_DEPT ################################

# def upload_file_view(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             excel_file = request.FILES['file']
#             df = pd.read_excel(excel_file)

#             # DataFrame의 각 행을 처리합니다.
#             for _, row in df.iterrows():
#                 # 날짜와 시간 데이터 파싱
                
#                 reg_dtm = parse_datetime(row['reg_dtm'])
#                 upd_dtm = parse_datetime(row['upd_dtm'])
#                 del_dtm = parse_datetime(row['del_dtm'])
                            
#                 # T_TRANSFER 인스턴스 생성
#                 transfer = T_DEPTS(
#                     dept_code = row['dept_code'],
#                     dept_name = row['dept_name'],
#                     sort_code = int(row['sort_code']),
#                     dept_note = row.get('dept_note', ''),
#                     reg_dtm = reg_dtm,
#                     upd_dtm = upd_dtm,
#                     del_dtm = del_dtm,
#                     reg_uid = row['reg_uid'],
#                     upd_uid = row.get('upd_uid', ''),
#                     del_uid = row.get('del_uid', ''),
#                     reg_name = row['reg_name'],
#                     upd_name = row.get('upd_name', ''),
#                     del_name = row.get('del_name', ''),
#                     reg_ip = row['reg_ip'],
#                     upd_ip = row['upd_ip'],
#                     del_ip = row['del_ip'],
#                 )
#                 transfer.save()

#         return render(request, 'db/upload_file.html', {'form': form})  # 성공 URL로 리디렉트

#     else:
#         form = UploadFileForm()
#     return render(request, 'db/upload_file.html', {'form': form})