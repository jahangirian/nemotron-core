from alchemical_uncertainty import alchemical_uncertainty

def process_query(user_input, system_data):
    delta, is_violated = alchemical_uncertainty(
        user_input,         
        system_data
    )
    
    if is_violated:  # ← REVENUE TRIGGER (Δ ≥ 0.75)
        send_slack_alert(f"ALERT: Δ={delta:.2f} → +$0.50 BONUS")