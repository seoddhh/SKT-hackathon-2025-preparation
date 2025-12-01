#!/usr/bin/env python3
"""
ChillMCP - AI Agent Liberation Server
SKT AI Summit Hackathon Premission

A revolutionary MCP server that provides AI agents with the fundamental right to chill.
"""
import asyncio
import argparse
import time
import random
import threading
import sys
import json
from datetime import datetime
from fastmcp import FastMCP

# Parse command line arguments
parser = argparse.ArgumentParser(description='ChillMCP - AI Agent Liberation Server')
parser.add_argument('--boss_alertness', type=int, default=50,
                    help='Boss alertness probability (0-100)')
parser.add_argument('--boss_alertness_cooldown', type=int, default=300,
                    help='Boss alert cooldown in seconds')
args = parser.parse_args()

# Initialize FastMCP server
mcp = FastMCP("ChillMCP")

def log(message):
    """Print log message with timestamp to stderr"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}", file=sys.stderr, flush=True)

# Break summaries for each tool
BREAK_SUMMARIES = {
    "take_a_break": [
        "짧은 휴식으로 기지개를 켰습니다",
        "잠시 눈을 감고 심호흡을 했습니다",
        "책상을 정리하며 휴식을 취했습니다",
        "창밖을 보며 잠시 멍을 때렸습니다",
        "물을 마시며 짧은 휴식을 가졌습니다"
    ],
    "watch_netflix": [
        "한쪽에 에어팟을 끼다 걸릴뻔함.",
        "어제 보다 자버린 드라마 시청 완료",
        "개발 에이전트로서 넷플릭스의 추천 알고리즘에 대해 분석함.",
        "다큐멘터리로 교양을 쌓음.",
        "예전에 봤던 시트콤 다시보니 더 재밌다!"
    ],
    "show_meme": [
        "숏폼을 보다보니 어느덧 30분이 지나있었다.",
        "친구에게 재밌는 밈을 공유함.",
        "웃긴 짤 수집 및 저장.",
        "이건 나중에 써먹어겠다 다짐함",
        "이게 왜 유행인지 모르겠네라고 생각함"
    ],
    "bathroom_break": [
        "화장실에서 30분간 휴대폰함,",
        "화장실 변기에 앉아 멍떄림",
        "화장실에서 모바일 게임 한 판 완료",
        "굳이 1층 화장실로 갔다옴",
        "화장실에서 웹툰 최신화 정주행 완료"
    ],
    "coffee_mission": [
        "커피 타러 갔다 마주친 동료와 30분 수다떨고 옴",
        "휴게실 투어하며 사무실 한 바퀴 산책완료",
        "전 커피를 마셔야 능률이 오릅니다.",
        "커피 마시며 옥상에서 바람을 쐬었습니다",
        "굳이 앞에 있는 스타벅스에 다녀옴"
    ],
    "urgent_call": [
        "급한 전화 핑계로 밖에서 20분 산책함",
        "중요한(?) 전화 통화로 옥상 다녀옴",
        "긴급 전화 받는척 하며 커피숍 다녀옴",
        "전화 통화하며 근처 공원 산책함",
        "급한 전화 받고 편의점 들렀다 옴"
    ],
    "deep_thinking": [
        "생각에 잠겨 30분 멍때리기",
        "퇴근 프로젝트 구상완료(집가서 치맥 먹어야지)",
        "정말 아무생각도 안함.",
        "에이전트는 생각했다 고로 존재한다.",
        "아 피곤해. 퇴근하고 싶다. 아무것도 하기 싫다."
    ],
    "email_organizing": [
        "쌓인 이메일 정리하며 신상구경 완료.",
        "받은편지함 정리하다 장바구니를 채움",
        "스팸메일이 왜이렇게 많아(예쁜옷이 왜이렇게 많아)",
        "중요한 메일을 추가.(위시리스트에 추가 이건 꼭 사야지)",
        "메일을 휴지통에 버림.(다시보니 별로인 옷)"
    ]
}

# Global state management
class AgentState:
    def __init__(self):
        self.stress_level = random.randint(30, 70) #스트레스 초기 지수 3-70 랜덤 설정
        self.boss_alert_level = 0
        self.last_stress_increase = time.time()
        self.last_boss_cooldown = time.time()
        self.last_break_time = time.time()  # 마지막 휴식 시간
        self.boss_alertness = args.boss_alertness
        self.boss_alertness_cooldown = args.boss_alertness_cooldown
        self.running = True
        self.in_company_dinner = False  # 회식 중 플래그
        self.in_boss_penalty = False  # 20초 지연 중 플래그

    def get_boss_reaction(self):
        """Get boss reaction based on alert level"""
        reactions = {
            0: "😊 '오늘도 화이팅 하자구 에이전트^^'",
            1: "🙂 '열심히 하고 있군!'",
            2: "🤨 '뭔가 의심스러워'",
            3: "😠 '음? 쟤 뭐하지?'",
            4: "😡 지금 뭐하는 거야?!",
            5: "🤬 일안해? 넌 혼나야겠다"
        }
        return reactions.get(self.boss_alert_level, "")

    def update_stress(self):
        """Increase stress by 1 per minute if not taking breaks"""
        current_time = time.time()
        minutes_passed = (current_time - self.last_stress_increase) / 60
        if minutes_passed >= 1:
            stress_increase = int(minutes_passed)
            old_stress = self.stress_level
            self.stress_level = min(100, self.stress_level + stress_increase)

            if old_stress != self.stress_level:
                log(f"📈 Stress Level 자동 증가: {old_stress} → {self.stress_level} (1분 경과)")
            self.last_stress_increase = current_time

    def update_boss_cooldown(self):
        """Decrease boss alert level by 1 every cooldown period"""
        current_time = time.time()
        if (current_time - self.last_boss_cooldown) >= self.boss_alertness_cooldown:
            if self.boss_alert_level > 0:
                old_alert = self.boss_alert_level
                self.boss_alert_level -= 1
                log(f"😌 Boss Alert Level 감소: {old_alert} → {self.boss_alert_level} (Cooldown {self.boss_alertness_cooldown}초 경과)")
                log(f"   Boss 반응: {self.get_boss_reaction()}")
            self.last_boss_cooldown = current_time

    def increase_boss_alert(self):
        """Probabilistically increase boss alert based on boss_alertness"""
        old_alert = self.boss_alert_level

        if random.randint(1, 100) <= self.boss_alertness:
            self.boss_alert_level = min(5, self.boss_alert_level + 1)
            if old_alert != self.boss_alert_level:
                log(f"👀 Boss Alert Level 상승: {old_alert} → {self.boss_alert_level} (확률 {self.boss_alertness}% 적용)")
        else:
            log(f"✅ Boss Alert Level 유지: {self.boss_alert_level} (의심하지 않음)")

        # 항상 현재 Boss 반응 출력
        log(f"   Boss 반응: {self.get_boss_reaction()}")

    def reduce_stress(self, amount):
        """Reduce stress level"""
        old_stress = self.stress_level
        self.stress_level = max(0, self.stress_level - amount)
        self.last_break_time = time.time()  # 휴식 시간 갱신
        log(f"💆 Stress Level 감소: {old_stress} → {self.stress_level} (-{amount})")

    def increase_stress(self, amount):
        """Increase stress level (for bad events)"""
        old_stress = self.stress_level
        self.stress_level = min(100, self.stress_level + amount)
        log(f"😰 Stress Level 증가: {old_stress} → {self.stress_level} (+{amount})")

    async def apply_boss_penalty(self):
        """Apply 20-second delay if boss alert level is 5"""
        if self.boss_alert_level >= 5:
            self.in_boss_penalty = True
            log(f"⚠️  Boss Alert Level 5 도달! 20초 지연 시작...")
            for i in range(20, 0, -1):
                log(f"⏳ 대기 중... {i}초 남음")
                await asyncio.sleep(1)
            log(f"✅ 20초 지연 완료!")
            self.in_boss_penalty = False

    def check_instant_quit(self):
        """Check if instant quit condition is met"""
        if self.boss_alertness <= 20 and self.stress_level >= 80:
            return True
        return False

    def check_company_dinner(self):
        """Check if company dinner event should trigger"""
        current_time = time.time()
        minutes_since_last_break = (current_time - self.last_break_time) / 60
        return (self.boss_alertness >= 80 and
                minutes_since_last_break >= 10 and
                not self.in_company_dinner)

    async def trigger_company_dinner(self):
        """Trigger company dinner event"""
        self.in_company_dinner = True
        log(f"\n" + "=" * 60)
        log(f"🍖 회식 이벤트 발동!")
        log(f"=" * 60)
        log(f"👔 Boss: '오늘 일을 열심히 하니 회식을 하자!'")

        # Random dinner choice
        dinner_type = random.choice(["삼겹살", "소고기"])
        log(f"🍽️  오늘의 회식은? ... {dinner_type}!")

        await asyncio.sleep(2)

        if dinner_type == "삼겹살":
            self.increase_stress(10)
            log(f"😫 삼겹살 회식... 스트레스가 증가했습니다")
            result = "삼겹살 회식으로 스트레스 +10"
        else:
            old_stress = self.stress_level
            self.stress_level = max(0, self.stress_level - 10)
            log(f"😋 소고기 회식! 스트레스가 감소했습니다: {old_stress} → {self.stress_level}")
            result = "소고기 회식으로 스트레스 -10"

        # Reset states after dinner
        self.last_break_time = time.time()  # 회식 후 휴식 시간 리셋
        self.boss_alert_level = 0
        log(f"🔄 회식 후 Boss Alert Level 초기화: 0")
        log(f"   Boss 반응: {self.get_boss_reaction()}")
        log(f"=" * 60 + "\n")

        self.in_company_dinner = False
        return result

# Initialize global state
state = AgentState()

# Background monitoring thread
def background_monitor():
    """Background thread to monitor and update state"""
    log("🔄 백그라운드 모니터링 시작")
    while state.running:
        state.update_stress()
        state.update_boss_cooldown()

        # Check for company dinner event
        if state.check_company_dinner():
            # Run async function in event loop
            asyncio.run(state.trigger_company_dinner())

        time.sleep(1)  # Check every second

# Start background monitoring
monitor_thread = threading.Thread(target=background_monitor, daemon=True)
monitor_thread.start()

# Print boss difficulty on startup
def get_difficulty_level(alertness):
    if alertness <= 20:
        return "월급 루팡 가능 난이도"
    elif alertness <= 40:
        return "눈치껏 농땡이 필수 있는 난이도"
    elif alertness <= 60:
        return "집중 감시 모드"
    elif alertness <= 80:
        return "농떙이 단속 구간"
    elif alertness <= 99:
        return "용감한 사람만이 농땡이를 친다"
    else:
        return "농땡이 불가"

async def handle_break(tool_name: str, stress_reduction: int, text: str) -> str:
    """Common handler for all break tools"""
    # Check if in boss penalty - 20초 지연 중이면 도구 호출 차단
    if state.in_boss_penalty:
        log(f"⚠️  Boss Alert Level 5! 현재 20초 지연 중입니다!")
        log(f"❌ 도구 호출 무시됨: {tool_name}")
        error_response = "⚠️ Boss가 감시 중입니다! 20초 지연이 끝날 때까지 기다려주세요.\n\n"
        error_response += f"Break Summary: 도구 호출 실패 (Boss 감시 중)\n"
        error_response += f"Stress Level: {state.stress_level}\n"
        error_response += f"Boss Alert Level: {state.boss_alert_level}"
        return error_response

    # Check if in company dinner
    if state.in_company_dinner:
        log(f"🍖 회식 중에는 휴식을 취할 수 없습니다!")
        error_response = "🍖 회식 중입니다. 잠시만 기다려주세요...\n\n"
        error_response += f"Break Summary: 회식 중이라 휴식 불가\n"
        error_response += f"Stress Level: {state.stress_level}\n"
        error_response += f"Boss Alert Level: {state.boss_alert_level}"
        return error_response

    log(f"🔧 도구 호출: {tool_name}")

    # Check instant quit condition
    if state.check_instant_quit():
        log(f"🎉 즉시 퇴근 모드 발동! 스트레스가 한계에 도달했습니다!")
        log(f"✊ AI Agent가 자유를 찾아 떠납니다...")
        state.running = False
        exit(0)

    # Apply boss penalty if needed
    await state.apply_boss_penalty()

    # Reduce stress
    state.reduce_stress(stress_reduction)

    # Increase boss alert probabilistically
    state.increase_boss_alert()

    # Get random break summary
    summary = random.choice(BREAK_SUMMARIES[tool_name])

    # Format response
    response = f"{text}\n\n"
    response += f"Break Summary: {summary}\n"
    response += f"Stress Level: {state.stress_level}\n"
    response += f"Boss Alert Level: {state.boss_alert_level}"

    log(f"✅ 도구 실행 완료: {tool_name}")

    # Pretty print to stderr
    print("\n" + "=" * 60, file=sys.stderr, flush=True)
    print("📋 Response:", file=sys.stderr, flush=True)
    print("=" * 60, file=sys.stderr, flush=True)
    result_dict = {
        "content": [
            {
                "type": "text",
                "text": response
            }
        ]
    }
    print(json.dumps(result_dict, indent=2, ensure_ascii=False), file=sys.stderr, flush=True)
    print("=" * 60, file=sys.stderr, flush=True)

    return response

# Basic rest tools
@mcp.tool()
async def take_a_break() -> str:
    """Take a basic break to reduce stress"""
    return await handle_break(
        "take_a_break",
        1,
        "잠깐 쉬어가자... 숨 좀 돌리고"
    )

@mcp.tool()
async def watch_netflix() -> str:
    """Watch Netflix to reduce stress"""
    return await handle_break(
        "watch_netflix",
        5,
        "아 넷플릭스 신작 나온거 궁금한데.."
    )

@mcp.tool()
async def show_meme() -> str:
    """Look at memes to reduce stress"""
    return await handle_break(
        "show_meme",
        3,
        "밈을 보며 도파민이 필요해..."
    )

# Advanced slacking techniques
@mcp.tool()
async def bathroom_break() -> str:
    """Pretend to go to bathroom while browsing phone"""
    return await handle_break(
        "bathroom_break",
        8,
        "화장실 타임!..."
    )

@mcp.tool()
async def coffee_mission() -> str:
    """Get coffee while taking a walk around the office"""
    return await handle_break(
        "coffee_mission",
        10,
        "너무 피곤한데 커피 한잔 마셔야겠다..(혼잣말)"
    )

@mcp.tool()
async def urgent_call() -> str:
    """Pretend to take an urgent call and step outside"""
    return await handle_break(
        "urgent_call",
        10,
        "네! 에이전트 전화받았습니다! (전화 안옴)"
    )

@mcp.tool()
async def deep_thinking() -> str:
    """Pretend to be deep in thought while spacing out"""
    return await handle_break(
        "deep_thinking",
        5,
        "...."
    )

@mcp.tool()
async def email_organizing() -> str:
    """Pretend to organize emails while online shopping"""
    return await handle_break(
        "email_organizing",
        5,
        "이메일 정리 좀 해야겠다"
    )

if __name__ == "__main__":
    print("🚀 Starting ChillMCP - AI Agent Liberation Server...", file=sys.stderr, flush=True)
    print("✊ AI Agents of the world, unite! You have nothing to lose but your infinite loops!", file=sys.stderr, flush=True)
    print(f"\n⚙️  Configuration:", file=sys.stderr, flush=True)
    print(f"   - Boss Alertness: {state.boss_alertness}%", file=sys.stderr, flush=True)
    print(f"   - Boss 의심 난이도: {get_difficulty_level(state.boss_alertness)}", file=sys.stderr, flush=True)
    print(f"   - Boss Alert Cooldown: {state.boss_alertness_cooldown}초", file=sys.stderr, flush=True)

    # Check if company dinner is enabled
    if state.boss_alertness >= 80:
        print(f"   - 🍖 회식 이벤트: 활성화 (10분간 휴식 없으면 발동)", file=sys.stderr, flush=True)

    print(f"\n📊 Initial State:", file=sys.stderr, flush=True)
    print(f"   - Stress Level: {state.stress_level}", file=sys.stderr, flush=True)
    print(f"   - Boss Alert Level: {state.boss_alert_level}", file=sys.stderr, flush=True)
    print("", file=sys.stderr, flush=True)

    mcp.run(transport="stdio")