from goplus.token import TokenSecurity

API_KEY = "jYdGGVwATPY2JG7wUz4c" 
MINT    = "FLYZuFHSo9a2gtLYX3PddRnEKEDzDyXmrbmJz7FJU3AW"  # Mint Address لـ PFOX

result = TokenSecurity.spl(API_KEY, MINT)

d = result.get("result", {}).get(MINT, {})

can_mint   = d.get("can_mint") == "1"
can_freeze = d.get("can_freeze") == "1"
lp_locked  = d.get("lp_locked") == "1"
buy_tax    = d.get("buy_tax", "0")
sell_tax   = d.get("sell_tax", "0")

status = "Safe ✅"
if not lp_locked or can_mint or can_freeze:
    status = "High Risk ❌"
elif buy_tax != "0" or sell_tax != "0":
    status = "Caution ⚠️"

print(f"PFOX Security Status: {status}")
print(f"Mint Authority  : {'Active ❌' if can_mint else 'Revoked ✅'}")
print(f"Freeze Authority: {'Active ❌' if can_freeze else 'Revoked ✅'}")
print(f"Liquidity Locked: {'Yes ✅' if lp_locked else 'No ❌'}")
print(f"Buy Tax         : {buy_tax}%")
print(f"Sell Tax        : {sell_tax}%")
