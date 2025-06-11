CREATE TABLE banks (
       bank_id NUMBER PRIMARY KEY,
       bank_name VARCHAR2(100) UNIQUE
   );

   CREATE TABLE reviews (
       review_id NUMBER PRIMARY KEY,
       review VARCHAR2(2000),
       rating NUMBER,
       review_date DATE,
       bank_id NUMBER,
       source VARCHAR2(50),
       FOREIGN KEY (bank_id) REFERENCES banks(bank_id)
   );