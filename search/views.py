from django.shortcuts import render
from db.models import *
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.db.models import Sum,Q
from django.utils import timezone
import pandas as pd
from io import BytesIO
from datetime import datetime, timedelta, date

from openpyxl.utils import get_column_letter
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side

import os
from django.conf import settings

names = []



for u in T_USERS.objects.all():
    names.append(u.username)

company = ['naver', 'navergfa', 'gmarket', 'eleven', 'wemakeprice']

change = ['네이버', '네이버지에프에이', '지마켓', '11번가', '위메프']

data = {}

for n in names:
    data[n] = {}


def get_previous_week_dates(reference_date):
    start_of_week = reference_date - timedelta(days=reference_date.weekday())  # 주의 시작 (월요일)
    end_of_week = start_of_week + timedelta(days=6)  # 주의 끝 (일요일)
    return start_of_week, end_of_week


def get_previous_month_range(current_date):
    # 전월의 마지막 날을 구하기 위해 현재 월의 첫날에서 하루를 빼면 전월의 마지막 날이 됩니다.
    end_of_last_month = current_date.replace(day=1) - timedelta(days=1)
    # 전월의 첫날은 마지막 날의 day를 1로 설정하면 됩니다.
    start_of_last_month = end_of_last_month.replace(day=1)
    return start_of_last_month, end_of_last_month


def calculate_growth(last_week_total, week_before_last_total):
    if week_before_last_total == 0 and last_week_total != 0:
        return 100
    elif week_before_last_total == 0 and last_week_total == 0:
        return 0
    else:
        return (last_week_total / week_before_last_total * 100)

# 엑셀파일 생성 및 다운로드

header_font = Font(bold=True)
header_fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))
center_align = Alignment(horizontal='center', vertical='center')

######################
####### 첫번째 헤더생성
######################
def create_excel_header(worksheet, company_list):
    # 첫 번째 행의 헤더 설정
    worksheet['A1'] = '매체'
    worksheet['A1'].font = header_font
    worksheet['A1'].fill = header_fill
    worksheet['A1'].alignment = header_align
    worksheet['A1'].border = border
    col_idx = 2  # B열에서 시작
    
    for company in change:
        cell = worksheet.cell(row=1, column=col_idx)
        worksheet.merge_cells(start_row=1, start_column=col_idx, end_row=1, end_column=col_idx+2)
        cell.value = company
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align
        cell.border = border
        col_idx += 3
        
    # '맵핑수(누적)'과 '전매체 Live 계정수' 헤더 설정
    cell = worksheet.cell(row=1, column=col_idx)
    worksheet.merge_cells(start_row=1, start_column=col_idx, end_row=1, end_column=col_idx+1)
    cell.value = '맵핑수(누적)'
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = border
    col_idx += 2

    cell = worksheet.cell(row=1, column=col_idx)
    worksheet.merge_cells(start_row=1, start_column=col_idx, end_row=1, end_column=col_idx+2)
    cell.value = '전매체 Live 계정수'
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = border
    col_idx += 3

    # 두 번째 행의 헤더 설정
    
    worksheet['A2'] = '팀원'
    worksheet['A2'].font = header_font
    worksheet['A2'].fill = header_fill
    worksheet['A2'].alignment = header_align
    worksheet['A2'].border = border

    col_idx = 2  # B열에서 시작
    
    sub_headers = ['전전주매출', '전주매출', '성장률']
    for _ in company_list:
        for sub_header in sub_headers:
            cell = worksheet.cell(row=2, column=col_idx)
            cell.value = sub_header
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_align
            cell.border = border
            col_idx += 1

    
    # '맵핑수(누적)' 밑에 '신규', '이관' 설정
    cell = worksheet.cell(row=2, column=col_idx)
    cell.value = '신규'
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = border
    col_idx += 1
    
    cell = worksheet.cell(row=2, column=col_idx)
    cell.value = '이관'
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = border
    col_idx += 1


    # '전매체 Live 계정수' 밑에 '전전주', '전주', '증감' 설정
    sub_headers = ['전전주', '전주', '증감']
    for sub_header in sub_headers:
        cell = worksheet.cell(row=2, column=col_idx)
        cell.value = sub_header
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align
        cell.border = border
        col_idx += 1


######################
####### 두번째 헤더생성
######################
def create_excel_header2(worksheet, row_num):
    col_idx = 1
    
    cell = worksheet.cell(row=row_num, column=col_idx)
    worksheet.merge_cells(start_row=row_num, start_column=col_idx, end_row=row_num+1, end_column=col_idx)
    cell.value = '팀원'
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = border
    col_idx += 1
    
    # 첫 번째 행의 헤더 설정
    cell = worksheet.cell(row=row_num, column=col_idx)
    worksheet.merge_cells(start_row=row_num, start_column=col_idx, end_row=row_num, end_column=col_idx+3)
    cell.value = '전매체 총 매출'
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = border
    col_idx += 4
    
    cell = worksheet.cell(row=row_num, column=col_idx)
    worksheet.merge_cells(start_row=row_num, start_column=col_idx, end_row=row_num+1, end_column=col_idx)
    cell.value = '주력매체'
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = border
    col_idx += 1
    
    cell = worksheet.cell(row=row_num, column=col_idx)
    worksheet.merge_cells(start_row=row_num, start_column=col_idx, end_row=row_num+1, end_column=col_idx)
    cell.value = 'DB수집방식'
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = border
    col_idx += 1

    cell = worksheet.cell(row=row_num, column=col_idx)
    worksheet.merge_cells(start_row=row_num, start_column=col_idx, end_row=row_num+1, end_column=col_idx)
    cell.value = '영업방식'
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = border
    col_idx += 1
    
    # 두번째 행
    col_idx = 2
    row_num+=1
    
    sub_headers = ['전월매출', '당월누적매출', '예상매출', '예상증감']
    for sub_header in sub_headers:
        cell = worksheet.cell(row=row_num, column=col_idx)
        cell.value = sub_header
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align
        cell.border = border
        col_idx += 1
    return row_num

def export_to_excel(data, selected_names, company_list):
    # 엑셀 파일 생성을 위한 버퍼
    wb = Workbook()
    ws = wb.active
    ws.title = "Sales Data"

    # 엑셀 헤더 생성
    create_excel_header(ws, company_list)
    
    # 데이터 쓰기
    row_num = 3
    for name in selected_names:
        if name in data:
            cell = ws.cell(row=row_num, column=1, value=name)
            cell.alignment = center_align
            col_idx = 2
            for company in company_list:
                company_data = data[name].get(company, {})
                
                cell = ws.cell(row=row_num, column=col_idx, value=company_data.get('week_before_last_total', 0))
                cell.alignment = center_align
                
                cell = ws.cell(row=row_num, column=col_idx+1, value=company_data.get('last_week_total', 0))
                cell.alignment = center_align
                
                cell = ws.cell(row=row_num, column=col_idx+2, value=f"{company_data.get('growth_rate', 0)}%")
                cell.alignment = center_align
                
                col_idx += 3
    
            cell = ws.cell(row=row_num, column=col_idx, value=data[name].get('new'))
            cell.alignment = center_align
            
            cell = ws.cell(row=row_num, column=col_idx+1, value=data[name].get('escalation'))
            cell.alignment = center_align
            
            cell = ws.cell(row=row_num, column=col_idx+2, value=data[name].get('before_last_live'))
            cell.alignment = center_align
            
            cell = ws.cell(row=row_num, column=col_idx+3, value=data[name].get('last_live'))
            cell.alignment = center_align
            
            cell = ws.cell(row=row_num, column=col_idx+4, value=data[name].get('increase'))
            cell.alignment = center_align
        row_num += 1
    

    row_num = create_excel_header2(ws, row_num+1)
    row_num+=1
    
    for name in selected_names:
        
        if name in data:
            # 각 팀원에 대한 데이터를 작성하기 위해 새로운 행을 추가합니다.
            cell = ws.cell(row=row_num, column=1, value=name)
            cell.alignment = center_align
            
            col_idx = 2
            
            cell = ws.cell(row=row_num, column=col_idx, value=data[name].get('previous_month_sales', 0))
            cell.alignment = center_align
            
            cell = ws.cell(row=row_num, column=col_idx+1, value=data[name].get('last_week_total', 0))
            cell.alignment = center_align
            
            cell = ws.cell(row=row_num, column=col_idx+2, value=data[name].get('estimated_sales', 0))
            cell.alignment = center_align
            
            cell = ws.cell(row=row_num, column=col_idx+3, value=data[name].get('estimated_growth', 0))
            cell.alignment = center_align
            

            col_idx += 4
            row_num += 1
    
    for column in ws.columns:
        max_length = 0
        column = [cell for cell in column if cell.value]  # 값이 있는 셀만 고려
        for cell in column:
            try:
                # 셀의 내용 길이를 체크 (셀에 저장된 데이터가 문자열이 아닐 수도 있으니 str()로 변환)
                length = len(str(cell.value))
                if length > max_length:
                    max_length = length
            except:
                pass
        adjusted_width = (max_length + 4)  # 약간의 여백 추가
        ws.column_dimensions[get_column_letter(column[0].column)].width = adjusted_width
    
    # 버퍼를 통해 파일 저장
    filename = "sales_report.xlsx"
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    wb.save(file_path)

    # 서버 내 파일 URL 생성
    file_url = settings.MEDIA_URL + filename
    return file_url

##########################
#### views.py 메인함수 ####
##########################

def sales_report(request):
    today = datetime.now().date()
    
    teams = T_DEPTS.objects.all()
    members = T_USERS.objects.all()
    
    team_code = request.GET.get('team_code')
    member_code = request.GET.get('member_code')
    export_excel = request.GET.get('export_excel') == 'true'
    selectedDate = request.GET.get('selectedDate')
    
    if selectedDate:
        ref_date = datetime.strptime(selectedDate, '%Y-%m-%d').date()
        today = ref_date
    else:
        today = datetime.now().date()
    
    if team_code or member_code:
        if team_code and member_code:
            members = T_USERS.objects.filter(username=member_code)
        elif team_code: 
            members = T_USERS.objects.filter(dept_code=team_code)
        else:
            members = T_USERS.objects.filter(username=member_code)
        
        selected_names = [m.username for m in members]

        data = {}

        for n in selected_names:
            data[n] = {}

        # 현재 날짜를 기준으로 전주와 전전주 날짜를 계산합니다.
        last_week_start, last_week_end = get_previous_week_dates(today - timedelta(weeks=1))
        week_before_last_start, week_before_last_end = get_previous_week_dates(today - timedelta(weeks=2))

        # 현재 날짜를 기준으로 전월달 과 현재까지를 계산합니다.
        previous_month_start, previous_month_end = get_previous_month_range(today)
        current_month_start = today.replace(day=1)

        # 모든 관련 데이터를 한 번에 조회합니다.
        last_week_data = T_Sales_Day.objects.filter(
            media_id__in=company,
            mkt_nm__in=selected_names,
            sale_date__range=[last_week_start, last_week_end]
        ).values('media_id', 'mkt_nm').annotate(total=Sum('tot_amt'))

        week_before_last_data = T_Sales_Day.objects.filter(
            media_id__in=company,
            mkt_nm__in=selected_names,
            sale_date__range=[week_before_last_start, week_before_last_end]
        ).values('media_id', 'mkt_nm').annotate(total=Sum('tot_amt'))

        # 데이터를 파싱하여 처리합니다.
        last_week_totals = { (d['media_id'], d['mkt_nm']): d['total'] for d in last_week_data }
        week_before_last_totals = { (d['media_id'], d['mkt_nm']): d['total'] for d in week_before_last_data }

        for name in selected_names:
            for com in company:
                last_week_total = last_week_totals.get((com, name), 0)
                week_before_last_total = week_before_last_totals.get((com, name), 0)
                growth_rate = calculate_growth(last_week_total, week_before_last_total)
                # 결과 저장
                data[name][com] = {
                    'last_week_total': round(last_week_total),
                    'week_before_last_total': round(week_before_last_total),
                    'growth_rate': round(growth_rate)
                }
                        
            ###### ###### ###### ###### ###### 
            ###### 신규, 이관을 계산합니다 ######
            ###### ###### ###### ###### ######  
            
            new = T_TRANSFER.objects.filter(
                mkt_nm=name,
                trns_gbn=1
            ).count()
            
            escalation = T_TRANSFER.objects.filter(
                mkt_nm=name,
                trns_gbn = 2
            ).count()
            
            data[name]['new'] = new
            data[name]['escalation'] = escalation    
                
                
            ###### ###### ###### ###### ###### ######
            ###### 전매체 Live 계정수를 계산합니다 ######
            ###### ###### ###### ###### ###### ######    

            # 전전주 Live 계정수
            before_last_live = T_Sales_Day.objects.filter(
                mkt_nm=name,
                tot_amt__gt=0,  # tot_amt가 0보다 큰 조건 추가
                sale_date__range=[week_before_last_start, week_before_last_end]
            ).count()  # 객체의 개수를 세는 메소드 사용

            # 전주 Live 계정수
            last_live = T_Sales_Day.objects.filter(
                mkt_nm=name,
                tot_amt__gt=0,  # tot_amt가 0보다 큰 조건 추가
                sale_date__range=[last_week_start, last_week_end]
            ).count()  # 객체의 개수를 세는 메소드 사용s
            
            increase = last_live-before_last_live
            
            data[name]['before_last_live'] = before_last_live
            data[name]['last_live'] = last_live
            data[name]['increase'] = increase

            ############# ###### ###### ###### ########
            # 전월매출, 당월누적매출, 예상매출, 예상증감 # 
            ###### ###### ###### ###### ###### ###### #
            
            # 전월 매출 
            previous_month_sales = round(T_Sales_Day.objects.filter(
                    mkt_nm=name,
                sale_date__range=[previous_month_start, previous_month_end]
                ).aggregate(total=Sum('tot_amt'))['total'] or 0)

            # 당월 누적 매출
            current_month_sales = round(T_Sales_Day.objects.filter(
                mkt_nm=name,
                sale_date__range=[current_month_start, today]
            ).aggregate(total=Sum('tot_amt'))['total'] or 0)

            # 예상 매출 계산 (단순화된 예상치 계산)
            estimated_sales = round((current_month_sales / today.day) * 30 if today.day != 0 else 0
    )
            # 예상 증감
            estimated_growth = round(estimated_sales - previous_month_sales)
            
            data[name]['previous_month_sales'] = previous_month_sales
            data[name]['current_month_sales'] = current_month_sales
            data[name]['estimated_sales'] = estimated_sales
            data[name]['estimated_growth'] = estimated_growth
            
        if export_excel:
            file_url = export_to_excel(data, selected_names, company)
            full_url = request.build_absolute_uri(file_url)  # 완전한 URL 생성
            return JsonResponse({'url': full_url})
        
        return render(request, 'search/search.html', {
            'teams': teams,
        'members': members,
        })
    return render(request, 'search/search.html', {
            'teams': teams,
        'members': members,
        })
##############
# 비동기 처리 #
############################### 1번 서버 #####################################
def fetch_team_data(request):
    team_code = request.GET.get('team_code')
    member_code = request.GET.get('member_code')
    ref_date_str = request.GET.get('ref_date')
    # 문자열을 datetime.date 객체로 변환
    
    if ref_date_str:
        ref_date = datetime.strptime(ref_date_str, '%Y-%m-%d').date()
        today = ref_date
    else:
        today = datetime.now().date()
    
    names = []
    company_list = {}
    
    if team_code and member_code:
        members = T_USERS.objects.filter(username=member_code)
    elif team_code:
        members = T_USERS.objects.filter(dept_code=team_code)
    elif member_code:
        members = T_USERS.objects.filter(username=member_code)
    else:
        members = T_USERS.objects.all()
    for m in members:
            names.append(m.username)
    
    for com in company:
            company_list[com] = 0
    
    data = data_process(names,today)
    
    return JsonResponse({'members': data, 'selected' : names, 'company': company_list}, safe=False)

############################### 1번 서버 후처리 ###############################
def data_process(members, today):
    
    data = {}
    # 선택된 이름을 받아옵니다.
    selected_names = members
    
    for n in selected_names:
        data[n] = {}
    
    # 현재 날짜를 기준으로 전주와 전전주 날짜를 계산합니다.
    # 기준 날짜를 2023년 2월 5일로 설정
    last_week_start, last_week_end = get_previous_week_dates(today - timedelta(weeks=1))
    week_before_last_start, week_before_last_end = get_previous_week_dates(today - timedelta(weeks=2))

    # 현재 날짜를 기준으로 전월달 과 현재까지를 계산합니다.
    previous_month_start, previous_month_end = get_previous_month_range(today)
    current_month_start = today.replace(day=1)

    # 모든 관련 데이터를 한 번에 조회합니다.
    last_week_data = T_Sales_Day.objects.filter(
        media_id__in=company,
        mkt_nm__in=selected_names,
        sale_date__range=[last_week_start, last_week_end]
    ).values('media_id', 'mkt_nm').annotate(total=Sum('tot_amt'))

    week_before_last_data = T_Sales_Day.objects.filter(
        media_id__in=company,
        mkt_nm__in=selected_names,
        sale_date__range=[week_before_last_start, week_before_last_end]
    ).values('media_id', 'mkt_nm').annotate(total=Sum('tot_amt'))

    # 데이터를 파싱하여 처리합니다.
    last_week_totals = { (d['media_id'], d['mkt_nm']): d['total'] for d in last_week_data }
    week_before_last_totals = { (d['media_id'], d['mkt_nm']): d['total'] for d in week_before_last_data }


    for name in selected_names:
        for com in company:
            last_week_total = last_week_totals.get((com, name), 0)
            week_before_last_total = week_before_last_totals.get((com, name), 0)
            growth_rate = calculate_growth(last_week_total, week_before_last_total)
            # 결과 저장
            data[name][com] = {
                'last_week_total': round(last_week_total),
                'week_before_last_total': round(week_before_last_total),
                'growth_rate': round(growth_rate)
            }
            
                    
        #########################
        # 신규, 이관을 계산합니다 #
        #########################
        
        # 신규
        new = T_TRANSFER.objects.filter(
            mkt_nm=name,
            trns_gbn=1
        ).count()
        
        # 이관
        escalation = T_TRANSFER.objects.filter(
            mkt_nm=name,
            trns_gbn = 2
        ).count()
        
        data[name]['new'] = new
        data[name]['escalation'] = escalation    
            
            
        #################################
        # 전매체 Live 계정수를 계산합니다 #
        #################################   

        # 전전주 Live 계정수
        before_last_live = T_Sales_Day.objects.filter(
            mkt_nm=name,
            tot_amt__gt=0,  # tot_amt가 0보다 큰 조건 추가
            sale_date__range=[week_before_last_start, week_before_last_end]
        ).count()  # 객체의 개수를 세는 메소드 사용

        # 전주 Live 계정수
        last_live = T_Sales_Day.objects.filter(
            mkt_nm=name,
            tot_amt__gt=0,  # tot_amt가 0보다 큰 조건 추가
            sale_date__range=[last_week_start, last_week_end]
        ).count()  # 객체의 개수를 세는 메소드 사용s
        
        # 증감
        increase = last_live-before_last_live
        
        data[name]['before_last_live'] = before_last_live
        data[name]['last_live'] = last_live
        data[name]['increase'] = increase

        
        ###########################################
        # 전월매출, 당월누적매출, 예상매출, 예상증감 #
        ###########################################
        
        # 전월 매출 
        previous_month_sales = round(T_Sales_Day.objects.filter(
                mkt_nm=name,
            sale_date__range=[previous_month_start, previous_month_end]
            ).aggregate(total=Sum('tot_amt'))['total'] or 0)

        # 당월 누적 매출
        current_month_sales = round(T_Sales_Day.objects.filter(
            mkt_nm=name,
            sale_date__range=[current_month_start, today]
        ).aggregate(total=Sum('tot_amt'))['total'] or 0)

        # 예상 매출 계산 (단순화된 예상치 계산)
        estimated_sales = round((current_month_sales / today.day) * 30 if today.day != 0 else 0
)
        # 예상 증감
        estimated_growth = round(estimated_sales - previous_month_sales)
        
        data[name]['previous_month_sales'] = previous_month_sales
        data[name]['current_month_sales'] = current_month_sales
        data[name]['estimated_sales'] = estimated_sales
        data[name]['estimated_growth'] = estimated_growth
   
    return data
