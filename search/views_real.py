from django.shortcuts import render
from db.models import *
from django.http import HttpResponse
from django.db.models import Sum
from django.utils import timezone
import pandas as pd
from io import BytesIO
from datetime import datetime, timedelta, date


from openpyxl.utils import get_column_letter
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side


names = [
"김재웅", "안수빈", "심재용", "서대석", "서상민", "김남형", "정윤지", "유시완", "정태수", "문강현",
"황건우", "황병동", "박주형", "장평화", "김다윗", "심민우", "박승훈", "신재호", "김승국", "심인",
"김상욱", "이서현", "조규리", "김관호", "김상길", "유광훈", "김수용", "박혜강", "권동영", "진주혜",
"오민욱", "현남규", "유우종", "황지성", "조경래", "김성수", "김종룡", "정지원", "김소은", "장현민",
"김부미", "백준혁", "김효남", "강은정", "손승완", "김수진", "서명석", "유현동", "장병림", "배태욱",
"박춘성", "김성쥔", "이원형", "한민규", "김정현", "이광근", "박웅균", "신희진", "이환희", "최성빈",
"김규일", "이만덕", "정순홍", "정태민", "유주연", "맹훈", "김청기", "정태영", "임현상", "박중재",
"유호철", "김하늘", "김민지", "김성진", "조강은", "이환규", "김정환", "송화백", "유지수", "김동휘",
"송창진", "송화백", "이동규", "박성근", "전병민", "김경회", "이상빈", "김민수", "이진우", "박희지",
"이상윤", "신민주", "채종호", "배준수", "정상은", "한정민", "엄현준", "김가은"
]
company = ['adn', 'coupangmu', 'criteo', 'eleven', 'facebook', 'gmarket', 'interpark', 'kakao', 'kakaostyle', 'naver', 'navergfa', 'ssg', 'TG', 'tmon', 'wemakeprice', 'google', 'mobon', 'etc', 'da']

change = ['에이디엔','쿠팡','크리테오','11번가','페이스북','지마켓','인터파크','카카오','카카오스타일','네이버','네이버지에프에이','쓱','티지','티몬','위메프','구글','모본','디에이','기타']

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

######################
####### 첫번째 헤더생성
######################
def create_excel_header(worksheet, workbook, company_list):
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'align': 'center',
        'valign': 'vcenter',
        'bg_color': '#FFFF00',
        'border': 1
    })
    
    # 첫 번째 행의 헤더 설정
    worksheet.write('A1', '매체', header_format)
    col_idx = 1  # B열에서 시작
    for company in company_list:
        worksheet.merge_range(0, col_idx, 0, col_idx + 2, company, header_format)
        col_idx += 3  # 세 개의 열을 병합했으므로 인덱스를 3 증가
    
    # '맵핑수(누적)'과 '전매체 Live 계정수' 헤더 설정
    worksheet.merge_range(0, col_idx, 0, col_idx + 1, '맵핑수(누적)', header_format)
    col_idx += 2
    worksheet.merge_range(0, col_idx, 0, col_idx + 2, '전매체 Live 계정수', header_format)
    
    # 두 번째 행의 헤더 설정
    worksheet.write('A2', '팀원', header_format)
    col_idx = 1  # B열에서 시작
    sub_headers = ['전전주매출', '전주매출', '성장률']
    for _ in company_list:
        for sub_header in sub_headers:
            worksheet.write(1, col_idx, sub_header, header_format)
            col_idx += 1
    
    # '맵핑수(누적)' 밑에 '신규', '이관' 설정
    worksheet.write(1, col_idx, '신규', header_format)
    worksheet.write(1, col_idx + 1, '이관', header_format)
    col_idx += 2
    
    # '전매체 Live 계정수' 밑에 '전전주', '전주', '증감' 설정
    sub_headers = ['전전주', '전주', '증감']
    for sub_header in sub_headers:
        worksheet.write(1, col_idx, sub_header, header_format)
        col_idx += 1


######################
####### 두번째 헤더생성
######################
def create_excel_header2(worksheet, workbook, row_num):
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'align': 'center',
        'valign': 'vcenter',
        'bg_color': '#FFFF00',
        'border': 1
    })
    
    # 첫 번째 행의 헤더 설정
    worksheet.merge_range(row_num, 0, row_num+1 , 0, '팀원', header_format)
    
    col_idx = 1  # B열에서 시작
    
    worksheet.merge_range(row_num, col_idx, row_num , col_idx+3, '전매체 총 매출', header_format)
    
    col_idx+=3
    
    worksheet.merge_range(row_num, col_idx+1, row_num+1 , col_idx+1, '주력매체', header_format)
    worksheet.merge_range(row_num, col_idx+2, row_num+1 , col_idx+2, 'DB수집방식', header_format)
    worksheet.merge_range(row_num, col_idx+3, row_num+1 , col_idx+3, '영업방식', header_format)

    row_num+=1
    col_idx = 1
    
    sub_headers = ['전월매출', '당월누적매출', '예상매출', '예상증감']
    for sub_header in sub_headers:
        worksheet.write(row_num, col_idx, sub_header, header_format)
        col_idx += 1
    return row_num

def export_to_excel(data, selected_names, company):
    # 엑셀 파일 생성을 위한 버퍼
    output = BytesIO()
    # xlsxwriter를 사용하여 Excel writer 설정
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    workbook = writer.book

    # 엑셀 시트 생성
    worksheet = workbook.add_worksheet("Sales Data")
    writer.sheets['Sales Data'] = worksheet

    # 엑셀 헤더 생성
    create_excel_header(worksheet, workbook, company)
    
    center_align = workbook.add_format({'align': 'center'})
    # 데이터 쓰기
    row_num = 2
    for name in selected_names:
        
        if name in data:
            # 각 팀원에 대한 데이터를 작성하기 위해 새로운 행을 추가합니다.
            worksheet.write(row_num, 0, name, center_align)
            
            # 팀원의 각 company에 대한 데이터를 순회하며 작성합니다.
            col_idx = 1
            for com in change:
                company_data = data[name].get(com, {})
                worksheet.write(row_num, col_idx, company_data.get('week_before_last_total', 0), center_align)
                worksheet.write(row_num, col_idx + 1, company_data.get('last_week_total', 0), center_align)
                worksheet.write(row_num, col_idx + 2, f"{company_data.get('growth_rate', 0)}%", center_align)
                col_idx += 3
            
            # '신규'와 '이관' 데이터를 작성합니다.
            worksheet.write(row_num, col_idx, data[name].get('new', 0), center_align)
            worksheet.write(row_num, col_idx + 1, data[name].get('escalation', 0), center_align)
            col_idx += 2
            
            # '전매체 Live 계정수' 데이터를 작성합니다.
            worksheet.write(row_num, col_idx, data[name].get('before_last_live', 0), center_align)
            worksheet.write(row_num, col_idx + 1, data[name].get('last_live', 0), center_align)
            worksheet.write(row_num, col_idx + 2, data[name].get('increase', 0), center_align)
            
            row_num += 1
    
    row_num = create_excel_header2(worksheet, workbook, row_num+1)
    row_num+=1
    
    for name in selected_names:
        
        if name in data:
            # 각 팀원에 대한 데이터를 작성하기 위해 새로운 행을 추가합니다.
            worksheet.write(row_num, 0, name, center_align)
            
            # 팀원의 각 company에 대한 데이터를 순회하며 작성합니다.
            col_idx = 1
            
            worksheet.write(row_num, col_idx, data[name].get('previous_month_sales', 0), center_align)
            worksheet.write(row_num, col_idx + 1, data[name].get('last_week_total', 0), center_align)
            worksheet.write(row_num, col_idx + 2, data[name].get('estimated_sales', 0), center_align)
            worksheet.write(row_num, col_idx + 3, data[name].get('estimated_growth', 0), center_align)
            
            col_idx += 4
            row_num += 1
    
    # 파일 저장
    writer.close()
    output.seek(0)

    # HTTP 응답으로 엑셀 파일 전송
    response = HttpResponse(
        output.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="sales_report.xlsx"'
    return response

# views.py 메인함수

def sales_report(request):
        
    if request.method == 'POST':
        # 선택된 이름을 받아옵니다.
        selected_names = request.POST.getlist('names')

        # 현재 날짜를 기준으로 전주와 전전주 날짜를 계산합니다.
        today = date(2024, 2, 7)  # 기준 날짜를 2023년 2월 5일로 설정
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

            
            ###### ###### ###### ###### ###### ###### ###### ###### 
            ######  전월매출, 당월누적매출, 예상매출, 예상증감 ###### 
            ###### ###### ###### ###### ###### ###### ###### ###### 
            
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
            
        
            if 'export_excel' in request.POST:
                return export_to_excel(data, selected_names, change)
            
        return render(request, 'search/search.html', {
            'names' : names,
            'data' : data,
            'selectedName' : selected_names
        })
    return render(request, 'search/search.html', {
            'names' : names,
        })
