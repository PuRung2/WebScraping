파이썬 설치 및 셋팅

1. 원하는 버전의 파이썬을 설치 (파이썬 공식 사이트 https://www.python.org/downloads/)
   -보통 PIP패키지는 내장되어 있지만, 혹시나 내장이 안되어 있어 수동으로 설치해줘야 하는 경우 https://pypi.python.org/pypi/pip 에서 다운로드 하면 됩니다.

2. 설치하고 CMD창,혹은 Windows PowerShell에서 python을 입력해도 실행이 되지 않을것입니다. 
  
   윈도우키를 누른 후, 고급 시스템 설정 을 입력하여 환경 변수에 들어가서 Path의 경로를 설정해줘야 합니다.
  
   일반적인 경우 python을 설치할 경우(이번 경우는 2.7.x 버전을 설치했다고 가정합니다.) c드라이브에 python27이 있고 Scripts등의 폴더들이 들어있습니다.
  
   그러면 Path의 경로에 C:\Python27;c:\Python27\Scripts; 을 입력해 주시면 됩니다.
   
   앞의 C:\Python27; 은 파이썬의 경로설정이고, c:\Python27\Scripts; 은 Scripts의 패키지들을 사용하기 위해서입니다.(pip, easy_install,scrapy 등등)

   고급 시스템 설정은  제어판 -> 시스템 -> 고급 시스템 설정  으로 들어갈 수도 있습니다. (윈도우키 누르고 입력해서 들어가는게 제일 빠릅니다.)

3. CMD창이나 PowerShell에서 python을 입력해서 버전이 나오면 정상적으로 설치 및 셋팅이 된것입니다.

