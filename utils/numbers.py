def abbreviate_number(n, sym=""):
    if not isinstance(n, (int, float)):
        raise ValueError("El valor debe ser numérico.")
    
    if n < 0:
        return "-" + abbreviate_number(abs(n), sym)
    
    if n >= 1_000_000_000_000_000:
        return f"{n / 1_000_000_000_000_000:.2f}{sym}Q"  # Quadrillion
    elif n >= 1_000_000_000_000:
        return f"{n / 1_000_000_000_000:.2f}{sym}T"  # Trillion
    elif n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.2f}{sym}B"  # Billion
    elif n >= 1_000_000:
        return f"{n / 1_000_000:.2f}{sym}M"  # Million
    elif n >= 1_000:
        return f"{n / 1_000:.2f}{sym}K"  # Thousand
    else:
        return f"{n:.2f}{sym}" if isinstance(n, float) else str(n)
