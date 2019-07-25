# baekjoon_solutions
baekjoon solutions

## Tips
- *input()* 대신 *sys.stdin.readline()* 사용 (*import sys* 필요)
- *print()* 대신 *sys.stdout.write()* 사용 (*import sys* 필요, 줄바꿈 없음, string 형식만 가능)

- *sys.stdin = open("a.txt", "r")*
  - 문제의 입력을 a.txt에 저장
  
- 개행문자(\n) 제거
  - *a.rstrip()*
  
- 리스트 중복 제거
  - *a = list(set(a))*
  
- (중복 없이) 문자열에 나타나는 단어별로 보기
  - *for char in set(string):*
  
- 반복문 시 *range* 및 *enum*은 메모리 비효율적임
  - for 대신 while 사용 ---> 아니었음. python3에서 range를 list가 아니라 다르게 처리해서, 빠름.
  
- *split* 함수에서 empty string + specified split --> return ['']

- 같은 함수를 반복하여 사용할 때 = *map*
  - ex) string.count("a") + string.count("b") + ...    -->    sum(map(string.count, ["a","b",...]))
  
- sort 함수
  - 결과는 항상 낮->높. (내림차순은 *reverse=True*)
  - *a.sort()* : a를 sort하고 return은 없음. list만 가능.
  - *sorted(a, key=a.count)* : a를 key 기준으로 sort한 결과 return. a는 변하지 않음. list 및 string 가능.

- *int(a/10)* == *a//10*
  - 실행 시간 : (long) *int(a/10)* >> *a//10* (short)

- list, string의 [:::]
  - *[a : b : c]* 의 의미 = a부터 b까지, c 간격으로 출력
