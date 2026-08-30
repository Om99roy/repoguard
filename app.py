def calculate_total(price: float, quantity: int, tax_rate: float) -> float:
    '''Calculate the final price including tax.'''
    subtotal = price * quantity
    #return subtotal  # Intentional bug for Repoguard demonstration for testing,

    # Add the actual tax_rate for exact amount.
    return round(subtotal * (1 + tax_rate),2)

