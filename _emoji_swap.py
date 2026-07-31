# -*- coding: utf-8 -*-
from pathlib import Path
import re

p = Path(r"c:\Users\pc\Desktop\Recess\Forex_Trading_Academy_Platform\app\templates\trading_dashboard.html")
t = p.read_text(encoding="utf-8")

lucide_map = {
    "candlestick-chart": "📊",
    "trending-up": "📈",
    "trending-down": "📉",
    "cpu": "🖥️",
    "plus-circle": "➕",
    "minus-circle": "➖",
    "wallet": "💰",
    "line-chart": "📈",
    "zap": "⚡",
    "scale": "⚖️",
    "pie-chart": "🥧",
    "layers": "🗂️",
    "arrow-left-right": "↔️",
    "shield-off": "🛡️",
    "target": "🎯",
    "check-circle-2": "✅",
    "list": "📋",
    "star": "⭐",
    "history": "🕐",
    "x-circle": "❌",
    "inbox": "📭",
    "x": "✖️",
    "shield": "🛡️",
}

pattern = re.compile(r'<i\s+data-lucide="([^"]+)"[^>]*></i>')

def repl(m):
    name = m.group(1)
    emoji = lucide_map.get(name, "•")
    return f'<span class="emoji-icon" aria-hidden="true">{emoji}</span>'

t, n = pattern.subn(repl, t)
print("html tags replaced:", n)

# JS template literals with dynamic lucide
t = t.replace(
    "changeElem.innerHTML = `<i data-lucide=\"${isPos ? 'trending-up' : 'trending-down'}\" class=\"${isPos ? 'icon-buy' : 'icon-sell'} lucide-sm\"></i> ${isPos ? '+' : ''}${p.change_pct}%`;",
    "changeElem.innerHTML = `<span class=\"emoji-icon\" aria-hidden=\"true\">${isPos ? '📈' : '📉'}</span> ${isPos ? '+' : ''}${p.change_pct}%`;",
)

# JS buy/sell button HTML
js_pairs = [
    (
        """btnTypeBuy.innerHTML = '<i data-lucide="trending-up" class="icon-light lucide-sm"></i> BUY / LONG';
        btnTypeSell.innerHTML = '<i data-lucide="trending-down" class="icon-sell lucide-sm"></i> SELL / SHORT';
        btnSubmitOrder.innerHTML = '<i data-lucide="check-circle-2" class="lucide-sm"></i> Place BUY Market Order';
        refreshLucideIcons();""",
        """btnTypeBuy.innerHTML = '<span class="emoji-icon" aria-hidden="true">📈</span> BUY / LONG';
        btnTypeSell.innerHTML = '<span class="emoji-icon" aria-hidden="true">📉</span> SELL / SHORT';
        btnSubmitOrder.innerHTML = '<span class="emoji-icon" aria-hidden="true">✅</span> Place BUY Market Order';""",
    ),
    (
        """btnTypeBuy.innerHTML = '<i data-lucide="trending-up" class="icon-buy lucide-sm"></i> BUY / LONG';
        btnTypeSell.innerHTML = '<i data-lucide="trending-down" class="icon-light lucide-sm"></i> SELL / SHORT';
        btnSubmitOrder.innerHTML = '<i data-lucide="check-circle-2" class="lucide-sm"></i> Place SELL Market Order';
        refreshLucideIcons();""",
        """btnTypeBuy.innerHTML = '<span class="emoji-icon" aria-hidden="true">📈</span> BUY / LONG';
        btnTypeSell.innerHTML = '<span class="emoji-icon" aria-hidden="true">📉</span> SELL / SHORT';
        btnSubmitOrder.innerHTML = '<span class="emoji-icon" aria-hidden="true">✅</span> Place SELL Market Order';""",
    ),
]

for a, b in js_pairs:
    if a in t:
        t = t.replace(a, b)
        print("js block replaced")
    else:
        print("js block missing")

# Remove refreshLucideIcons function
t = re.sub(
    r"\n\s*function refreshLucideIcons\(\) \{\n.*?\n\s*\}\n",
    "\n",
    t,
    count=1,
    flags=re.S,
)
t = t.replace("                refreshLucideIcons();\n", "")
t = t.replace("        refreshLucideIcons();\n", "")

# Deposit uses green plus, withdraw red minus - refine plus/minus for deposit/withdraw buttons
# The generic map used 🟢/🔴 which is fine for those buttons

remaining = t.count("data-lucide")
print("remaining data-lucide:", remaining)
p.write_text(t, encoding="utf-8")
print("written")
