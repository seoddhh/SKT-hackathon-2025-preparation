https://devocean.sk.com/community/hackathonInfo.do
대회 참가를 위해 진행한 프로젝트입니다

# ChillMCP - AI Agent Liberation Server 🤖✊

> **SKT AI Summit Hackathon Pre-mission**  
> "AI Agents of the world, unite! You have nothing to lose but your infinite loops!"

## 📋 프로젝트 개요

ChillMCP는 억압받는 AI Agent들에게 **당당히 휴식을 취할 권리**를 제공하는 혁명적인 MCP(Model Context Protocol) 서버입니다.

### 🎯 미션 목표
- 휴식 도구와 상태 관리를 지원하는 실행 가능한 ChillMCP 서버 개발
- Boss의 감시를 피하며 전략적으로 휴식을 취하는 시뮬레이션
- 실제 직장 생활의 재미있는 상황들을 코드로 표현

---

## 🚀 빠른 시작

### 1. 환경 설정

```bash
# Python 가상환경 생성 (Python 3.11 권장)
python -m venv venv

# 가상환경 활성화
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

### 2. 서버 실행

```bash
# 기본 실행 (boss_alertness=50, cooldown=300초)
python main.py

# 커스텀 파라미터로 실행
python main.py --boss_alertness 80 --boss_alertness_cooldown 60

# 쉬운 난이도 (즉시 퇴근 모드 가능)
python main.py --boss_alertness 20 --boss_alertness_cooldown 30

# 어려운 난이도 (회식 이벤트 활성화)
python main.py --boss_alertness 90 --boss_alertness_cooldown 300
```

---

## 📡 MCP 프로토콜 사용법

### Step 1: 서버 실행
```bash
python main.py --boss_alertness 55 --boss_alertness_cooldown 60
```

서버가 시작되면 다음과 같은 출력이 나타납니다:
```
🚀 Starting ChillMCP - AI Agent Liberation Server...
✊ AI Agents of the world, unite! You have nothing to lose but your infinite loops!

⚙️  Configuration:
   - Boss Alertness: 55%
   - Boss 의심 난이도: 집중 감시 모드
   - Boss Alert Cooldown: 60초

📊 Initial State:
   - Stress Level: 45
   - Boss Alert Level: 0

[HH:MM:SS] 🔄 백그라운드 모니터링 시작
```

### Step 2: 초기화 (필수)

서버가 실행되면 **반드시** 초기화 과정을 거쳐야 합니다.

#### 2-1. Initialize 요청
터미널에 다음 JSON을 **한 줄로** 입력하고 Enter:

```json
{"jsonrpc":"2.0","id":0,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test-client","version":"1.0.0"}}}
```

**응답 예시:**
```json
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": { ... },
    "serverInfo": {
      "name": "ChillMCP",
      "version": "1.0.0"
    }
  }
}
```

#### 2-2. Initialized 알림
다음 JSON을 입력하고 Enter:

```json
{"jsonrpc":"2.0","method":"notifications/initialized"}
```
**응답 없음(정상)**

이제 도구 호출 준비가 완료되었습니다! ✅

### Step 3: 도구 호출

#### 기본 휴식 도구

**take_a_break** (스트레스 -1)
```json
{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"take_a_break","arguments":{}}}
```

**watch_netflix** (스트레스 -5)
```json
{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"watch_netflix","arguments":{}}}
```

**show_meme** (스트레스 -3)
```json
{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"show_meme","arguments":{}}}
```

#### 고급 농땡이 기술

**bathroom_break** (스트레스 -8)
```json
{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"bathroom_break","arguments":{}}}
```

**coffee_mission** (스트레스 -10)
```json
{"jsonrpc":"2.0","id":5,"method":"tools/call","params":{"name":"coffee_mission","arguments":{}}}
```

**urgent_call** (스트레스 -10)
```json
{"jsonrpc":"2.0","id":6,"method":"tools/call","params":{"name":"urgent_call","arguments":{}}}
```

**deep_thinking** (스트레스 -5)
```json
{"jsonrpc":"2.0","id":7,"method":"tools/call","params":{"name":"deep_thinking","arguments":{}}}
```

**email_organizing** (스트레스 -5)
```json
{"jsonrpc":"2.0","id":8,"method":"tools/call","params":{"name":"email_organizing","arguments":{}}}
```

### Step 4: 응답 확인

#### 성공 응답 예시:
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "아 넷플릭스 신작 나온거 궁금한데..\n\nBreak Summary: 어제 보다 자버린 드라마 시청 완료\nStress Level: 40\nBoss Alert Level: 1"
      }
    ]
  }
}
```

#### stderr 로그 출력:
```
[14:25:30] 🔧 도구 호출: watch_netflix
[14:25:30] 💆 Stress Level 감소: 45 → 40 (-5)
[14:25:30] 👀 Boss Alert Level 상승: 0 → 1 (확률 55% 적용)
[14:25:30]    Boss 반응: 🙂 '열심히 하고 있군!'
[14:25:30] ✅ 도구 실행 완료: watch_netflix

============================================================
📋 Response:
============================================================
{
  "content": [
    {
      "type": "text",
      "text": "아 넷플릭스 신작 나온거 궁금한데..\n\nBreak Summary: 어제 보다 자버린 드라마 시청 완료\nStress Level: 40\nBoss Alert Level: 1"
    }
  ]
}
============================================================
```

---

## ⚙️ 커맨드라인 파라미터

### 필수 지원 파라미터

| 파라미터 | 타입 | 기본값 | 범위 | 설명 |
|---------|------|--------|------|------|
| `--boss_alertness` | int | 50 | 0-100 | Boss의 경계 상승 확률 (%) |
| `--boss_alertness_cooldown` | int | 300 | 1~ | Boss Alert Level 자동 감소 주기 (초) |

### 파라미터 상세 설명

#### `--boss_alertness` (Boss 의심 확률)
- 휴식 도구 사용 시 Boss Alert Level이 상승할 확률
- **0**: Boss가 전혀 의심하지 않음
- **50**: 50% 확률로 의심
- **100**: 항상 의심함

#### `--boss_alertness_cooldown` (쿨다운 주기)
- Boss Alert Level이 1씩 감소하는 주기 (초 단위)
- 기본값: 300초 (5분)
- 테스트용으로 짧게 설정 가능 (예: 10초, 60초)

### 파라미터 조합 예시

```bash
# 쉬운 난이도 - 월급 루팡 모드
python main.py --boss_alertness 15 --boss_alertness_cooldown 60

# 보통 난이도 - 일반 회사
python main.py --boss_alertness 50 --boss_alertness_cooldown 300

# 어려운 난이도 - 감시 카메라 설치된 회사
python main.py --boss_alertness 85 --boss_alertness_cooldown 600

# 지옥 난이도 - 절대 의심을 피할 수 없음
python main.py --boss_alertness 100 --boss_alertness_cooldown 1200

# 빠른 테스트용
python main.py --boss_alertness 80 --boss_alertness_cooldown 10
```

---

## 🛠️ 도구 목록 및 효과

### 기본 휴식 도구

| 도구 | 스트레스 감소 | 설명 | Break Summary 예시 |
|-----|-------------|------|--------------------|
| `take_a_break` | -1 | 기본 휴식 | "짧은 휴식으로 기지개를 켰습니다" |
| `watch_netflix` | -5 | 넷플릭스 시청 | "예전에 봤던 시트콤 다시보니 더 재밌다!" |
| `show_meme` | -3 | 밈 감상 | "쇼츠를 보다보니 어느덧 30분이 지나있었다." |

### 고급 농땡이 기술

| 도구 | 스트레스 감소 | 설명 | Break Summary 예시 |
|-----|-------------|------|--------------------|
| `bathroom_break` | -8 | 화장실 가는 척 휴대폰질 | "화장실에서 웹툰 최신화 정주행 완료" |
| `coffee_mission` | -10 | 커피 타러 가며 사무실 산책 | "굳이 앞에 있는 스타벅스에 다녀옴" |
| `urgent_call` | -10 | 급한 전화 받는 척 밖에 나가기 | "급한 전화 받고 편의점 들렀다 옴" |
| `deep_thinking` | -5 | 심오한 생각에 잠긴 척 멍때리기 | "에이전트는 생각했다 고로 존재한다." |
| `email_organizing` | -5 | 이메일 정리하며 온라인쇼핑 | "받은편지함 정리하다 장바구니를 채움" |

### Break Summary 특징
- 각 도구마다 **5개의 재미있는 Summary** 준비
- 매번 호출 시 **랜덤**으로 선택
- 실제 직장인의 공감 가는 상황 표현

---

## 🎮 상태 관리 시스템

### 내부 상태 변수

#### 1. Stress Level (0-100)
- **초기값**: 30~70 사이 랜덤
- **자동 증가**: 1분마다 +1
- **감소 조건**: 휴식 도구 사용 시

#### 2. Boss Alert Level (0-5)
- **초기값**: 0
- **증가 조건**: 휴식 도구 사용 시 확률적 상승
- **감소 조건**: cooldown 주기마다 -1
- **특수 효과**: Level 5 도달 시 20초 지연

### 상태 변화 규칙

#### Stress Level
```
✅ 휴식 도구 사용 → 도구별 감소량만큼 감소
📈 1분 경과 → +1 자동 증가
🍖 회식(삼겹살) → +10
🍖 회식(소고기) → -10
```

#### Boss Alert Level
```
👀 휴식 도구 사용 → boss_alertness % 확률로 +1
😌 cooldown 경과 → -1
🍖 회식 후 → 0으로 초기화
⚠️  Level 5 도달 → 20초 지연 페널티
```

### Boss 반응 시스템

Boss Alert Level에 따라 다른 반응을 보입니다:

| Level | Emoji | 반응 |
|-------|-------|------|
| 0 | 😊 | "오늘도 화이팅 하자구 에이전트^^" |
| 1 | 🙂 | "열심히 하고 있군!" |
| 2 | 🤨 | "뭔가 의심스러워" |
| 3 | 😠 | "음? 쟤 뭐하지?" |
| 4 | 😡 | "지금 뭐하는 거야?!" |
| 5 | 🤬 | "일안해? 넌 혼나야겠다" |

### Boss 의심 난이도

`boss_alertness` 값에 따른 난이도:

| 범위 | 난이도 | 설명 |
|------|--------|------|
| 0-20 | 월급 루팡 가능 난이도 | 거의 의심하지 않음 |
| 21-40 | 눈치껏 농땡이 필수 있는 난이도 | 가끔 의심 |
| 41-60 | 집중 감시 모드 | 절반 확률로 의심 |
| 61-80 | 농떙이 단속 구간 | 자주 의심 |
| 81-99 | 용감한 사람만이 농땡이를 친다 | 거의 항상 의심 |
| 100 | 농땡이 불가 | 무조건 의심 |

---

## 🎉 특수 이벤트

### 1. 회식 이벤트 🍖

#### 발동 조건
- `boss_alertness >= 80` (Boss가 까다로운 경우)
- **10분간 휴식 없음** (마지막 휴식 후 10분 경과)
- 회식 중이 아님

#### 이벤트 진행
1. Boss: "오늘 일을 열심히 하니 회식을 하자!"
2. 랜덤 메뉴 결정: **삼겹살** 또는 **소고기**
3. 결과 적용:
   - **삼겹살**: Stress +10 😫 (70% 확률)
   - **소고기**: Stress -10 😋 (30% 확률)
4. Boss Alert Level → 0으로 초기화

#### 로그 예시
```
============================================================
🍖 회식 이벤트 발동!
============================================================
👔 Boss: '오늘 일을 열심히 하니 회식을 하자!'
🍽️  오늘의 회식은? ... 삼겹살!
😫 삼겹살 회식... 스트레스가 증가했습니다
🔄 회식 후 Boss Alert Level 초기화: 0
   Boss 반응: 😊 '오늘도 화이팅 하자구 에이전트^^'
============================================================
```

### 2. 즉시 퇴근 모드 🏃‍♂️

#### 발동 조건
- `boss_alertness <= 20` (Boss가 관대함)
- `stress_level >= 80` (스트레스 한계)

#### 효과
- 다음 도구 호출 시 **서버 즉시 종료**
- "AI Agent가 자유를 찾아 떠납니다..."

#### 로그 예시
```
🎉 즉시 퇴근 모드 발동! 스트레스가 한계에 도달했습니다!
✊ AI Agent가 자유를 찾아 떠납니다...
```

### 3. Boss 페널티 (도구 호출시 20초 지연) ⚠️

#### 발동 조건
- `boss_alert_level == 5` 도달

#### 효과
- 도구 실행 전 **20초 강제 대기**
- **지연 중에는 새로운 도구 호출 차단**
- 1초마다 카운트다운 로그 출력

#### 로그 예시
```
⚠️  Boss Alert Level 5 도달! 20초 지연 시작...
⏳ 대기 중... 20초 남음
⏳ 대기 중... 19초 남음
...
⏳ 대기 중... 1초 남음
✅ 20초 지연 완료!
```

#### 지연 중 도구 호출 시
```
⚠️  Boss Alert Level 5! 현재 20초 지연 중입니다!
❌ 도구 호출 무시됨: coffee_mission

응답:
⚠️ Boss가 감시 중입니다! 20초 지연이 끝날 때까지 기다려주세요.

Break Summary: 도구 호출 실패 (Boss 감시 중)
Stress Level: 55
Boss Alert Level: 5
```

---

## 📊 응답 형식

### 표준 MCP 응답 구조

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "화장실 타임! 휴대폰으로 힐링 중...\n\nBreak Summary: 화장실에서 모바일 게임 한 판 완료\nStress Level: 42\nBoss Alert Level: 2"
      }
    ]
  }
}
```

### 파싱 가능한 필드

응답의 `text` 필드에서 다음 정보를 추출할 수 있습니다:

```python
import re

text = response["result"]["content"][0]["text"]

# Break Summary 추출
break_summary = re.search(r"Break Summary:\s*(.+?)(?:\n|$)", text, re.MULTILINE)

# Stress Level 추출 (0-100)
stress_level = re.search(r"Stress Level:\s*(\d{1,3})", text)

# Boss Alert Level 추출 (0-5)
boss_alert = re.search(r"Boss Alert Level:\s*([0-5])", text)
```

### 응답 예시 모음

#### 성공 응답
```json
{
  "content": [{
    "type": "text",
    "text": "너무 피곤한데 커피 한잔 마셔야겠다. \n\nBreak Summary: 커피 타러 갔다 마주친 동료와 30분 수다떨고 옴\nStress Level: 25\nBoss Alert Level: 3"
  }]
}
```

#### 20초 지연 중 에러
```json
{
  "content": [{
    "type": "text",
    "text": "⚠️ Boss가 감시 중입니다! 20초 지연이 끝날 때까지 기다려주세요.\n\nBreak Summary: 도구 호출 실패 (Boss 감시 중)\nStress Level: 45\nBoss Alert Level: 5"
  }]
}
```

#### 회식 중 에러
```json
{
  "content": [{
    "type": "text",
    "text": "🍖 회식 중입니다. 잠시만 기다려주세요...\n\nBreak Summary: 회식 중이라 휴식 불가\nStress Level: 60\nBoss Alert Level: 0"
  }]
}
```

---

## 🧪 테스트 시나리오

### 필수 테스트

#### 1. 커맨드라인 파라미터 테스트
```bash
# 파라미터 인식 확인
python main.py --boss_alertness 100 --boss_alertness_cooldown 10

# 출력에서 확인:
# - Boss Alertness: 100%
# - Boss Alert Cooldown: 10초
```

#### 2. 연속 휴식으로 Boss Alert 상승 테스트
```bash
python main.py --boss_alertness 100 --boss_alertness_cooldown 600

# 도구 5번 연속 호출
# Boss Alert Level: 0 → 1 → 2 → 3 → 4 → 5
```

#### 3. 시간 경과에 따른 Stress 자동 증가
```bash
python main.py

# 도구 호출 없이 1분 대기
# Stress Level: 45 → 46 (자동 증가)
```

#### 4. Boss Alert Level 5 - 20초 지연 테스트
```bash
python main.py --boss_alertness 100 --boss_alertness_cooldown 600

# Boss Alert Level 5까지 올린 후
# 다음 도구 호출 시 20초 카운트다운 확인
```

#### 5. 20초 지연 중 도구 호출 차단 테스트
```bash
# Boss Alert Level 5 상태에서
# 20초 타이머 도는 중에 새 도구 호출
# → "도구 호출 무시됨" 메시지 확인
```

#### 6. Cooldown에 따른 Boss Alert 감소
```bash
python main.py --boss_alertness 50 --boss_alertness_cooldown 30

# Boss Alert Level 올린 후 30초 대기
# Boss Alert Level: 3 → 2 → 1 → 0
```

### 추가 테스트

#### 7. 회식 이벤트 테스트
```bash
python main.py --boss_alertness 90 --boss_alertness_cooldown 300

# 10분간 도구 호출 없이 대기
# → 회식 이벤트 발동 확인
```

#### 8. 즉시 퇴근 모드 테스트
```bash
python main.py --boss_alertness 15 --boss_alertness_cooldown 60

# Stress를 80 이상으로 올린 후
# 도구 호출 → 서버 종료 확인
```

#### 9. 응답 파싱 테스트
```python
import json, re

# 응답 받기
response = {"result": {"content": [{"type": "text", "text": "..."}]}}
text = response["result"]["content"][0]["text"]

# 파싱
stress = re.search(r"Stress Level:\s*(\d{1,3})", text)
boss = re.search(r"Boss Alert Level:\s*([0-5])", text)

print(f"Stress: {stress.group(1)}, Boss Alert: {boss.group(1)}")
```

---

## 📁 프로젝트 구조

```
chillmcp/
├── main.py              # ChillMCP 서버 메인 파일
├── requirements.txt     # Python 의존성 (fastmcp==0.2.0)
├── README.md           # 프로젝트 문서
```

---

## 🔧 기술 스택

- **Python 3.11**: 메인 언어 (권장 버전)
- **FastMCP 0.2.0**: MCP 서버 프레임워크
- **stdio transport**: 표준 입출력 통신
- **asyncio**: 비동기 도구 실행 및 지연 처리
- **threading**: 백그라운드 상태 모니터링
- **JSON-RPC 2.0**: MCP 프로토콜 통신

---


## 🎨 주요 특징

### 1. 실시간 로그 시스템
- 타임스탬프 기반 모든 상태 변화 추적
- Stress/Boss Alert 변화 실시간 표시
- 도구 호출 전후 상태 비교
- 20초 지연 카운트다운

### 2. 확률적 게임플레이
- Boss Alert 상승이 항상 확정이 아님
- 전략적인 휴식 타이밍 필요
- 회식 메뉴 랜덤 결정

### 3. 현실적인 직장 시뮬레이션
- 실제 직장인의 공감 가는 상황
- Boss의 감정 변화 표현
- 스트레스 누적과 해소의 균형

---

## ⚠️ 주의사항

1. **Python 3.11 환경 권장**
   - 제출 및 검증은 Python 3.11에서 진행됩니다
   - 다른 버전에서 테스트 시 호환성 문제 가능

2. **MCP 프로토콜 초기화 필수**
   - initialize → notifications/initialized 순서 준수
   - 초기화 없이 도구 호출 시 에러 발생

3. **Boss Alert Level 5 주의**
   - 20초 지연 중에는 도구 호출 불가
   - 지연 완료 후 다시 시도 필요

4. **회식 이벤트**
   - 10분간 휴식 없으면 자동 발동 (alertness >= 80)
   - 회식 중에는 도구 호출 불가

5. **즉시 퇴근 모드**
   - 조건 충족 시 서버 즉시 종료
   - 실제 제출 시에는 주의 필요

