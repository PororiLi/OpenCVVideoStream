import cv2
 
########### URL 영상 스트림  ############
# 실시간 영상 스트리밍 되는데 control+c 로 강제종료 해야함. 다른 종료 방법 찾아봐야 할듯
# python 3.7.9 버전
# pip install openCV-python 설치
# Windows/System32/ffmpeg.dll 넣어주기
# 영상 틀어둔 만큼 녹화되고, 영상 안보고 녹화만 할 수도 있음.
#########################################################
 
url = 'url' #여기에 영상 리스트  
cap=cv2.VideoCapture(url)

 
# frame 사이즈
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)
 
# 코덱 설정하기
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # ('D', 'I', 'V', 'X')
fourcc = cv2.VideoWriter_fourcc(*'mp4v') #('M','P','4','V') mp4 형식으로 파일 저장.
print("hi")
 
# 이미지 저장하기 위한 영상 파일 생성
out1 = cv2.VideoWriter('C:/etc/record0.mp4',fourcc, 20.0, frame_size)
# out2 = cv2.VideoWriter('./data/record1.mp4',fourcc, 20.0, frame_size,isColor=False)
print("hi2") 
while True:
    print("while")
    ret, frame = cap.read()	# 영상을 한 frame씩 읽어오기
    if not ret:
        print("beak")
        break   
    out1.write(frame)	# 영상 파일에 저장   
    
    # # 이미지 컬러 변환
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # out2.write(gray)	# 영상 파일에 저장        
    
    # cv2.imshow("frame",frame)	# 이미지 보여주기
    
    key = cv2.waitKey(25)
    if key == ord('q'):
        break

print("while out")        
cap.release()	# 객체 해제
out1.release()
print("release1")
# out2.release()
cv2.destroyAllWindows()