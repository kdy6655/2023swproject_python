import tkinter as tk
from tkinter import ttk

def order_drink():
    selected_drink = drink_var.get()
    quantity = quantity_var.get()
    
    # 주문 처리 로직 작성
    
    # 주문 정보 출력
    result_label.config(text=f"{selected_drink} {quantity}잔 주문이 완료되었습니다.")

def scroll_to_top():
    canvas.yview_moveto(0)  # 스크롤을 맨 위로 이동

# 음식과 가격 데이터 사전
menu_data = {
    "소주": 4000,
    "맥주": 5000,
    "위스키": 10000,
    "와인": 15000,
    "막걸리": 6000,
    "보드카": 8000,
    "럼": 9000,
    "칵테일": 12000,
    "마진": 3000,
    "마이티": 3500,
    "탁주": 7000,
    "진": 10000,
    "사케": 6000,
    "흑맥주": 5500,
    "청하": 5000,
    "송로": 9000,
    "기네스": 6500,
    "헤이즐넛": 5500,
    "라임": 4000,
    "에일": 7000
}

# tkinter 윈도우 생성
window = tk.Tk()
window.title("술집 티오더 프로그램")

# 스크롤바 생성
scrollbar = ttk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Canvas 생성
canvas = tk.Canvas(window, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 스크롤바와 Canvas 연결
scrollbar.config(command=canvas.yview)

# 메뉴 프레임 생성
menu_frame = ttk.Frame(canvas)

# Canvas에 메뉴 프레임 추가
canvas.create_window((0, 0), window=menu_frame, anchor=tk.NW)

# 음료 선택 라벨
drink_label = tk.Label(window, text="음료 선택:")
drink_label.pack()

# 음료 선택 옵션 메뉴
drink_var = tk.StringVar(window)
drink_var.set("소주")  # 기본 선택값
drink_option_menu = tk.OptionMenu(window, drink_var, *menu_data.keys())
drink_option_menu.pack()

# 수량 입력 라벨
quantity_label = tk.Label(window, text="수량 입력:")
quantity_label.pack()

# 수량 입력 엔트리
quantity_var = tk.IntVar(window)
quantity_entry = tk.Entry(window, textvariable=quantity_var)
quantity_entry.pack()

# 주문 버튼
order_button = tk.Button(window, text="주문하기", command=order_drink)
order_button.pack()

# 추천메뉴 버튼
recommend_button = tk.Button(window, text="추천메뉴", command=scroll_to_top)
recommend_button.pack()

# 주문 결과 출력 라벨
result_label = tk.Label(window, text="")
result_label.pack()

# 메뉴 항목을 추가하는 함수
def add_menu_item(menu_frame, menu_name, menu_price):
    menu_item = tk.Label(menu_frame, text=f"{menu_name} - {menu_price}원")
    menu_item.pack()

# 메뉴 데이터를 기반으로 메뉴 항목 추가
for menu_name, menu_price in menu_data.items():
    add_menu_item(menu_frame, menu_name, menu_price)

# Canvas 스크롤 영역 설정
menu_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Canvas 스크롤바 동작 설정
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

# tkinter 이벤트 루프 실행
window.mainloop()
