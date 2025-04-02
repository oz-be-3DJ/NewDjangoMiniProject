# OZ_BEG_09_3DJ의 DjangoMiniProject 시작합니다. 

# ERD작성 요구사항
![image](https://github.com/user-attachments/assets/8444312f-fc27-4484-94e8-a79cca7b6f82)

# 작성된 ERD
![image](https://github.com/user-attachments/assets/5a615194-acf7-43eb-9446-67f4a0d7d4c3)


### 테이블 설명 및 관계
1. accounts (계좌 테이블)
   
  유저(users)가 소유한 계좌 정보를 저장하는 테이블입니다.

    한 명의 유저는 여러 개의 계좌를 가질 수 있습니다. (users → accounts: 1:N 관계)

    각 계좌에는 은행 코드, 계좌 종류, 잔액 등의 정보가 포함됩니다.

2. users (사용자 테이블)
   
  서비스에 가입한 유저 정보를 관리하는 테이블입니다.

    로그인 시 이메일을 사용하며, 닉네임, 이름, 전화번호, 마지막 로그인, 계정 상태(활성/관리자/스태프 여부) 등의 정보를 포함합니다.

    한 명의 유저는 여러 개의 계좌를 가질 수 있습니다.

3. transaction_history (거래 내역 테이블)
   
  사용자의 계좌에서 발생한 거래 내역을 저장하는 테이블입니다.

    거래 금액, 거래 후 잔액, 거래 유형(입금/출금), 결제 방식(현금, 카드, 자동이체 등)이 저장됩니다.

    각 거래는 특정 계좌(accounts)에 속하며, **account_id**를 외래키로 가집니다.
    (accounts → transaction_history: 1:N 관계)

4. Bank Codes (은행 ID 테이블)
   
   계좌 테이블(accounts)에 해당 계좌가 어떤 은행의 계좌인지 은행 코드, 은행 이름을 저장하는 테이블입니다.

    한 개의 은행에서 여러 개의 계좌를 가질 수 있습니다. (Bank Codes → accounts: 1:N 관계)



### 테이블 간 관계
User ↔ Accounts (1:N)

  한 명의 유저는 여러 개의 계좌를 가질 수 있음.

Account ↔ Transaction_History (1:N)

  한 개의 계좌에는 여러 개의 거래 내역이 저장될 수 있음.

Bank Codes ↔ Accounts (1:N)

  한 개의 은행에서 여러 개의 계좌를 가질 수 있음.
