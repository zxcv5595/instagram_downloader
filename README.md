# instagram_downloader
인스타그램 비디오 파일 다운로더 입니다  / This is an Instagram video file downloader

[release [ instagram_downloader.exe ]](https://github.com/zxcv5595/instagram_downloader/releases/tag/v0.0.1)

---
사용법 / HOW TO USE
---
- 먼저 동영상을 다운받고 싶은 게시물들의 url를 수집합니다.
- 저는 인스타그램의 공유하기 기능으로, 고양이 게시물들을 개인메세지에 모아 놓곤합니다. 😻 


　

- First, collect the URLs of the posts from which you want to download videos.
- I often use Instagram's share feature to gather cat posts in a private message. 😻



<img src='https://github.com/zxcv5595/instagram_downloader/assets/109198584/2718898e-8e33-46c7-97a4-92f47af87974' style='width: 300px; height: auto;'>
　

---
-  수집한 url들을 instagram.xlsx 파일, 'Links' 컬럼 아래 붙혀넣습니다.
- 알아서 '/문자열/' 형태를 가진 게시물의 id만을 파싱 해주기 때문에 사진과 같이 붙혀넣어도 상관없습니다. (ex : '/CylSlgtx4wM/')

　

- Paste the collected URLs into the 'Links' column of the instagram.xlsx file.
- It automatically parses only the post IDs in the '/string/' format, so it's fine to paste them as shown in the image (e.g., '/CylSlgtx4wM/').

<img src='https://github.com/zxcv5595/instagram_downloader/assets/109198584/1fb059d9-96da-4a7b-9c36-0e9778f58805' style='width: 600px; height: auto;'>

---

- 엑셀파일을 저장한 후, 실행파일을 실행시켜 주세요 (instagram_downloader.exe)

　

- Please save the Excel file, and then run the executable file named "instagram_downloader.exe".





<img src='https://github.com/zxcv5595/instagram_downloader/assets/109198584/e5c72632-1391-4f2f-b9ce-2b63bd270721' style='width: 300px; height: auto;'>


　


- 동작 코드는 아래와 같습니다. 
- xlsx 파일명과 컬럼명을 확인해주세요.

　

- The functioning code is as follows. 
- Please verify the name of the xlsx file and the column names.

```python
# Reading addresses from an Excel file
excel_file = "instagram.xlsx"
df = pd.read_excel(excel_file)
urls = df['Links'].tolist()
```

---
- [ 실행화면 ] 인스타그램 아이디와 비밀번호를 입력해주세요

　

- [Execution Screen] Please enter your Instagram username and password.


<img src='https://github.com/zxcv5595/instagram_downloader/assets/109198584/f144eb56-a188-4597-883a-22db3d3eb4a4' style='width: 700px; height: auto;'>


---
- 'Downloads' 폴더가 생성되면서, 동영상파일이 잘 다운받아진 것을 확인 할 수 있습니다. 
😎

　

- The 'Downloads' folder has been created, and you can confirm that the video files have been successfully downloaded. 😎


<img src='https://github.com/zxcv5595/instagram_downloader/assets/109198584/e76c20d1-f045-4aa8-bcc9-c8134fbc9403' style='width: 300px; height: auto;'>

　

<img src='https://github.com/zxcv5595/instagram_downloader/assets/109198584/c921c999-874e-4eda-87b8-5eda68c30431' style='width: 500px; height: auto;'>

---
##  출처 / SOURCE

<ul>
  <li><code>instaloader</code>: Instagram에서 데이터를 크롤링하는 라이브러리로, Instagram 게시물을 다운로드하는 데 사용됩니다. <br>
    출처: <a href="https://instaloader.github.io/">Instaloader Documentation</a>.</li><br>
  <li><code>pandas</code>: 데이터 분석 및 조작을 위한 라이브러리로, Excel 파일에서 URL 목록을 가져오는 데 사용됩니다.<br>
    출처: <a href="https://pandas.pydata.org/">pandas Documentation</a>.</li><br>
  <li><code>concurrent.futures</code>: 비동기 실행을 위한 고수준 인터페이스를 제공하는 모듈로, 동시에 여러 Instagram 게시물을 다운로드하는 데 사용됩니다.<br>
    출처: <a href="https://docs.python.org/3/library/concurrent.futures.html">concurrent.futures Documentation</a>.</li><br>
  <li><code>os</code>: 운영 체제와 상호 작용하는 기능을 제공하는 모듈로, 다운로드 폴더 생성 및 파일 시스템 작업에 사용됩니다.<br>
    출처: <a href="https://docs.python.org/3/library/os.html">os Documentation</a>.</li><br>
  <li><code>re</code>: 정규 표현식을 사용하여 문자열을 처리하는 모듈로, URL에서 특정 패턴을 찾는 데 사용됩니다.<br>
    출처: <a href="https://docs.python.org/3/library/re.html">re Documentation</a>.</li><br>
  <li><code>tqdm</code>: 진행 상황 표시줄을 제공하는 라이브러리로, 다운로드 진행 상황을 시각적으로 표시하는 데 사용됩니다.<br>
    출처: <a href="https://tqdm.github.io/">tqdm Documentation</a>.</li><br>
  <li><code>multiprocessing</code>: 멀티프로세싱을 위한 함수를 포함하는 모듈로, 특히 Windows에서 멀티프로세싱을 사용할 때 필요합니다.<br>
    출처: <a href="https://docs.python.org/3/library/multiprocessing.html">multiprocessing Documentation</a>.</li><br>
</ul>


<!-- 
Instagram Downloader

인스타그램 다운로드

인스타 다운로드

인스타그램 다운

인스타 다운

Instagram 동영상 다운로드

Insta 동영상 다운로드

Instagram 동영상 다운

Insta 동영상 다운

Instagram Video Saver

인스타그램 비디오 저장

Social Media Video Grabber

소셜 미디어 비디오 추출

Open Source Instagram Tool

Instagram 다운로드 소스 코드

인스타그램 비디오 추출 도구
-->






